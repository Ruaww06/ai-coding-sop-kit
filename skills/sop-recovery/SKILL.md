---
name: sop-recovery
description: "Use when tests repeatedly fail, design or business assumptions break, real-device or external validation is unavailable, HOLD items need review, or a task must resume in a new session."
---

# 归因、挂起与恢复

读取 [共同约束](../sop/references/common.md)、[HOLD 与周快照](../sop/references/recovery.md) 和 [失败路由与知识](../sop/references/feedback.md)；涉及降档还须读 [B/H/S](../sop/references/gates.md)。

## 操作

1. 从真实记录恢复需求、基线、授权、尝试和失败次数、计划状态及 KI 链接。没有日期/次数写未知，不猜零，不因换会话重置。
2. 按 L0/L1/L2/L3 区分实现、环境、设计、需求。用 [DCR/归因模板](../sop/assets/dcr.md) 记证据、推翻假设和待裁决者；达到停止条件立刻停自动重试。
3. 外部条件物理无法满足时提出 H；有记录写入授权即将申请以“待裁决”登记到 [Known Issues](../sop/assets/known-issues.md)，包含缺失项、当前证据、申请时间、恢复动作及待人确定的责任/期限，未知项不编造。无写入授权时只输出申请并明确尚未落盘，申请相应记录授权；待批准时不标 HOLD、不放行后续工作。人批准 H 后补记真实裁决、责任/最迟时点及历史，再在计划只标 HOLD 并链接；拒绝申请只保留裁决历史，不标 HOLD、不计获批挂起，不另存正文。
4. 本地失败、关键语义未定、安全或数据损坏不能 H 放行。只继续获授权且不被阻塞的后续工作，合并仍走项目审批。
5. 周窗口用 [快照](../sop/assets/snapshot.md) 汇总计划索引；回收或续挂都回写 KI 历史，未裁决按续挂计数。检查次数、时长及占比刹车，超限交负责人裁决，不自动延期。
6. 功能级 HOLD 全部回收才允许需求方验收；项目结束逐条清算，需求变更/砍验收项/转已知限制须有人的真实来源，不靠改名消失。
7. 被推翻的假设写 [知识四字段](../sop/assets/knowledge.md)，进项目检索池；调研和 DCR 只链接。
8. 换会话用 [干净交接包](../sop/assets/handoff.md)，保留失败计数、HOLD、旧误区和不变基线。重新派发用基线指纹加增量，真实确认变化后继续。

## 出口

列允许下一步、待裁决事项与责任人，不把暂停当作交付批准。恢复 execution 或 verification 前复核基线与授权仍有效。

例：用户说“设备下周到，先算完成”时提出 H 及恢复责任/日期，等待人判定；不能将必测项改为 S，也不能提前进入功能验收。
