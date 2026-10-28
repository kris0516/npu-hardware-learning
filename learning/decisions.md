# 课程与工程决策日志

## 2026-10-28 · 首次课程部署

- 采用 **8 项、每项 14 天目标**；P01–P07 为主线，P08 ASIC RTL-to-GDSII 是选修。
- **统一旧编号**：初始 README 曾为 P01 Logic、P02 时序、P03 MCU、P04 PCB、P05 FPGA、P06 MAC、P07 NPU、P08 ASIC。新版本改为 P01 Logic、P02 MCU+PCB、P03 RTL Datapath、P04 MAC、P05 Array、P06 FPGA、P07 Tiny MLP、P08 ASIC。后续会话只按新编号，不得混用旧项目号。
- 新聊天每个项目单独开；GitHub state、handoff、项目 README 是上下文。
- 教师小步教学、学生完成核心电路、Codex 辅助自动化，CI 与学习验收分开。
- P06 的 UKM DE1-SoC 使用权限、环境、工具版本均待实际确认；不可提前算成功上板。
- P07 14 天内的最小可行目标限定为 tiny quantized MLP，不保证一次做到完整 digits CNN/NPU 产品。
- P08 不默认真实流片，不产生虚假的 GDSII 实硅测试结论。
- 初始化 `rtl/and_gate.v` 与测试仅用于仓库测试流水线，不代表任何学生知识点已通过。
