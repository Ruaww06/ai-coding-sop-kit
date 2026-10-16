---
name: sop-execution
description: "Use when implementing, fixing or refactoring a dispatched task with confirmed requirements, frozen design, human-confirmed test tier and explicit implementation scope."
---

# 范围内执行

读取 [共同约束](../sop/references/common.md)、[派发规则](../sop/references/stages.md)、[门禁与测试](../sop/references/gates.md) 和 [失败归因与停机条件](../sop/references/feedback.md)。不要因直接调用本技能而绕过需求、设计或人定档位。

## 操作

1. 恢复真实派发、计划编号/档位、实施授权、验收、允许文件和开始基线；读项目规约、目标代码、调用关系、契约、已有测试及同类实现。
2. 复述目标、非范围、验收和假设。缺前置证据报缺项，转正确阶段；已确认同一授权不反复索批。
3. 引用唯一调研记录，报告内部检索词和命中，避免重复实现被否决方案。
4. 修 bug 先有失败复现测试，按档位做实现/独立验证短回路。预期来自需求、外部规格或不变量，不复制实现作为断言。
5. 仅改白名单及已授权新增文件。新增依赖、公共接口、schema、验收、风险或范围变化停下请求相应裁决，不顺手重构、不改门禁让测试过。
6. 使用项目真实检查入口，核对新增路径、白名单和依赖锁；缺能力报未完成，测试后代码再变重验。
7. 失败先归因；达到停止条件或涉及高风险时转 recovery，不无限重试，也不靠换 Agent 清零。

## 出口

给实际文件改动、runner 证据、版本和未验证项。进入 verification 做交付核对，不自批独立验收。物理外部环境缺失只申请 H，本地测试失败不能伪装成 H。

例：真机缺失时可保留获授权的 feature 分支代码和未验证标记，先申请挂起；不能报告功能验收完成。
