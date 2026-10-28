# RTL 目录

`and_gate.v` 是仓库初始化 smoke test，**并非 P01 学生完成证明**。

从 P03 起按 `rtl/P03/`、`rtl/P04/`、`rtl/P05/`、`rtl/P06/`、`rtl/P07/` 放学生/教师审查后的可综合 Verilog/SystemVerilog。要求：
- 每个模块在文件头说明端口位宽、signedness、clock/reset、enable/valid、latency；
- 关键模块必须有对应 `tests/Pxx/` 中能自动失败的 testbench；
- 不提交 IP/PDK 商业授权文件、难以复现的生成物；
- 学生先自己动手，Codex 可审代码或生成测试，但不得代替核心 RTL 实现。
