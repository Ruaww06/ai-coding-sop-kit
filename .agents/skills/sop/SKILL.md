---
name: sop
description: "Use when an older SOP document installation points to this compatibility entry. It redirects to the single canonical skills tree without maintaining a second workflow."
disable-model-invocation: true
---

# 旧入口兼容指引

正式技能已迁入工具包 `skills/`，本文件不再维护工作流。按本文件目录读取 [唯一入口](../../../skills/sop/SKILL.md)，不存在就报告副本不完整，不猜项目根路径。

新安装不要把本兼容入口与原生插件同时注册。不能仅复制本文件：手动安装须复制完整 `skills/` 目录并保留 `sop`、其他阶段技能及公共资源的相邻关系。步骤见 [安装说明](../../../docs/installation.md)。

迁移前保留项目已有需求、计划、真实授权、失败和 HOLD 历史；未经查看及删除授权不移除旧入口。文件路径和调用语法由宿主决定，不保证此兼容文件在所有客户端被自动发现。
