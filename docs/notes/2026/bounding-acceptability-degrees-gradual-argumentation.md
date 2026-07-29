---
title: "Bounding Acceptability Degrees and Eliciting Initial Weights in Gradual Argumentation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["argumentation_reasoning", "human_agent_interaction", "safety_verification"]
dblp_key: ""
doi: "10.65109/NSCC6791"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NSCC6791.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "weighted_h_categoriser_scope", "interval_elicitation_assumptions", "full_algorithm_in_external_version", "no_human_study_reported"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Bounding Acceptability Degrees and Eliciting Initial Weights in Gradual Argumentation

## 一句话总结

本文为渐进加权论证提出区间式 elicitation：让用户报告每个 argument 的“最终 acceptability”区间，而非难以区分的精确 initial weight；再判断区间是否由 \([0,1]\) 初始权重可实现、在不丢失有效解时收缩区间，或以启发式修复完全无解的区间。它是 weighted h-categoriser 语义下的逆问题框架，不等于已验证的人机决策支持系统或通用论证语义工具。

## 方法与证据

- 输入是 interval constrained argumentation framework（ICAF）：标准 argument graph \((A,R)\) 加上每个 argument 的 acceptability interval \(I(a)\subseteq[0,1]\)（§2）。以 weighted h-categoriser 为例，最终 degree 是由攻击者和 initial weights 的 fixed point 得到；初始权重与最终 degree 因图中相互作用不能逐 argument 独立换算。
- 流程是：(1) 用户为每个 argument 报告相信的 final acceptability 区间；(2) 若存在合法 initial weights 使区间中的某个联合 degree 可得，则称 rational，并删除其中不可达部分以作 refinement；(3) 若没有任何联合点可由合法初始权重得到，则视为 irrational 并移动 bounds 修正（§2）。这里的 rationality 是“至少一个联合赋值可实现”，不是每一个区间内组合都可实现。
- 论文区分 fully rational：区间笛卡尔积内每个 degree 组合都有某个初始权重实现。例 1 的二节点攻击 \(a\to b\) 显示：给定 \(I(a)=[0.8,1]\) 时，\(I(b)\) 的上界不超过 \(L=0.5\) 可 fully rational；上界介于 \(L\) 与 \(U=5/9\) 时仅 rational；下界超过 \(U\) 时 irrational。该例说明独立地把 final-degree interval 当作 initial-weight interval 会错。
- \(\epsilon\)-rationality 用于量化离 fully rational 有多远：缩小各 interval 的上端，直到整个 box 可行，得到 \(\epsilon\)-refinement（图 2）。对于 irrational 输入，作者称额外研究了把“最靠近原点”的点移动来修正的 heuristics，但该 3 页文稿未给算法细节、正确性、最优性或运行成本，指向外部 arXiv 版本。
- 文中称提供含 source-code link 的 Web UI，并列出 knowledge engineering/辅助人类推理作为应用，但未报告用户实验、标注协议、任务成功率、可用性、公平性、真实知识库案例、运行时间或与其他 elicitation 方法的定量比较。因而证据支持形式化区间推理/示例，不支持提高人类判断质量的经验结论。

## 适用边界与复现

- 适用于能明确建成 attack graph、采用（或可证明等价于）weighted h-categoriser、且专家愿意给出 \([0,1]\) 最终可接受度范围的知识工程场景。它不直接覆盖 support/bipolar interactions、概率/自然语言不确定性、时变论证、非数值反馈、不同 gradual semantics 或“初始权重就是用户真实信念”的解释。
- 复现需固定 graph、攻击方向、chosen semantics 与 fixed-point 求解精度，收集所有 interval bounds；枚举/优化联合 final degrees，验证是否存在 \([0,1]\) initial weights，并分别报告 rational、fully rational 与 \(\epsilon\)-refinement。应从文中链接 UI/source 和 arXiv full version 恢复 correction heuristic、参数与 tie-breaking，再用例 1 复现 \(L=0.5,U=5/9\) 的三种区域。
- 应测试大型/稠密/循环 graph、不同区间宽度和不一致比例、attacks/support 混合、语义切换、噪声或策略性输入、多个专家的聚合、优化可扩展性与数值误差。需比较“收缩 upper bounds”及“移动接近原点的点”对原始用户意图、可解释性和不同群体的影响，而不能只报告有解率。
- 在法律、医疗、政策或内容治理中，界面给出的修正区间不是事实或价值判断的校准证明：收缩/移动会改变用户表达，且图结构/语义选择本身会塑造结果。应显示原始与修正后的区间、理由和不可达证据，支持撤销/人工复核，并审计敏感 argument、少数意见和操作者偏差。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的渐进论证、偏好/不确定性 elicitation extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/NSCC6791.pdf) 核验 ICAF 定义、rational/fully rational 的区分、二节点示例、\(\epsilon\)-refinement 和外部完整细节的指向；没有把 Web UI 或理论可行性写成已完成的人类实验、通用语义保证或自动决策授权。
