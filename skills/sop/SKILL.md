---
name: sop
description: "Use when starting or resuming an AI-assisted development task, deciding which SOP stage applies, or checking whether prerequisites permit implementation. Also use when the user explicitly asks to follow SOP; consultation and repository exploration stay read-only."
---

# SOP 入口

本技能选择阶段，不替人批准需求、档位、挂起或验收。先遵守目标项目规约；安装插件不代表目标项目已采用全套 SOP，也不授权写文件、清理、提交或部署。

## 路径与读取

- 本技能的目录为资源基准：`references/` 与 `assets/` 相对本文件，不相对使用者工作目录。
- 下表中的其他技能是 `../<技能名>/SKILL.md`。优先用宿主原生 Skill 调用实际已发现的名字（插件可能加命名空间）；无原生调用就读取该文件，不编造命令。
- 项目任务、规约、代码、测试和记录始终属于目标项目，不能写入插件安装目录。沿用项目已有记录位置，插件更新不改项目记录。

## 首次使用与路由

1. 读取 [共同约束](references/common.md)，恢复用户目标、已有规约和真实授权。缺文件或冲突明确报告。
2. 首输出包含模式自检、路由判定、缺失项、下一步；模式无法读取时写“未验证”，不声称改变了工具配置。若首次发言时尚未加载本技能，加载后立即补报，不倒称已遵守首输出义务。
3. 只做咨询/项目了解时保持相应只读范围，不因缺开发产物强迫用户先写需求。
4. 业务开发且尚未采用 SOP 时，说明要求并由人确认采用；按 startup 准备项目规约。不能因全局安装本插件就在所有仓库创建文件。
5. 已采用时按下表加载一个当前阶段；仅在需要转换阶段时加载下一个。不要一次读取全部阶段资源。

| 当前情况 | 加载技能 | 允许动作 / 停止位置 |
| --- | --- | --- |
| 新项目采用 SOP / 老项目切换流程 | `../sop-startup/SKILL.md` | 盘点并在授权内准备规约 |
| 一句话诉求、语义歧义、需求/调研不足 | `../sop-requirements/SKILL.md` | 澄清和调研；不开始实现 |
| DoR 已满足，缺冻结设计 | `../sop-design/SKILL.md` | 设计、决策和派发准备 |
| 需求/设计/派发齐备，人已确认档位与范围 | `../sop-execution/SKILL.md` | 在授权范围实现与短回路测试 |
| 需要检查证据、交叉评审或准备交付 | `../sop-verification/SKILL.md` | 执行验证，不自批最终验收 |
| 外部条件缺失、失败升级、HOLD / 周快照 / 换会话 | `../sop-recovery/SKILL.md` | 归因、申请/回收挂起、恢复基线 |

派发信息不齐时列缺失项，可在授权内协助起草，不将 AI 草案当确认。已有明确授权不重复索取；关键歧义或范围/风险变化才等待新的裁决。

## 结果与边界

分别报告：文件齐备、结构核对、真实人工批准、runner 结果、独立评审与最终验收。不把一个状态代替另一个。

阶段规则和模板在本目录 `references/`、`assets/` 单独维护，并随技能打包。执行限制及采用时需确认的事项见 [适配边界](references/boundaries.md)。

例：用户说“先摸清项目”只读探索；“做个笔记工具”先问场景和边界；完整已授权任务则恢复派发基线后执行，不重复询问同一授权。
