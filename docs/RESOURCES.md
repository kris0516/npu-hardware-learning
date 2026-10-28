# 六模块学习资源（优先中文书 + 免费课程）

按**用到再读**组织，不要求先读完教材；出版信息/在线链接可能变化，正式使用前以学校图书馆/出版社为准。

| 模块 | 主资源 | 中文书 | 实验映射 |
|---|---|---|---|
| 数字逻辑 | [Nand2Tetris](https://www.nand2tetris.org/) | 《计算机系统要素》；《数字设计和计算机体系结构 RISC-V 版》（Harris） | P01 |
| 计算机体系结构 | [ETH Onur Mutlu 课程资源](https://safari.ethz.ch/architecture/)；[Berkeley CS61C](https://cs61c.org/) | 《计算机组成与设计：硬件/软件接口》（Patterson & Hennessy） | P03–P07 |
| 并行计算 | [Stanford CS149](https://cs149.stanford.edu/) | 《大规模并行处理器编程实战》（版本需核对） | P05–P07 |
| 数字 VLSI | [Berkeley EECS151](https://eecs151.org/)；[OpenROAD](https://theopenroadproject.org/) | 《CMOS 超大规模集成电路设计》（Weste & Harris） | P08 |
| HDL/RTL | [HDLBits](https://hdlbits.01xz.net/wiki/Main_Page) | 《Verilog HDL 数字设计与综合》（版本需核对） | P03–P06 |
| AI Accelerator | [MIT 6.5930](https://sze.eecs.mit.edu/); [Berkeley Gemmini](https://github.com/ucb-bar/gemmini); [SCALE-Sim](https://github.com/scalesim-project/scale-sim-v2) | 先读中文版《计算机体系结构：量化研究方法》第 7 章，再配原版论文 | P04–P08 |

## 各阶段阅读原则

- P01：二进制、真值表、布尔逻辑、半/全加器即可。
- P02：电压、电流、数字接口、KiCad 基础；严禁直接接入市电。
- P03：组合/时序逻辑、阻塞与非阻塞赋值、状态机、仿真与综合区别。
- P04：补码、定点乘加、数值溢出和测试覆盖。
- P05：矩阵乘法映射、PE 数据重用、阵列 warm-up/drain。
- P06：FPGA LUT/DSP/BRAM、约束与 STA。
- P07：量化推理、激活函数、Host/Accelerator 数据传输。
- P08：CMOS/标准单元、PPA、布局布线、DRC/LVS；不要把流片当成必要课程成果。

所列公开课的**公开视频、作业和访问权限**可能不一致；教师应优先选无账号限制的可用资源，不要假称所有大学课程均开放完整视频/作业。
