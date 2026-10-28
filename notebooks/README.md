# Notebooks 的 Mother / Work 规则

- 教师创建正式母版到 `notebooks/masters/Pxx_Syy_topic.ipynb`（尚未发布时不要假设存在）。
- 学员先 `git pull` 获取真实母版，再复制到本地 `notebooks/work/Pxx_Syy_topic_work.ipynb` 运行、修改和回答问题。
- `notebooks/work/` 本地工作文件默认不纳入 Git。最终具有复现价值的数据和图表，经过检查后归档到 `projects/Pxx-*/evidence/` 或正式实验记录。
- 不强制所有硬件练习都用 Notebook；Verilog 测试、KiCad 工程优先保持原生文件。
- Notebook 不预先给出全部核心练习答案；可给必要的 Python Golden Model 验证接口和提示。
