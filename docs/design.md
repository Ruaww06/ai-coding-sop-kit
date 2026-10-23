# 设计依据

## 从职责出发

本版将 SOP v4.0 转成面向需求驱动全栈交付的按需技能。v1 的需求/设计评审与分层回流、v2 的启动/澄清/调研/计划进度及挂起恢复，作为需要承接的机制；v3 的简单优先、复用与最小完整改动用于降低实施和流程成本，不能替代评审与责任。

保留 `sop`、`sop-design`、`sop-execution`、`sop-verification`、`sop-recovery`，新增 `sop-requirements`。需求技能独立承担澄清、需求负责人确认和非起草者评审，防止“文档完整”被误认为“已审过”。设计技能保留调研并明确关键设计评审，检查完整场景如何穿过交互、接口、业务和数据。实施关联依赖、责任、验收、验证和进度；验证要求适用的跨层证据；恢复成为所有阶段的反馈与关闭路径，不能只在测试失败后加载。

这不是必须逐一调用的六步。局部任务复用有效评审与授权，只确认变化部分；调查不要求采用全套流程。共用边界保持短，细节随职责加载；无固定文档套装、模板库、会议或输出顺序。所有任务可合并记录，但不能省略必要判断。

升级保留 v3 的五个入口、公共资源路径和接入形态，新增技能不自动授权改写项目规则。v2 同名需求技能需内容比较，不能保留旧规则并假称兼容。历史项目中的有效评审、授权、失败次数与未完成验证保留；缺失评审补充受影响判断，不能追认或全量重写。安装冲突从 INSTALL 进入，安全切换步骤仍按需读取，不成为新项目仪式。

这些决定防止过重入口、无意义产物、模型自证、局部实现与端到端需求脱节、反馈不写回及精简漏掉经验。技能按触发条件提供动作，不预建运行时、任务数据库、模型 API 或遥测。

## 语言与成立条件

执行内核（技能、共享边界、Agent 安装协议）维护一份英文正文，面向使用者的 README 和说明用中文；技能语言不要求用户改用英文交流。这样便于复用工程术语和外部技能习惯，并避免两套执行规则漂移；它不是“英文一定让模型更可靠”的实验证明。本版尚无中英文行为对照证据。

该结构成立的前提是：宿主能够发现并读取技能及相对资源，入口不成为固定仪式，各职责仍覆盖 SOP 的必要思想。若真实任务出现错误路由、反复加载造成明显成本、关键授权或调研遗漏，或英文义务强度被误读，就应修正触发、内容或拆分，而不是为守住技能数量增加补丁。通过逐条语义复核和真实任务观察检查这些反例；脚本测试只能检查分发与部分文本约束。

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

保留一句话 Agent 安装体验，但 Agent 必须确认项目、来源、冲突及真实加载；没有原生发现能力时如实说明。Claude 本地插件与项目技能分开，不默认叠加入口。v4 以 Beta 预发布供试用，公开来源安装、原生加载与真实任务行为均待验证；历史观察不冒充新版结果，见[测试说明](testing.md)。

结构是否有效要通过真实任务观察缺陷、返工、等待、验证成本与文档负担；不能以技能数量、字数或静态检查代替实际效果。
