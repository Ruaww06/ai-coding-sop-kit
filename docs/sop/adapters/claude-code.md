# Claude Code 接入

使用支持原生 AGENTS.md 的版本，从目标项目根目录启动。优先共用唯一 AGENTS.md，不默认增加 CLAUDE.md 兼容层。

官方文档说明从 2.1.277 起支持 AGENTS.md。默认回退条件包括：工作目录及祖先目录无 CLAUDE.md、.claude/CLAUDE.md 或 CLAUDE.local.md，相关内置支持未禁用。接入者核对自己的版本、目录和加载状态，不假设所有环境自动读取。若项目已有 Claude 指令入口，不删除它；按项目约定合并引用或显式读取。

AGENTS.md 原生支持不等于自动发现 `.agents/skills/`。官方 Skills 文档列出项目 `.claude/skills/`；本包不提供额外 Skill 副本，不保证 `/sop` 注册。常驻入口直接要求读取唯一工作流正文即可。

无需手动调用 Skill。加载不确定时发送 README 的保底指令，核对实际读取与任务恢复，不只依据 Agent 承诺。

本包不安装 Hooks、权限或 CI。需要程序门禁时由接入项目另行实施和验证，不能把模型指令视为强制阻断。

官方依据：
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/skills#where-skills-live
