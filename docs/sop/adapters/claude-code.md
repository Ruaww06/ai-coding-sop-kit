# Claude Code 接入

## 一句话项目技能安装

与其他 Agent 使用同一个[安装入口](../../../INSTALL.md)，由 Agent 确认目标项目和能力，将七个技能作为一组放入项目 `.claude/skills/`。入口为实际发现的 `sop`（用户命令 `/sop`），阶段技能同层，共享资源随组保留。这是项目技能，不是插件安装：不含插件命名空间、清单或 SessionStart hook，不修改全局配置。写入 `.claude/` 触发额外审批时停止等待，不把用户安装意愿当作已解除宿主限制。

仅文件存在不证明当前会话已发现；应实际调用并检查来源，必要时在同一项目新会话核验。已有用户技能、插件或旧项目入口时比较冲突并确认采用方式，不默认叠加第二套流程。已有限验证本地候选指南的 Agent 文件安装、普通新会话原生发现及项目技能实际调用；公开 URL 获取仍待验证。restricted 测试会话未列出项目技能，不应把这种受限发现结果等同普通会话；文件存在、原生发现和实际调用分别报告。

## 可选本地插件

v2 也提供原生插件，不依赖 AGENTS.md 自动加载，不为用户创建 CLAUDE.md 兼容层。插件根的维护者 AGENTS.md 不复制到目标项目。

- 技能统一放 `skills/<name>/SKILL.md`，入口 `/ai-coding-sop-kit:sop`。
- `.claude-plugin/plugin.json` 声明插件名称和版本等元数据；当前使用固定版本源码及 `--plugin-dir` 加载，不提供 marketplace 清单。
- SessionStart 只读导航覆盖 startup/resume/clear/compact；不运行项目检查、不写项目文件、不证明批准、不硬阻断工具。
- 插件资源相对技能文件或插件根；shell cwd 仍是项目位置，不能猜插件文件在项目 docs 下。
- 安装、加载、实际触发和遵循流程分别核验。新版本只分发 `skills/` 入口；迁移时不要同时注册项目中遗留的旧入口。

安装/更新及发布状态见 [安装说明](../../installation.md)，测试见 [测试说明](../../testing.md)。

官方依据：
- https://code.claude.com/docs/en/plugins/create
- https://code.claude.com/docs/en/plugins/manifest-reference
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/hooks#sessionstart
