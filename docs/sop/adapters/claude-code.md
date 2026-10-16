# Claude Code 插件接入

v2 使用原生插件，不依赖 AGENTS.md 自动加载，也不为用户创建 CLAUDE.md 兼容层。插件根的维护者 AGENTS.md 不复制到目标项目。

- 技能统一放 `skills/<name>/SKILL.md`，入口 `/ai-coding-sop-kit:sop`。
- `.claude-plugin/plugin.json` 声明包元数据，marketplace.json 提供同仓库分发；尚未发布时使用本地 `--plugin-dir`。
- SessionStart 只读导航覆盖 startup/resume/clear/compact；不运行项目检查、不写项目文件、不证明批准、不硬阻断工具。
- 插件资源相对技能文件或插件根；shell cwd 仍是项目位置，不能猜插件文件在项目 docs 下。
- 安装、加载、实际触发和遵循流程分别核验。旧 `.agents/` 仅重定向，不与原生插件同时注册。

安装/更新及发布状态见 [安装说明](../../installation.md)，测试见 [测试说明](../../testing.md)。

官方依据：
- https://code.claude.com/docs/en/plugins/create
- https://code.claude.com/docs/en/plugins/manifest-reference
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/hooks#sessionstart
