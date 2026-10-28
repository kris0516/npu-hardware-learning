# P06 · 将计算阵列部署到 FPGA

**计划：**14 天；**目标硬件：**UKM IMEN MINES Lab 公示的 Terasic DE1-SoC / Intel Cyclone V（预约/可用性需确认）。**先修：**P05 完成仿真自检。

## 项目目标

学会将已验证 RTL 转为 FPGA 配置：选择时钟和复位、加入 Pin/SDC 约束、Quartus 编译、观察 ALM/DSP/BRAM 使用与 Fmax，最后让真实板卡执行至少一个矩阵案例。**不写“实测成功”直到确认板卡真实运行。**

## 两周 Steps

| ID | 日 | 学员操作 | 新知识 | 证据 |
|---|---|---|---|---|
| P06-S01 | D1–2 | 复核板卡型号/Quartus 版本/电脑、画 IO 图 | FPGA vs ASIC、引脚与电压 | 设备清单/权限 |
| P06-S02 | D3–4 | 建立 project、选择 device 与 top module | synthesis、elaboration | 无错误编译 log |
| P06-S03 | D5–6 | 设置 clock、reset、SDC/pins | timing constraints、clock domain | QSF/SDC 与审查 |
| P06-S04 | D7–9 | 布局布线/时序检查、读资源报告 | ALM、DSP、BRAM、Fmax、timing slack | 报告与工具版本 |
| P06-S05 | D10–12 | 下载 bitstream、执行已知矩阵样本 | on-board verification、IO/host interface | 板卡记录/真实输出 |
| P06-S06 | D13–14 | 对比 RTL/FPGA、解释瓶颈与问题 | simulation ≠ hardware | 报告、独立答辩 |

## 验收分级

- **完整 P06 PASS：**可复现 Quartus project、明确芯片/时钟/IO、带约束的成功编译与时序报告、至少一次实板输入输出正确性，以及学生能够解释时序/资源的主要结论。
- **设备未获准：**仍可完成 Quartus/开源综合（取决于工具/器件支持）和仿真、架构/约束文档，但记录 `blocked` 或部分验收，不可将“未上板”标为完整 PASS。可调换工程任务的实际进行顺序，待设备开放再补证据。
- **重要：**不能把 RTL testbench 的 CPU 运行时间说成 FPGA 推理延迟。

## 进阶

板级 UART 或 ARM HPS 通信、SignalTap、功耗测量；只有具备实际测量条件时才报告板上功耗。

## 交接 P07

报告包括能使用的主机到 FPGA 数据传输方式、最高可稳定运行频率（若经过真实验证）、阵列接口、可用存储容量与协议。P07 依赖这些实际约束选定小网络规模。
