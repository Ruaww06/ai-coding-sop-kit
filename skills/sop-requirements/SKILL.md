---
name: sop-requirements
description: "Use when a development request is vague, requirements or acceptance criteria are missing, business assumptions need clarification, or pre-design research has not been verified."
---

# 需求澄清与调研

读取 [共同约束](../sop/references/common.md)、[路由](../sop/references/routing.md) 和 [需求与阶段门槛](../sop/references/stages.md) 中需求部分；跳过项还需核对 [门禁](../sop/references/gates.md)。文件相对本技能，不在项目根猜找插件资源。

## 操作

1. 恢复真实使用场景与需求确认来源。只提出草案，不替人回答业务取舍。
2. 按 [五轴澄清](../sop/assets/clarification.md) 填范围、边界、异常、约束、非功能；无歧义也给依据，不能交空清单。歧义给可选择的问题，等待人的答案。工具不支持提问也输出待答项并停下。
3. 用 [需求卡](../sop/assets/requirements.md) 写可断言验收、非范围、约束、依赖与异常。最低数量以规则为准，不为凑数发明功能、数字或外部事实。
4. 用 [唯一调研记录](../sop/assets/research.md) 比较外部候选并检索项目负向知识；链接来自本次实际检索，标核验日期、人核验来源。未查写未调研，不能凭记忆补链接。
5. 需求必须真机/实测的验收显式标注；按 DoR→DoD 映射对应断言、真实依赖和后续证据。
6. 纯机械改动申请 S 时记录人判定与依据，未批准不跳澄清；S 不免除其他 B。

## 出口

列 DoR 已有证据、尚缺项和待谁确认。未过门槛不设计冻结、不实现。齐备后转 design；不把“需求草案已写”称为已批准。

例：“做个笔记工具”先问用户场景与边界，不自选框架开始编码；没有检索能力就明确未调研，不提供虚构仓库链接。
