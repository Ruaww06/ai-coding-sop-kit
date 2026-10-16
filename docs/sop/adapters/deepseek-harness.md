# DeepSeek Harness 手动接入

本说明针对官方 `deepseek-ai/deepseek-harness`，不是仅在别的客户端替换 DeepSeek 模型。

当前未制作专用 Harness 插件/自动安装器。先核对所用版本/profile 的指令、文件系统及 Skill 提供方，再按 [整组安装说明](../../installation.md) 注册同一 `skills/` 正文。保留所有相邻技能与公共资源，不只复制旧兼容入口。

发现或快捷调用不确定时由用户要求实际读取入口，不猜其他客户端斜杠命令。没有对应的启动注入代码，不能声称已自动加载或压缩后自动恢复。

不改项目规约和全局设置，不因安装批准开发。需实测读取、阶段判断、停手、真实验证与跨会话恢复；当前未实际安装验收。

官方依据：
- https://github.com/deepseek-ai/deepseek-harness
- https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.zh.md
