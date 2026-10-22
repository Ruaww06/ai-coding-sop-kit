---
name: sop-design
description: "Use when confirmed requirements need architecture, interface or data decisions, a design freeze, or a development plan and human-rated task dispatch before implementation."
---

# 设计冻结与派发准备

读取 [共同约束](../sop/references/common.md)、[阶段门槛](../sop/references/stages.md) 和 [门禁与档位](../sop/references/gates.md)。资源相对本技能，项目产物沿用项目位置。

## 操作

1. 先核对 DoR 和唯一调研记录，缺实际调研/人核验则回 requirements，不静默冻结假设。
2. 对影响其他模块的契约、所有权、生命周期、不变量、一致性、权限、量级、选型退出路径、观测和回滚前置决策。每条设计约束给失败场景，局部细节可延后。
3. 用 [冻结记录](../sop/assets/design.md) 引用接口契约、数据模型和 ADR。已有有效产物复用；无接口/模型时明确不存在及人评审依据，不创建空文档冒充完成。非功能目标仍要定义，H 只挂实际测量。
4. 设计冻结须真实确认。关键取舍没定不进入实现，不把 AI review 当作人批准。
5. 冻结后用 [开发计划](../sop/assets/plan.md) 拆单一可验任务，列硬依赖、不同的负责人/验收人、验收锚点；任务粒度和档位按规则。
6. AI 可建议档位，派发前由人判定、项目负责人确认。档位/状态只记计划， [派发单](../sop/assets/task.md) 回指编号，列范围、真实验证入口、基线、参考实现、检索词与命中。

## 出口

报告冻结三产物、真实决策来源、计划及派发缺项。只有任务、档位与实施授权齐备才转 execution；批准设计不自动批准业务代码、安装依赖或修改公共契约。

例：已有 API 和模型且本次无需修改时引用原文和版本，不重造一套；依赖挂掉时的行为仍需定义，不能留到编码时猜。
