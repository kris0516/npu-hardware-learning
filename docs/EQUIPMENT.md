# UKM 实验室资源、预算与证据边界

**原则：**常规仪器仅在校内实验室使用，不借走；学生现有 Mac 不计入项目采购。设备是否免费、可预约、处于可用状态仍需按 UKM 规定确认。

## 可能的学校资源（不等于借用许可）

| UKM 单位 | 已公开列出的相关设施（后续预约时复核） | 项目用途 |
|---|---|---|
| FKAB / JKEES Student Project Laboratory | 示波器、万用表、函数发生器、电源、焊接/逻辑实验等 | P02，调试电路/电源 |
| FKAB / JKEES Microwave Laboratory | LPKF S63 PCB 刻板机及 CircuitPro（是否可操作需确认） | P02 PCB 原型 |
| IMEN / MINES Lab | Terasic DE1-SoC（Cyclone V）及电子测试设备 | P06、P07 FPGA |
| FTSM | 导师、计算机实验室与软件工程资源 | 跨院协调、算法与数据验证 |

参考公开入口：
- https://www.ukm.my/jkees/student-project-laboratory/
- https://www.ukm.my/jkees/microwave-laboratory/
- https://www.ukm.my/imen/mines-lab/
- https://www.ukm.my/imen/ijana/

**联系人、校内收费及开放时间可能更新，应由学校当前正式通知确认。** 不将实验室板卡列出视作可以预约到特定日期。

## 条件性预算（RM，初步教学计划而非学校报价）

- P01：0。
- P02：约 50–200（ESP32、跳线、电阻、电容、基础 PCB 耗材；若学校提供可更低）。
- P03–P05：0–50（有 Mac 且仅做开源软件仿真）。
- P06：0–50（假定学校 FPGA 与相关工具免费现场使用；若无权限需重新评估）。
- P07：0–150（假定复用 P06 板卡；可为线材/额外调试耗材预留）。
- P08：0–200（开源 EDA，不含流片；软件许可证/算力视条件调整）。

这些是**可叠加但有复用关系的零件/耗材预算**，不是权威学校收费表或 NPU 产品成本。

## 硬件安全与数据

- P02 使用 USB/安全低压、明确 3.3V/5V 兼容，按设备手册与实验室规定操作；严禁实验中直连市电。
- 进 FPGA 时先确认供电、引脚约束、电平与 IO 配置；不要盲接 5V 外设。
- 记录板卡型号、bitstream/RTL commit、工具版本、时钟、约束、测试条件。
- ASIC P08 默认不流片；MPW/PDK/封装和测试需要导师、许可证与经费。
