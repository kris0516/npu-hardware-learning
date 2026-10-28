# P03 · 可综合 RTL：8-bit ALU、寄存器与 FSM

**计划：**14 天；**环境：**Mac + Icarus Verilog/Verilator + GTKWave（实测安装状态），不需要 FPGA。**先修：**P01 的加法器、P02 的输入输出理解。

## 目标

学会“描述会同时存在的电路”，不是把 Verilog 当依次执行的 Python。设计一个 8-bit ALU（加/减/AND/OR/XOR）、一个带时钟寄存器和一个简单控制 FSM，形成可仿真的 Datapath + Control。

## 小步安排

| ID | 日程 | 学生独立实现 | 只补必要理论 | 验收 |
|---|---|---|---|---|
| P03-S01 | D1–2 | 阅读简单 AND RTL，预测波形，搭建本地仿真 | module / ports / assign / testbench | 预测与实测对应 |
| P03-S02 | D3–4 | ALU 组合逻辑：ADD、SUB、AND/OR/XOR | select、signed/unsigned 的区别 | opcode 真值表/自检 |
| P03-S03 | D5–6 | 8-bit 结果寄存器和 reset | always_ff / nonblocking / clock edge | 复位、保持、更新波形 |
| P03-S04 | D7–9 | 简单 FSM 控制 load/execute/done | states、Moore/Mealy、合法状态 | 周期表、reset/非法输入 |
| P03-S05 | D10–12 | Python golden vs RTL Testbench，lint/基础综合检查 | self-checking TB、latency | 正常/边界随机样本 |
| P03-S06 | D13–14 | 独立解释组合/时序划分、提交报告 | latch、setup/hold 初识 | 设计讲解、验证结果 |

## MVD 设计契约

- 明确 ALU 的运算集、8-bit 结果是否 wrap、加减法进位/溢出旗标的含义；至少验证正反例。
- 有 clock/reset 的状态或结果寄存器，测试 reset 和 enable；非法 opcode/状态须有定义好的输出或可识别错误。
- 无意外 latch、无多驱动/未声明 net；Testbench 不只 `$display`，必须主动比较预期与实际并失败退出。
- 文件建议放在 `rtl/P03/`、`tests/P03/`，保存编译/运行命令、关键波形和独立解释。

## 高价值直觉问题

- 为什么 `always_comb` 代表组合电路，而 `always_ff` 是边沿更新？
- 同一时钟沿触发的两个寄存器相互赋值时，非阻塞赋值意味着什么？
- 为什么“仿真正确”不证明已满足目标 FPGA 的时钟频率？

**不要让 Codex 在第一次作业前写完 ALU+FSM。** 可以先让它检查工具、设计不暴露答案的 Testbench，或审阅学生已有代码。

## 进阶

实现可参数化位宽或五级流水线示例。P04 将直接重用 clock/reset/enable 的时序经验。
