# P07 · Tiny Quantized MLP 推理：软硬协同

**计划：**14 天目标；**前置：**P04–P06 或等价可验证 FPGA 接口；**任务：**将一个真正训练/定义并量化的极小神经网络输入/权重映射到自己设计的 MAC/阵列，取得端到端输出。

## 范围：两周 MVD vs 进阶

**最低 MVD：**建议 16→8→4 的两层小型 MLP，输入为 4×4 简单图案/合成数据，能够输出 4 类分类结果；软件提供浮点/量化参考，硬件至少完成真实的量化矩阵乘加，Host 执行与硬件结果可逐层比对。若 P06 实板因资源受阻，只能标记 `simulation-only/blocked`，不能认为完成“FPGA on-board inference”。

**进阶（不是 14 天硬要求）：**64→16→10 的 8×8 手写数字分类，具有真实数据集评估、缓冲/带宽优化、完整 CPU–FPGA 端到端 benchmark。

## 两周计划

| ID | 日 | 学员任务 | 理论补充 | 验收 |
|---|---|---|---|---|
| P07-S01 | D1–2 | 选网络形状和数据，先做软件浮点基线 | linear layer, ReLU, shape | 软件输入/输出与评估 |
| P07-S02 | D3–4 | 定义 INT8 量化规则和整数推理参考 | scale, zero-point, rounding, clamping | 量化误差/边界检查 |
| P07-S03 | D5–6 | 将权重/激活分块映射到 P05 阵列 | tiling、SRAM/Buffer、data movement | memory layout 说明 |
| P07-S04 | D7–9 | 做 host→accelerator→host 通信与执行控制 | latency、bandwidth、protocol | 一次端到端推理 trace |
| P07-S05 | D10–12 | 多样本比对、测端到端耗时与错误率 | numeric equivalence、benchmark | 公平 CPU vs FPGA 对照 |
| P07-S06 | D13–14 | 复现实验，展示分类 demo 和瓶颈分析 | utilization、throughput、I/O overhead | 报告与问答 |

## 完整验收

- 清楚记录：权重/激活维度、位宽、偏置与 ReLU 在何处实现、缩放/舍入规则、饱和或 wrap 规则；逐层数值误差要解释，不能只报 final class。
- 至少一个批次输入能够从 Host 发送并经过硬件运算取得结果；有独立 Python 整数量化 Golden Model，比对 INT8/INT32 中间结果。
- 同一批输入、同一数值语义下报告准确率/一致率、CPU 参考与 FPGA 端到端 latency（包含传输）。记录时钟、样本规模、测量重复次数和环境；若未测，不给“提升 xx%”。
- 学员解释为什么一个计算核快不一定端到端更快，数据复用和通信瓶颈在哪里。
- 对模型结果与性能实测严格区分 `floating point` / `quantized software` / `RTL simulation` / `FPGA measurement`。

## 失败后如何缩减

不要跳过数值验证来赶进度。可缩小网络到 4→4→2 或固定小权重；仍要完成**输入→计算→输出**真实闭环。未实现真实 FPGA 执行则如实写 `blocked`/in_progress，后续补设备时复验。

## 简历叙事（完成后才可写）

可证明地讲“自己设计了 INT8 NPU 计算阵列并完成可复现量化神经网络推理/性能分析”，不可将课程用阵列直接描述为商业 GPU 级 NPU。
