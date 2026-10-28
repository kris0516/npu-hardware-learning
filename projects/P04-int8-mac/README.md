# P04 · NPU 最小计算核：signed INT8 MAC

**计划：**14 天；**先修：**P03 的 RTL/测试时序、Python 基础。**硬件：**先纯仿真。

## 目标与数值契约

构造 Multiply-Accumulate（MAC）：
```text
acc_next = acc + int8(a) * int8(b)
```
约定输入 a,b 为带符号 8-bit（范围 -128..127），完整乘积需至少 16-bit 有符号承载，累加器采用 32-bit 有符号；复位、enable、latency、overflow 行为必须在实现前明确。**32-bit 不是无限精度**，累加过多仍会溢出，课程最低版可采用明确约定的二补码 wrap。

## 14 天步骤

| ID | 日 | 学员任务 | 新知识 | 验收 |
|---|---|---|---|---|
| P04-S01 | D1–2 | 写 INT8 正负数乘法手算与边界 | 二补码、符号扩展、bitwidth | -128、-1、0、127 案例 |
| P04-S02 | D3–4 | 纯组合 signed multiplier | signed cast、16-bit product | 对照 Python 结果 |
| P04-S03 | D5–6 | 加 32-bit accumulator、reset、enable | 寄存器更新、累计误差 | 连续多周期测试 |
| P04-S04 | D7–9 | 自己设计 ready/valid 或简化有效契约 | cycle timing、latency、throughput | 时序图与断言 |
| P04-S05 | D10–12 | Python Golden Model + 随机/边界回归 | directed/random test、oracle | 多序列无 mismatch |
| P04-S06 | D13–14 | 解释溢出、参数和面积/时序权衡 | DSP vs LUT（概念） | 报告 + 独立解答 |

## MVD 交付

- `rtl/P04/mac_int8.sv`（建议命名，实际由学生亲写），`tests/P04/` Python model 与 self-checking TB。
- 测试覆盖 signed extrema、负数乘积、连续加法、reset 后重新执行、enable=0 保持、长序列与溢出约定。
- 清晰记录 `valid`、累加器状态何时更新；从测试波形能读出准确 cycle。
- 学员能回答“8×8 为何不能把结果存在 8-bit？每次乘法和每次累加需要哪些位宽？”
- 至少一个有参考答案的随机样本集，按真实运行数量记录，不预填 PASS。

## 可选

流水线 MAC、饱和算术、可配置位宽、多通道 MAC。未实现不影响最低目标。

## 向 P05 交接

必须提交 MAC 的接口、符号/截断策略、latency、reset/enable 规则；这些是阵列互联的接口契约。
