---
name: sop-verification
description: "Use when checking an implementation against acceptance evidence, running project validation, preparing independent review or delivery, or deciding whether a completion claim is justified."
---

# 验证与交付

读取 [共同约束](../sop/references/common.md) 和 [门禁与测试证据](../sop/references/gates.md)；有未恢复外部项时再读 [挂起规则](../sop/references/recovery.md)。

## 操作

1. 获取实际代码/产物版本、人确认的验收、档位引用和当前 diff；不能只看实现者的总结。
2. 核对每条 oracle 能否不看实现独立写出。预期同源、弱断言或外部真值缺失时明确指出，不用覆盖率/两个 AI 一致替代正确性。
3. 使用真实项目 runner/实测入口，记录命令、退出结果及覆盖范围；没有执行写未验证，失败写失败。引用旧证据须确认版本仍适用，代码改变后重验。
4. 核对档内最小集、关键分支、日志、回归、文档更新依据、新增路径/白名单/依赖锁扫描。缺检查器不视为已通过。
5. 按 [交付报告](../sop/assets/delivery.md) 逐条列证据，区别自测、独立交叉验收和需求方验收。作为独立评审者须与实现会话分开，读取真实基线；不冒称自己是人类需求方。
6. 功能全部 HOLD 回收前仅部分交付，不进入需求方验收；不能把 Known Issues 当作本地失败、安全或数据损坏的豁免。
7. 给文件理由、未验证项、文档同步依据和符合项目规范的提交草案；未经授权不提交、推送或发布。

## 出口

报告文件齐备、结构核对、runner、独立评审、最终验收各自状态。向需求方提交材料不等于已获验收，插件测试通过也不等于业务项目通过。

例：只有静态链接检查时写“静态检查通过、客户端行为未验证”；两个模型都同意不能代替真实 runner 或业务 oracle。
