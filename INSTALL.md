# 在 DeepSeek Harness 中安装

供 Agent 在用户要求安装时执行。只安装当前项目的技能，不修改全局配置、API Key 或业务规约，不安装 Harness 或其他依赖，不启动额外模型进程。宿主拒绝权限时停止，不绕过。

## 安装

1. **确定项目。** 使用 Harness 已选中的业务 workspace。官方技能提供方以最近包含 `.git` 的祖先目录作为 projectRoot，没有 Git 根时使用会话 cwd。如果与用户选中的范围不同，先确认。目标目录为 `<projectRoot>/.dsh/skills/`，不要默认安装到用户主目录。

2. **获取源码。** 使用 Git 将 `https://github.com/Ruaww06/ai-coding-sop-kit.git` 的 `docs/sop-v2` 分支克隆到本次新建的 staging 目录。沿用项目允许的临时目录；没有约定时可在项目内 `tmp/` 使用唯一名称，不覆盖已有目录或改忽略规则。记录实际 commit SHA；所有安装文件来自同一个 checkout。不执行下载内容中的脚本或测试，不使用 `curl | sh`。Git/网络不可用时报告，不擅自安装软件。

3. **检查技能和冲突。** 确认以下七个目录及各自的 `SKILL.md` 存在：

   ```text
   sop
   sop-startup
   sop-requirements
   sop-design
   sop-execution
   sop-verification
   sop-recovery
   ```

   保留 `sop/references/`、`sop/assets/` 和相邻阶段技能，检查本地资源引用可解析且不逃出整组技能。确认源和目标无符号链接或异常路径。复制前检查全部七个目标；有同名但内容不同、不完整或来源不明的技能时，先列冲突并询问，不部分安装或直接覆盖。其他技能不动。

4. **复制整组。** 只将上述七个目录放到 `.dsh/skills/` 下，不再嵌套工具包目录。将仓库 `LICENSE` 复制到安装副本的 `sop/LICENSE`。不复制仓库 `.git`、维护者 `AGENTS.md`、测试、CI、`.claude-plugin/` 或 `hooks/`。

   已有完整且相同的安装无需重写：逐一比较来源技能文件，同时检查目标是否有额外文件；允许额外存在内容与来源一致的 `sop/LICENSE`，不要把这个许可证副本误判为冲突。其他额外文件或修改先询问。

5. **核验文件。** 对照同一 checkout 比较七个安装目录的文件与内容，包括资源和许可证。入口应为 `.dsh/skills/sop/SKILL.md`，其他阶段与 `sop/` 同层。失败时报告实际已写路径，不假装成功，也不擅自删除或回滚已有文件。

staging 是临时来源，不是运行时依赖。完成后报告其位置和是否残留；清理仅限本次创建目录且已有相应授权，不广泛删除项目临时文件。

## 验证加载

若当前 profile 提供 `skill` 工具，用它加载名称 `sop`，再读取其 `references/common.md`，仅做只读检查，不初始化项目或开始业务开发。没有发现时提示在所选 workspace 新建会话再试；不要猜 `/sop` 等 UI 命令、修改配置或关闭沙箱。

分别报告：

- 安装目录、来源分支和实际 commit。
- 七个技能及资源、许可证是否校验一致。
- 宿主是否实际发现并加载 `sop`；未观察到就写“加载待验证”。
- staging 是否残留及下一步。

文件安装完成不等于宿主已加载，也不等于项目采用完整 SOP。此安装方式依据官方技能提供方文档设计，尚未完成 Harness 端到端实测。

## 更新与移除

由用户另行发起。更新时获取新 checkout，列新旧差异；确认同名目录及本地修改如何处理后再更新完整技能组，不在不明来源上直接 `git pull` 或覆盖。移除前列出七个技能目录及本地修改，取得删除确认；不删除整个 `.dsh/skills/` 或项目记录。

## 其他客户端

这份指南只针对 DeepSeek Harness。Claude Code 使用 [本地插件加载说明](docs/installation.md#claude-code加载-beta)；不要将本指南的目录或其他工具的插件管理命令互相套用。
