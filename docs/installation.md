# 安装、更新与移除

## 让任意编程 Agent 安装

在所用 Agent 中选中业务项目，把同一句话发给 Agent，由它确认能力与接入方式：

```text
请获取并遵循 https://raw.githubusercontent.com/Ruaww06/ai-coding-sop-kit/refs/heads/docs/sop-v2/INSTALL.md，识别当前 Agent 的接入方式，将 AI Coding SOP Kit 安装到当前项目；遇到冲突先询问，已有旧版先预览迁移差异，不擅自改写项目规约。
```

[安装指南](../INSTALL.md)让 Agent 负责能力/宿主识别、获取、完整性检查、冲突处理和结果验证。Claude Code 项目技能目录是 `.claude/skills/`，Harness 是 `.dsh/skills/`，七个技能同层；未知宿主先核实文档，不直接沿用这些目录。无原生技能机制时可在取得授权后采用显式文件读取，并如实区分它与原生安装。不能联网/读写时报告缺项，不假称已安装。

只安装当前项目，不改账户、密钥或全局配置，不自动开始业务开发。先只读识别旧版/混合入口；业务规约迁移须先预览差异并获明确授权。已有本地插件或用户级同名技能时需确认采用方式和实际加载来源，不默认新增第二套入口。拒绝迁移或加载未验证时保留旧入口，分别报告技能安装与项目未迁移。

### Claude Code 项目技能

安装整组技能到当前项目 `.claude/skills/` 后，以实际发现的 `sop` 调用（用户入口 `/sop`），核对入口及共享资源来源。它不含 `.claude-plugin/`、SessionStart hook 或 `ai-coding-sop-kit:` 命名空间，不需要每次传 `--plugin-dir`。写入 `.claude/` 可能触发宿主的额外审批，安装授权不改变权限策略；被拒绝时停下，不绕过。

需要时在同一项目新建会话核验，不自动启动模型进程。Claude Code 已有限验证本地候选指南的 Agent 文件安装、内容一致性、普通新会话原生发现及项目技能实际调用；公开 URL 获取仍待验证。Harness 端到端仍未实测；已有本地插件实测不能替代这些验证。

## Claude Code：本地插件（可选）

需要已安装并登录的 Claude Code，以及用于获取源码的 Git。

### 获取工具包

克隆最新 beta 分支到新目录，不要覆盖已有副本：

```sh
git clone --branch docs/sop-v2 --single-branch https://github.com/Ruaww06/ai-coding-sop-kit.git ai-coding-sop-kit-beta
```

需要固定历史版本时，可将分支名替换为 `v2.0.0-beta.1`；该标签保持不变，不含后续的旧入口与市场清单移除。

### 在项目中启动

进入你要开发的项目目录，使用工具包的绝对路径：

```sh
claude --plugin-dir "/absolute/path/to/ai-coding-sop-kit-beta"
```

`--plugin-dir` 仅为该会话加载，不修改全局插件配置。路径含空格时需要引号。进入会话后调用：

```text
/ai-coding-sop-kit:sop
请先了解项目，暂时不要修改文件。
```

确认技能列表包含七个 `ai-coding-sop-kit:sop*` 入口，并检查启动导航。仅凭模型说“已经加载”不足以判断成功。插件不会自动创建项目规约，也不会覆盖已有 `AGENTS.md` 或 `CLAUDE.md`。

### 更新与移除

固定标签副本不会自动更新。升级时获取新版本的独立副本，阅读变更说明，再将 `--plugin-dir` 指向新目录。重启会话后核对版本，不假定运行中缓存已经更新。

装过 v1 文档包的项目不能只更换 `--plugin-dir`：加载新版后对 `sop` 入口说“检查旧 SOP 并预览迁移，先不要改文件”。入口按[迁移协议](../skills/sop/references/migration.md)核对旧规则和活动 Skill，经授权后才切换；重跑前重读现状和授权，不覆盖新增定制。详见[旧项目迁移](sop/migration-v2.md)。

停止在新会话中传入 `--plugin-dir` 即可停止加载该副本。项目中已创建的需求、计划和代码仍然保留；不要把移除插件理解为撤销项目改动。

## marketplace 状态

当前不分发 marketplace 清单。项目技能使用上述 Agent 安装协议；插件形态使用源码加 `--plugin-dir` 加载，请勿把仓库地址直接用于 marketplace 安装命令。既有标签的内容保持不变，精简目录结构的版本从下述 beta 分支获取。

## 其他 Agent Skills 客户端

以下为手动接入方法，尚未完成客户端实测：

1. 核对所用客户端的技能目录、发现和信任机制。
2. 将完整 `skills/` 的所有子目录作为一组复制到技能目录，保留相邻关系；共享资源在 `sop/references/` 和 `sop/assets/`。不要只复制一个 `SKILL.md`。
3. 已有同名目录时先比较，不整目录覆盖。保留 MIT 许可证；可将原 `LICENSE` 放在安装副本的 `sop/LICENSE`。
4. 不复制仓库的 `.git`、维护者 `AGENTS.md` ，不覆盖业务项目许可证或规约。
5. 没有 hook 时显式调用入口，或按客户端能力读取 `sop/SKILL.md`。资源路径以技能目录为基准，不要求目标项目存在 `docs/sop/`。

更新前保留定制并比较差异；不要把项目任务记录写入技能副本。

适配说明：[Claude Code](sop/adapters/claude-code.md)、[Kimi](sop/adapters/kimi.md)、[DeepSeek Harness](sop/adapters/deepseek-harness.md)。

## 支持范围

| 接入方式 | 状态 |
| --- | --- |
| Claude Code 项目技能 | 本地候选文件安装、普通新会话原生发现及真实调用已有限验证；公开获取未验收 |
| Claude Code 本地插件 | 已验证本地发现、startup、原生 resume 和有限任务场景 |
| Claude Code marketplace | 当前不提供 |
| DeepSeek Harness | Agent 安装指南，端到端安装/加载未实测 |
| Kimi | 手动接入说明，未实测原生安装 |
| 其他文件型 Agent | 可按能力显式读入口，不承诺原生发现 |

clear／compact、其他系统及行为测试的局限见[测试与兼容性](testing.md)。
