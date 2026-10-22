#!/bin/sh
set -eu

root=${CLAUDE_PLUGIN_ROOT:?CLAUDE_PLUGIN_ROOT must point to the installed plugin}
entry="$root/skills/sop/SKILL.md"
bootstrap="$root/hooks/bootstrap.md"

if [ ! -f "$entry" ] || [ ! -f "$bootstrap" ]; then
  printf '%s\n' 'SOP bootstrap: bundled entry or guidance is missing.' >&2
  exit 1
fi

printf '%s\n' 'AI Coding SOP Kit is available. Entry skill: ai-coding-sop-kit:sop'
printf 'Fallback entry file: %s\n\n' "$entry"
cat "$bootstrap"
