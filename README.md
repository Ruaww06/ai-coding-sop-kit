# AI Coding SOP Kit

给 AI 编程助手的一套开发流程技能：先澄清需求，再设计和实现；用实际测试支撑交付，在失败或缺少外部条件时停下来处理。

当前版本：**2.0.0-beta.1**。支持 Claude Code 本地插件；DeepSeek Harness 提供 Agent 辅助的项目级技能安装指南。

## 发一句话给 Agent 安装

在 DeepSeek Harness 中先选中要使用的项目，再发送：

```text
请获取并遵循 https://raw.githubusercontent.com/Ruaww06/ai-coding-sop-kit/refs/heads/docs/sop-v2/INSTALL.md，将 AI Coding SOP Kit 安装到当前 DeepSeek Harness 项目；遇到同名冲突先询问。
```

Agent 按指南获取同一版本的七个技能及资源，检查冲突并报告结果。需要网络和项目文件操作能力；权限不足或已有同名修改时应停下询问，新技能可能需要重开会话才能发现。

这是一份供 Agent 执行的安装协议，不是独立安装器；DeepSeek Harness 端到端安装仍待实测。其他客户端需先确认各自技能目录。详见 [Agent 安装指南](INSTALL.md)。

## Claude Code 命令行快速开始

需要 Git，以及已安装并登录的 Claude Code。无需为本工具包额外安装 Python、模型 SDK 或配置 API Key；模型使用费用由你的客户端账户承担。

### 1. 获取 beta

在尚不存在的新目录获取最新 beta 分支（包含精简后的目录结构）：

```sh
git clone --branch docs/sop-v2 --single-branch https://github.com/Ruaww06/ai-coding-sop-kit.git ai-coding-sop-kit-beta
```

分支会随修复更新；需要固定历史版本时可使用 `v2.0.0-beta.1` 标签，该标签不包含后续目录精简。当前仅提供本地插件加载，不提供 marketplace 安装。

### 2. 在你的项目中加载

进入你要开发的项目目录，启动 Claude Code。将下面路径替换为刚克隆目录的绝对路径；路径含空格时保留引号。

```sh
claude --plugin-dir "/absolute/path/to/ai-coding-sop-kit-beta"
```

这只为当前会话加载插件，不是全局安装，也不会自动覆盖项目的 `AGENTS.md` 或 `CLAUDE.md`。

### 3. 调用入口并描述任务

```text
/ai-coding-sop-kit:sop
我想做一个个人笔记工具。请先帮我澄清需求，暂时不要写代码。
```

也可以从现有项目开始：

```text
/ai-coding-sop-kit:sop
请先阅读这个项目，说明结构和现有测试，不修改文件。
```

入口会按任务情况选择阶段，不需要依次手动调用所有技能。完整开发流程包含需求确认、设计冻结、测试档位和独立验收；缺少前置条件时，助手应说明缺项，而不是直接开始实现。

## 适合做什么

- **澄清需求**：梳理范围、边界、异常、约束和可断言的验收标准。
- **设计与派发**：明确接口、数据、关键取舍及允许修改的文件。
- **范围内实现**：先复现问题，使用项目现有检查入口，保留他人改动。
- **验证与交付**：区分实际测试结果、独立评审和需求方验收。
- **失败恢复**：记录尝试和失败次数，避免换会话后从零重试；外部验证缺失时申请挂起并保留恢复条件。

咨询和只读了解不需要先建立整套开发文档。插件加载也不代表项目自动采用完整流程；需要时由你明确确认。

## 可用技能

| 技能 | 用途 |
| --- | --- |
| `sop` | 入口、阶段选择、恢复任务范围 |
| `sop-startup` | 项目采用流程、准备规约和记录入口 |
| `sop-requirements` | 需求澄清、验收标准与调研 |
| `sop-design` | 设计冻结、计划和任务派发 |
| `sop-execution` | 已授权任务的实现与短回路测试 |
| `sop-verification` | 检查证据并准备交付 |
| `sop-recovery` | 失败归因、挂起与交接恢复 |

Claude Code 中的完整命令为 `/ai-coding-sop-kit:<技能名>`。

## 项目文件与权限

技能、共享规则和模板在工具包目录中；代码、需求、计划和问题记录保存在你的项目里，沿用已有记录位置。插件不会自动初始化项目、提交代码、安装依赖或部署。

启动 hook 只提供导航，不运行项目测试或执行文件操作。**技能是模型指引，不是权限沙箱或审批系统**；重要改动仍应使用客户端权限控制，并由你审阅实际差异和测试结果。

## beta 支持范围

已进行打包测试，以及 Claude Code 的本地加载、启动、原生 resume 和有限任务场景测试。模型行为测试不构成普遍可靠性保证；最新规则调整尚未重新进行模型行为测试。

以下仍未完成验证：

- 原生 clear／compact 后的恢复。
- marketplace 分发（当前不提供）。
- 其他客户端的原生接入。
- 真实设备、长期挂起及复杂并发任务。

建议先在低风险项目或独立分支试用。详见[安装与更新](docs/installation.md)和[测试与兼容性](docs/testing.md)。

## 更多文档

- [安装、更新与移除](docs/installation.md)
- [从旧文档包迁移](docs/sop/migration-v2.md)
- [流程规则索引](docs/sop/workflow.md)
- [模板索引](docs/sop/templates.md)
- [贡献指南](CONTRIBUTING.md)
- [版本变更](CHANGELOG.md)

## 许可证

[MIT](LICENSE)。工具包不提供遥测或模型 API 集成；使用技能时，客户端仍会按其自身的数据与计费政策处理你的项目上下文。
