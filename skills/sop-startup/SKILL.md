---
name: sop-startup
description: "Use when the user adopts SOP in a new or existing project, prepares project conventions, or migrates an earlier SOP installation. Installing the plugin alone is not project adoption."
---

# 项目启动

## 读取

按本技能目录读取 [共同约束](../sop/references/common.md) 和 [启动要求](../sop/references/startup.md)。本插件资源与目标项目是两个位置；遵守目标项目已有规约，不往插件目录写项目文件。

## 操作

1. 确认目标项目、采用意愿与本次授权。只安装/了解插件时报告能力和下一步，不初始化业务项目。
2. 检查已有规约、架构/契约入口、代码规范、错误处理、禁止清单、术语、检查入口及在制品，保留用户改动。
3. 从旧版升级、发现旧入口或新旧混合时，在写任何启动产物之前读取 [旧项目识别与授权迁移](../sop/references/migration.md)，执行只读识别、差异预览、授权切换及验收。无法确认来源或仅有安装授权时不改业务文件。处理中断/重跑时重新比较当前基线和有效授权，保留定制与历史；旧活动 Skill 和规则引用均核验，不把新技能安装成功当作升级完成。迁移授权不自动包含后续启动补齐，未授权项只列缺项。
4. 在相应文档授权内用 [启动记录](../sop/assets/startup.md) 记录人确认的交互模式、项目负责人、记录位置与缺项；模式读不到写未验证，声明不能改变客户端设置。
5. 在文档授权内补齐项目规约的六类职责；已有 AGENTS/CLAUDE/其他入口按项目约定合并，不复制工具包维护者的 AGENTS，不删除原约定。遇到实质冲突只停受影响部分。
6. 检查入口缺失时提出适用方案；新增/运行脚本、安装依赖、清理旧文件均需对应授权。不能放空 check.sh 冒充门禁。

## 出口

区分插件安装、项目采用、启动产物齐备和实测效果。启动未齐报缺项与允许下一步；齐备后进入 requirements，不把采用 SOP 当作实现许可。

例：用户说“把这个插件装好”不创建需求/计划，也不清理项目缓存；用户明确采用后才准备启动记录和项目规约。
