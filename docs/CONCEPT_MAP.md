# 先修知识地图与硬件直觉

| 模块 | 从哪个项目引入 | 必须能解释的概念 | 常见误区 |
|---|---|---|---|
| 数字逻辑 | P01 | binary / carry / NAND / XOR / full adder | 误把二进制“10”当十进制十 |
| 板级电子 | P02 | voltage/current, pull-up, GPIO, common ground, UART | 忽略 3.3V 电平与地线 |
| 数字时序 | P03 | combinational vs sequential, clock edge, register, reset, FSM | 将 Verilog 非阻塞赋值当作 Python 顺序执行 |
| 数值硬件 | P04 | two's complement, signed extension, INT8×INT8, accumulator width, overflow | 忽略中间乘积位宽导致错误 |
| 并行与数据流 | P05 | processing element, weight/output stationary, skewing, tiling | PE 数量等于实际加速倍数 |
| FPGA 工程 | P06 | LUT/ALM/DSP/BRAM, synthesis, Fmax, timing closure, constraints | RTL 仿真通过不等于硬件可上板 |
| AI 推理 | P07 | calibration, quantization, zero-point/scale, memory movement, end-to-end latency | 只测计算核时间不含数据搬运 |
| ASIC 实现 | P08 | standard cells, STA, PPA, DRC/LVS, placement/routing, PDK | GDSII 文件等于制造并实测成功 |

## 必须训练的三个维度

- **静态空间：**位宽、形状、端口、接口、SRAM 容量、数据布局。
- **时间：**时钟域、每周期输入/输出、流水线延迟、ready/valid、背压与数据相关。
- **物理资源：**面积、动态功耗、布线扇出、带宽、延迟/频率以及测量限制。

教师每步只引入直接必要的概念；课外复习以 `learning/knowledge.md` 的证据驱动，不要求先通读整本 VLSI 教材。
