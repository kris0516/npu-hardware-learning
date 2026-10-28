# P08（选修）· ASIC RTL-to-GDSII / PPA

**计划：**14 天探索性目标；**先修：**P04 的可综合 MAC 和 P06 的综合/时序经验。**不要求真实流片。**

## 项目目标

用开源 ASIC 工具与合法公开 PDK，把一个已经验证的 MAC（或更小电路）走通：RTL → synthesize → floorplan → placement → clock tree（如适用）→ routing → STA/DRC → GDSII。关注功能约束、面积、关键路径与功率估计（若可靠），学会区分工程估算与实际芯片。

## 14 天 Steps

| ID | 日 | 操作 | 新知识 | 验收 |
|---|---|---|---|---|
| P08-S01 | D1–2 | 明确目标工艺/PDK/合法使用条款、选最小模块 | ASIC / FPGA / MPW / PDK | 版本与许可信息 |
| P08-S02 | D3–4 | RTL 重新仿真、给出时钟约束 | standard cell、Liberty、SDC | baseline 对照 |
| P08-S03 | D5–6 | 逻辑综合、记录面积/门数 | synthesis、area mapping | synthesis report |
| P08-S04 | D7–9 | Floorplan/Placement/CTS/Routing | congestion、timing、clock tree | 实际运行日志与布局视图 |
| P08-S05 | D10–12 | DRC/STA、关键路径分析与小幅优化 | setup/hold, parasitics, PPA | DRC/STA/report 比较 |
| P08-S06 | D13–14 | 解释 GDSII 的意义和制造缺口 | tapeout、wafer、packaging、test | 报告、独立问答 |

## MVD 验收与严谨边界

- 公开 PDK、工具、版本、约束可复现（不提交任何受限 PDK/许可证）。
- 同一个 RTL 输入通过了可核验的综合、物理实现与适用的 DRC/STA 检查，记录完整日志与 GDSII 文件生成结果；若工具不支持某项检查，必须如实标记缺失。
- 报告综合/布局布线面积、Fmax 或关键路径、功耗估算及其方法；没有 signoff 工具时称为研究/教学估计。
- 学员能解释为什么“文件能生成 GDSII”不等于“已经流片”、为什么 ASIC 功耗不能直接套用 FPGA 数据。
- **没有 MPW 订单与真实测量就不写 fabricated/taped-out/silicon-tested。**

## 扩展研究路线

如果用户以后争取 UKM 导师和经费，可单独规划 MPW 工艺、版图审查、外部封装、PCB 测试平台与风险；这些不属于本项目的 14 天最低验收。
