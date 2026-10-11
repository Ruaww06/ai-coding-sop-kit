# DeepSeek Harness 接入

本说明对应官方仓库 `deepseek-ai/deepseek-harness`，不是在其他客户端中仅替换模型。

选择目标项目根目录为工作区。官方指令插件支持 AGENTS.md；base 组合默认集成，但 profile 可以关闭，需要可用的文件系统提供方。配置、预算和版本可能影响实际加载，先核对所用组合。

官方本地 Skill 提供方支持项目 `.agents/skills/`。确认相关提供方/消费方启用后，可发现 sop；未发现也直接读取工作流正文。不要套用其他客户端的斜杠命令。

指令插件不解析 Claude 的 `@path` 导入语法，本包不依赖该语法。使用 README 保底入口即可引导实际读取。

本包不安装框架、插件或配置，不保证任何本地 profile 的行为。需验证实际读取、必要停手、范围控制、真实验证及跨会话恢复。项目独立检查入口不会因换工具而变成可省略项。

官方依据：
- https://github.com/deepseek-ai/deepseek-harness
- https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/context/agent-instructions/README.zh.md
- https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.zh.md
