# Kimi Code 接入

从目标项目根目录启动 Kimi Code。核对所用版本的项目指令与 Skills 发现规则，确认 AGENTS.md 和 `.agents/skills/sop/SKILL.md` 被加载或可读取。

支持相应命令的版本可显式使用 `/skill:sop <任务>`，但不是必需；通用入口已要求直接读取工作流正文。发现失败时使用 README 的保底指令，不跳过流程。

不要用初始化命令覆盖已有 AGENTS.md。保留人工裁决渠道，避免让无需询问的模式代替用户决定业务规则或风险取舍。

本包不安装 Hooks、修改配置或保证某版本实际行为。官方 Hooks 文档描述异常时可能放行，因此不能成为唯一安全防线；若项目需要，另行核对版本、失败行为和覆盖范围。

加载后验证：实际读取、需求歧义时停手、未验证不报通过、连续失败停手、跨会话恢复。客户端自报不是完整验收。

官方依据：
- https://moonshotai.github.io/kimi-code/zh/customization/agents.html
- https://moonshotai.github.io/kimi-code/zh/customization/skills.html
- https://moonshotai.github.io/kimi-code/zh/customization/hooks.html
