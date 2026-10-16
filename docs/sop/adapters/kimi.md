# Kimi Code 手动接入

当前没有 Kimi 原生插件或 hook；使用同一份 `skills/` 正文，不复制一套 Kimi SOP。先按所用版本核对 Skills 发现规则，再依 [整组安装说明](../../installation.md) 将所有技能及资源放入实际支持的技能目录。

Kimi 支持相应语法时可显式 `/skill:sop <任务>`，以当前客户端发现结果为准，不承诺所有版本有该命令。不能只复制旧 `.agents/skills/sop/SKILL.md` 重定向文件；缺资源须报告，不跳过。

不改已有 AGENTS.md、全局配置或权限。无自动启动注入时显式读取入口；采用 SOP 仍需用户确认，安装不等于授权业务实现。

需要实测：技能发现、阶段触发、歧义停机、真实验证、连续失败停止和跨会话恢复。当前未在 Kimi 中安装验证，不能仅凭官方格式说明称兼容验收通过。

官方依据：
- https://moonshotai.github.io/kimi-code/zh/customization/agents.html
- https://moonshotai.github.io/kimi-code/zh/customization/skills.html
