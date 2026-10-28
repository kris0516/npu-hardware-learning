# P05 · 从 MAC 到 Systolic Array

**计划：**14 天；**先修：**P04 signed MAC 与周期理解，基础矩阵乘法。

## 项目挑战

针对 `C=A×B` 的 2×2 INT8 有符号矩阵，搭建 2×2 Processing Element (PE) 阵列。每个 PE 在不同周期收到沿行/列传播的操作数，执行累加；要有输入排程、有效周期、输出收集和数值正确性。不要仅把 4 个 `*` 运算写在一个 always 块就称为 systolic array。

## 两周 Steps

| ID | 日 | 核心任务 | 新知识 | 验证 |
|---|---|---|---|---|
| P05-S01 | D1–2 | 手算 2×2 矩阵乘法，列出 K 维求和 | dimensions、multiply accumulate | Python NumPy reference |
| P05-S02 | D3–4 | 确定 PE 接口及元素传播方向 | dataflow、PE、output stationary | 手绘 cycle table |
| P05-S03 | D5–6 | 用 P04 MAC 组合 2×2 PE，处理 valid | intra-array connections、skew | 一组样本 cycle trace |
| P05-S04 | D7–9 | 添加输入加载/清零/收集输出控制 | warm-up/drain、控制 FSM | 各输出只计算 K 次 |
| P05-S05 | D10–12 | 随机矩阵和负数的 RTL vs NumPy 测试 | scoreboard、array utilization | 所有输出逐元素比对 |
| P05-S06 | D13–14 | 绘制架构、解释带宽/数据复用，写报告 | arithmetic intensity、memory | 独立追踪一个数据元素 |

## 最小正确性标准

- C 的 shape、输入元素 INT8、acc INT32；对随机正负矩阵得到与 reference 一致的结果（若有 wrap 必须模型同语义）。
- 必须给出真实 PE 连接与周期表：第 0/1/...周期每个 PE 接到哪些 A/B、何时 valid、何时输出；不能把波形截图当作解释的替代品。
- 指定输入开始/输出完成信号，重置后再次运算无旧值残留。
- 报告：运算个数、计算周期、warm-up/drain、理论与观测 throughput 及测试条件，不能虚构加速倍数。
- 4×4 参数化阵列为进阶（时间允许再做）；P06 上板可以先使用已证明正确的 2×2 版本。

## 误区与思考

- 4 个 PE 不自动实现 4 倍加速；数据到达、加载与排空会影响吞吐。
- Output-stationary 与 weight-stationary 如何改变移动的数据？只要求解释本项目使用的具体一种策略。
- 先让学生推导排程，Codex 可检查 Python cycle trace 或帮助整理波形，不应代写尚未掌握的核心数据通路。

## 交接到 P06

提交 `rtl/P05/`、`tests/P05/`、时钟/复位/valid 接口、时序与资源假设、可重复仿真命令。
