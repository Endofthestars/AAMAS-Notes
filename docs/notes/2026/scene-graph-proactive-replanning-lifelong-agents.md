---
title: "Towards Failure-Resilient Lifelong Learning Agents through Scene Graph-Guided Proactive Replanning"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "robotics_embodied"]
dblp_key: ""
doi: ""
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JJIZ3568.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["scene_graph_perception_dependency", "threshold_and_buffer_update_sensitivity", "sim_to_real_and_task_scope", "lifelong_learning_no_formal_guarantee", "official_pdf_doi_discrepancy"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Towards Failure-Resilient Lifelong Learning Agents through Scene Graph-Guided Proactive Replanning

## 一句话总结

该文让机器人在每个高层子任务之前，把 RGB-D 观测得到的场景图与成功示范的前置条件图 buffer 比较；相似度不足时才调用 LLM 验证、解释并重规划。它在 RoboFail/AI2-THOR 与有限实体机器人设置中优于所选基线，但“lifelong”主要是未遗忘保证的参考图累积，结果高度依赖场景图质量、阈值和被验证 buffer 的更新策略。

## 方法与证据

- 对当前子任务构建任务相关 3D scene graph，节点包含物体及状态、边包含空间关系；以 CLIP/语义分割特征的节点相似度、边匹配和度数结构相似度三项均值为图分数。当前图对所有参考前置条件图均低于阈值时，系统预先判为可能失败（§3、式 1–3）。
- buffer 初始为空；没有近邻参考时，GPT-4o 根据当前/期望图的文字描述、任务目标和子任务验证是否仍可执行。验证为可行的场景加入 buffer；不可行时，LLM 给出不匹配原因及约束，再由 replanning 模块根据机器人状态、可用动作和可见物体生成修正动作序列（§3）。
- 表 1 在 RoboFail Preemptive、RoboFail Post-action、加权 RoboFail 与 150 个手工厨房失败案例上报告：作者方法成功率分别为 73.53%、71.87%、71.99%、78.67%，执行时间 104.82、128.66、111.10、142.85 秒；对应 REFLECT-online 为 69.11%、65.14%、67.83%、66.67%，但这些是作者自己的同一评测设置，并非独立复现（§4、表 1）。
- 消融中完整图匹配的 failure detection rate 为 94.01%；去掉 subtask node、结构、节点、边匹配后分别为 84.33%、82.67%、74.67%、70.33%。去掉 reasoning 的 task success rate 从 75.67% 降至 37.67%（表 3）。
- 真实 RoboFail-Real 部分是 UR5e 收集的 30 个失败案例，比较 GPT-4o/Gemini 2.0 Flash 的图文字输入与图像输入；例如 GPT-4o 图输入 FDR 为 0.77（无物体上下文）/0.83（有上下文），图像输入为 0.57/0.80。另在 UR5e 与 Ghost Robotics Vision 60 上展示五个实体任务；这支持有限的实体可行性，不等于大规模长期部署（§4、表 2、图 8）。

## 局限与复现

- 可执行性被“与成功前置条件图相似”这一启发式代理；漏检/误检会随 RGB-D、分割、物体状态、关系抽取、CLIP 表征和 reference coverage 的误差累积。相似不是动作可行的必要或充分条件，LLM 验证也不提供安全或正确性保证。
- 文中在方法处以 `S_j < 0.9` 举例触发重规划，但实验设置称 buffer 方法阈值为 85%，并在图 7 中比较 90/85/80%。应把阈值、相似度归一化、近邻定义、tie/空图行为和每次验证的完整日志公开；否则结果不可直接复现或横比。
- buffer 的“validated”条目由同一感知/LLM 链路产生，错误参考会被持续复用；论文只展示随积累减少 LLM 调用，没有评估错误写入、陈旧环境、分布漂移、容量淘汰、遗忘或长期安全。因此“lifelong learning”应理解为经验缓存扩张，不是有理论保证的持续学习。
- 主基准是 100 个 RoboFail 场景及 150 个手工案例，真实数据只有 30 个 UR5e 失败案例，实体演示为五任务、两种平台。应在未知物体、遮挡/噪声、动力学失败、长程累积误差、未见环境及人类安全约束下进行预注册的独立比较，并报告 LLM 型号、提示词、延迟、成本和随机性。
- 官方 PDF 页脚的引用 DOI 写作 `10.65109/V1X2Y3Z4`，而官方目录标识为 `JJIZ3568`；未能从所核 PDF 建立可靠对应，故元数据 DOI 留空，复现者应以官方目录/PDF URL 而非该 DOI 字符串定位版本。

## 与 AAMAS 的关系与核验说明

该工作属于具视觉感知的机器人代理在子任务执行前进行 failure detection、解释与在线重规划。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JJIZ3568.pdf) 核对框架、buffer、表 1–3、RoboFail-Real 与实体平台范围；未将受控场景中的成功率和 LLM 调用减少外推为通用、无误差的终身学习或机器人安全保证。
