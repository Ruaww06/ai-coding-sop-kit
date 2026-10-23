# 设计依据

## 从职责出发

本版将 SOP v3.1 转成可按需调用的工程技能，而不是把旧流程换标题：入口处理接入、目标、授权、责任与路由；设计处理必要澄清、调研与证伪；实施处理完整影响范围内的最小改动与自测；验证处理依据、执行证据与验收；恢复处理失败止损、验证阻塞和交接。

技能为 `sop`、`sop-design`、`sop-execution`、`sop-verification`、`sop-recovery`；旧活动技能、模板库和重复规则已移除。以下描述设计决定，而非真实任务效果的验收结论。这不是必须逐一完成的五步。清晰低风险任务不强制设计文件，咨询不要求采用全套流程。只有共享授权和证据边界放入一份短 reference，其他规则随职责加载；无模板库、固定产物清单或独立大迁移协议。安装冲突与来源核验留在 INSTALL，不升格为业务流程。

预防的失效是：入口常驻过重、为流程制造工作、把模型自报当真实证据，以及精简时漏掉必要影响或安全边界。技能按触发条件描述，优先给可执行动作；不预建运行时、任务数据库、模型 API 或遥测。

## 语言与成立条件

执行内核（技能、共享边界、Agent 安装协议）维护一份英文正文，面向使用者的 README 和说明用中文；技能语言不要求用户改用英文交流。这样便于复用工程术语和外部技能习惯，并避免两套执行规则漂移；它不是“英文一定让模型更可靠”的实验证明。本版尚无中英文行为对照证据。

该结构成立的前提是：宿主能够发现并读取技能及相对资源，入口不成为固定仪式，各职责仍覆盖 SOP 的必要思想。若真实任务出现错误路由、反复加载造成明显成本、关键授权或调研遗漏，或英文义务强度被误读，就应修正触发、内容或拆分，而不是为守住五技能数量增加补丁。通过逐条语义复核和真实任务观察检查这些反例；脚本测试只能检查分发与部分文本约束。

## 实际查阅的 Superpowers 资料

2026-10-23 通过公开 GitHub API 和 raw 源码只读核验。固定提交 `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`，提交时间 2026-10-21；插件清单版本 `7.0.1`。以下文件均读取成功，不把移动 main 的未来内容当成本次依据。

| 来源 | 借鉴及适用边界 |
| --- | --- |
| [README](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/README.md) | 安装按宿主分别核实；部分宿主提供一句话交给 Agent 的指南，不等于所有客户端一种安装机制 |
| [入口技能](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/using-superpowers/SKILL.md) | 短入口教发现/调用，具体技能按需加载，宿主映射分开；不照搬“任何回应前必须调用” |
| [技能编写](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-skills/SKILL.md) | description 写触发条件，可复用方法而非单次会话叙述；只有需要时才拆重型参考，避免模板先行 |
| [需求与设计](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/brainstorming/SKILL.md) | 先读已有上下文再问，探索与调研可放在设计职责内；不继承固定设计目录、提交和强制计划串联 |
| [执行计划](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/executing-plans/SKILL.md) | 当前会话实施是可用选择，无需强制实现/测试分会话；不采用 Agent 自行裁决关键歧义的自主权 |
| [完成前验证](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/verification-before-completion/SKILL.md) | 先运行、读结果和退出码，再作声明；按当前版本及影响重验，不机械要求每次消息全量重跑 |
| [系统调试](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/systematic-debugging/SKILL.md) | 复现、定位、单假设验证与方法支持文件；其三次失败阈值不替代本版连续两次修复失败停机 |
| [宿主适配](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/docs/porting-to-a-new-harness.md) | 正文单源、薄适配，不改用户全局配置；不把其“必须自动启动注入”支持门槛强加到显式读取形态 |
| [Kimi 适配](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/docs/README.kimi.md) | 上游有原生清单/入口注入，说明宿主机制会变化；不是本工具包 Kimi 验收或新增适配授权 |

本次尝试读取旧 `.codex/INSTALL.md` 返回 HTTP 404，不再把该路径当作有效安装依据。Superpowers 的固定文档头、工作树、逐任务提交、fresh AI reviewer 和重型 ledger 都是其工程选择，不是本版通用底线。另开 AI 会话不能替代验收责任人，外部安装命令也不构成操作授权。

## 本工具包的接入依据与未确认项

调研前已检查仓库既有接入依据，继续引用 [Claude Code Skills](https://code.claude.com/docs/en/skills) 与 [Harness Skills 固定版本](https://github.com/deepseek-ai/deepseek-harness/blob/86a402200d95fecef4529d969836f1fe13c6cb0d/docs/subsystems/skills.zh.md)。它们支持项目技能接入的说明；本轮未重新核验宿主官方实现，旧版有限安装观察不冒充当前验收。

保留一句话 Agent 安装体验，但 Agent 必须确认项目、来源、冲突及真实加载；没有原生发现能力时如实说明。Claude 本地插件与项目技能分开，不默认叠加入口。本 Beta 的公开来源安装与真实任务行为仍待验证，见[测试说明](testing.md)。

结构是否有效要通过真实任务观察缺陷、返工、等待、验证成本与文档负担；不能以技能数量、字数或静态检查代替实际效果。
