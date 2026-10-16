#!/bin/sh
set -eu

base=${1:?base SHA required}
head=${2:?head SHA required}
event=${3:?event name required}
forced=${4:-false}
case "$forced" in
  true|false) ;;
  *) printf '%s\n' 'Expected explicit forced-event boolean' >&2; exit 2 ;;
esac

for sha in "$base" "$head"; do
  case "$sha" in
    ''|*[!0-9a-fA-F]*) printf '%s\n' 'Expected hexadecimal commit SHA' >&2; exit 2 ;;
  esac
  case ${#sha} in
    40|64) ;;
    *) printf '%s\n' 'Expected full commit SHA' >&2; exit 2 ;;
  esac
done
case "$event" in
  push|pull_request) ;;
  *) printf '%s\n' 'Unsupported event' >&2; exit 2 ;;
esac

# A branch deletion has no new patch. A new branch compares its full tree.
case "$head" in
  *[!0]*) ;;
  *)
    if [ "$event" = push ]; then exit 0; fi
    printf '%s\n' 'PR head must identify a commit' >&2; exit 2 ;;
esac
git cat-file -e "$head^{commit}"
# History replacement may intentionally make the old object unavailable.
# Validate the full current tree without fetching withdrawn history.
if [ "$event" = push ] && [ "$forced" = true ]; then
  base=$(git hash-object -t tree --stdin </dev/null)
  git diff --check "$base" "$head" --
  exit 0
fi
case "$base" in
  *[!0]*)
    git cat-file -e "$base^{commit}"
    if [ "$event" = pull_request ]; then
      base=$(git merge-base "$base" "$head")
    fi
    ;;
  *)
    if [ "$event" != push ]; then
      printf '%s\n' 'PR base must identify a commit' >&2; exit 2
    fi
    base=$(git hash-object -t tree --stdin </dev/null)
    ;;
esac

git diff --check "$base" "$head" --
