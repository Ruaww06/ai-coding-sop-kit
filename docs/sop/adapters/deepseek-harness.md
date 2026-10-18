# DeepSeek Harness 接入

针对官方 `deepseek-ai/deepseek-harness`，不是只在其他客户端替换模型。

## 一句话交给 Agent

在 Harness 选中你的业务项目，然后发送：

```text
请获取并遵循 https://raw.githubusercontent.com/Ruaww06/ai-coding-sop-kit/refs/heads/docs/sop-v2/INSTALL.md，识别当前 Agent 的接入方式，将 AI Coding SOP Kit 安装到当前项目；遇到冲突先询问，已有旧版先预览迁移差异，不擅自改写项目规约。
```

这是与其他 Agent 共用的一句话入口；Agent 识别 Harness 后使用对应分支。操作、冲突处理及校验要求见 [安装指南](../../../INSTALL.md)。你不需要手工寻找目录或搬文件。

## 发现与加载

官方文件系统技能提供方支持项目级 `<projectRoot>/.dsh/skills/`。七个技能目录直接位于该目录下，共享资源保留在 `sop/references/` 与 `sop/assets/`。projectRoot 为最近含 `.git` 的祖先目录，没有 Git 根时用会话 cwd；与选中项目范围不一致时先确认，不擅自安装到父目录。

在启用相应技能组件的 profile 中，模型可通过 `skill` 工具加载名称 `sop`。这是模型工具调用，不是 shell 命令；不套用 Claude 命名空间，也不假定 `/sop` 等 UI 快捷语法。文件安装后可能需要新会话才能发现技能。

安装仅提供技能，不表示采用完整 SOP 或批准写业务代码。指南先只读识别旧项目入口；旧版迁移先预览差异，经明确授权才修改项目规约、停用旧活动入口，保留定制与历史。仅安装不改项目规约，不移植 Claude hook，不修改全局配置，不保证压缩后自动恢复。迁移与中断恢复的真实 Agent 行为尚待实测。

## 验证状态

已核对官方技能提供方文档与项目目录约定。已在 DSH 桌面版的隔离会话中观察两次安装：Agent 正确选择 `.dsh/skills/`，把其他宿主的同源副本只作报告、不改动，规则指向其他宿主路径时按漂移停下等待授权。另在 fixture 目录内启动一次 headless CLI 会话，会话记录显示 `skill` 工具加载 `sop`，宿主返回的基目录为该项目的 `.dsh/skills/sop`；同目录的 `.claude/skills/` 副本未被使用，运行后文件未变。原生加载只有这一次观察，未完成业务行为验收；实际能力取决于所用版本/profile，应分别核对文件完整性、技能发现、资源读取和行为，不能只凭模型说“已安装”判断成功。详见[测试说明](../../testing.md)。

官方依据（核对版本）：

- [Skills 子系统](https://github.com/deepseek-ai/deepseek-harness/blob/86a402200d95fecef4529d969836f1fe13c6cb0d/docs/subsystems/skills.zh.md)
- [技能目录配置](https://github.com/deepseek-ai/deepseek-harness/blob/86a402200d95fecef4529d969836f1fe13c6cb0d/docs/config-catalog.md)

其他加载方式和兼容范围见 [安装说明](../../installation.md)。
