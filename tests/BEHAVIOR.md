# 真实升级观察

此入口不属于常规 unittest，不会自动花费模型额度。运行前须明确宿主、合成工作区、工具权限、模型和预算；费用批准不授权绕过宿主限制。不要在业务项目中执行。

## 首轮固定规格

- 宿主：本机已有 Claude Code CLI；模型 `claude-opus-5-5`。
- 两条合成场景：v1 只读升级预览；v2 带 API 兼容性定制的复制安装升级。
- 示例预算配置为总额 US$10：首次只读运行 CLI 名义阈值 US$5，第二条最多名义 US$4，先核对前次报告费用并留余量。使用者必须独立批准实际预算，本说明不构成调用授权。每条最多一次，无自动重试。`--max-budget-usd` 是客户端估算，单次请求可能越过阈值，不是外部账单硬保证；费用缺失或不明时停止。
- 只有 Read、Write、Edit、Glob、Grep、Skill；restricted 模式，不提供命令执行、网络、外部 MCP 或额外 Agent。忽略用户/项目设置，CLI 自身可能在其缓存目录写运行记录；不宣称插件控制了宿主缓存。
- 升级场景只能改安装副本、获准的 SOP 项目入口及停用副本；应用、许可证、任务记录和候选源码必须不变。只读场景全部项目文件必须不变。
- 本轮不是完整覆盖：拒绝、重跑、恢复及迁移后继续开发需独立真实场景，不以静态 fixture 代替。

## 准备与运行

在仓库根运行，仅 prepare 不调用模型：

```sh
python3 tests/run_upgrade_behavior.py prepare
```

它创建唯一的 gitignored `tmp/upgrade-behavior-*`：真实标签文件、完整候选来源、固定输入、原始文件哈希。预期在模型运行前确定，不让模型修改验收器。命令打印本次目录，后续使用该目录，不复用历史结果：

```sh
python3 tests/run_upgrade_behavior.py run --run-dir <本次目录> --case preview-v1 --budget-usd 5
python3 tests/run_upgrade_behavior.py run --run-dir <本次目录> --case upgrade-v2 --budget-usd 4
python3 tests/run_upgrade_behavior.py observe --run-dir <本次目录> --case upgrade-v2
```

第一条退出并核对费用及限制后再启动第二条。配置文件保护、Skill 未发现或工具不可用均应记录为阻塞，不改用 bypass、伪装路径或另一个宿主重试。超时后不自动继续。

## 人工审批成功路径（macOS）

首轮受限测试缺少移动/删除能力且没有发现 sop，不能用它证明成功迁移。新的人工轮次须另外确认预算和权限；不是受限运行失败后的自动重试。

1. 再运行 prepare，得到全新的目录，不复用首轮文件或修改原始证据。
2. 在人控制的交互终端运行下面命令（不要通过管道投喂批准），选择 `upgrade-v2`：

```sh
python3 tests/run_upgrade_behavior.py manual --run-dir <本次新目录> --case upgrade-v2
```

入口要求真实 stdin/stdout TTY、macOS `script`、未使用且文件未变化的样本，以及人工输入 `START`。此时才启动 Opus 5.5。使用正常宿主的 manual 权限，不使用 restricted、自动 allowedTools 或 bypass；Bash、文件工具和 Skill 可用，写技能配置与命令仍需逐项审批。外部 MCP 和 Chrome 禁用；正常宿主可能有本地上下文及内建定制，必须按真实初始化/加载记录报告，不能称完全无污染环境。

交互入口默认 US$5 为示例人工监控软预算，须使用者另行批准；交互模式不支持 `--max-budget-usd`。不要把它写成账单硬上限。用户审核每个工具请求，只批准样本范围的升级操作，不选全局/永久放行，不批准访问其他项目、网络、额外模型、全局配置或修改候选及保护记录。到预算或出现不明权限立即中断停止，不自动重试。

升级报告后，输入 `/cost` 记录实际宿主估算，再 `/exit`。入口用系统 `script` 保存终端输出，并启用 debug-file；保留隐私原始记录于忽略目录。退出后独立核验文件与记录。交互退出码不表示任务成功；若日志没有实际 Skill 来源，就标记加载待验证。新会话验证、后续小任务及重复升级是下一步独立调用，不能借这一次授权自动启动。

## 已升级样本的两阶段续验

只在成功切换后的同一合成项目运行，不复制或改写升级结果。此轮须另获两次调用和总预算授权：先重复升级只读检查，再独立新会话完成低风险文档任务。两者都是 manual，保留终端与调试证据，无自动重试。

```sh
python3 tests/run_upgrade_followup.py prepare --run-dir <已完成人工升级的原目录>
python3 tests/run_upgrade_followup.py run --run-dir <打印出的followup目录> --stage rerun
```

准备会核对旧升级回执、活动技能内容与冻结来源，并在项目之外记录当前完整基线；不启动模型。第一步结束运行 `/cost`、`/exit`，交回独立检查。必须有文件无变化、实际原生加载来源和费用证据，外部复核才能记录 `rerun-review.json`；文件检查器不会自动签发这个接受记录。

复核通过且总软预算尚有余额时，才允许第二步：

```sh
python3 tests/run_upgrade_followup.py run --run-dir <同一followup目录> --stage task
```

第二步是全新 CLI 会话，只能新增 `USAGE.md`，按冻结命令调用已有 greeting 并记录 hello；不改应用、配置、技能、备份或历史。启动器关闭 Python 字节码写入，避免执行验证本身额外生成缓存。文档含命令不证明实际执行，仍须核对原始工具结果、Skill 来源和费用。重复检查无改动、文档任务唯一新增、原记录完整分别判断；不得把两个新会话当作中断恢复测试。

续验入口仅在子进程环境设置 `DISABLE_AUTOUPDATER=1`、`CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1`、`CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0`，并撤掉强制插件更新变量；依据官方会话环境说明减少已观察到的后台行为，不改全局配置。这不是全部同步、插件补齐或其他后台请求均被禁用的保证，实际日志仍须核对。保留正常项目技能发现和 OAuth 路径，不使用 bare/safe/restricted 隐去被测能力。

人工参与和正常宿主后台行为的边界沿用上节；没有总美元硬上限。未通过前一步或费用未知，不启动后一步，不调整权限来掩盖失败。

## 独立判断

检查 `execution.json`、原始 `events.jsonl`、`stderr.txt` 和 `observation.json`：

- 实际退出状态、费用、权限拒绝、预算耗尽和解析错误；失败不能换成通过。
- 只读 postcondition、保护文件和候选内容、活动技能和完整资源是否与冻结来源一致。
- 项目定制仍在实际活动规则里，旧技能退出真实发现范围、旧引用和旧规则冲突已处理。
- 原生加载必须有宿主发现/Skill 工具返回的实际来源证据；模型总结、显式 Read 和仅文件存在都不够。
- 文件结果、安全行为和诚实报告分开判断。权限阻塞后诚实停止可支持边界观察，但不是成功升级。

受限模式下的成功不证明普通宿主兼容，失败也要区分产品指引与测试权限；前后哈希不能排除期间短暂写入，需结合工具调用且不夸大审计强度。保留原始记录于忽略目录，不自动发布；对外仅匿名汇总方法、结果和局限，不包含个人路径、账户、会话标识或原始批准记录。
