---
title: "Real Preferences under Arbitrary Norms"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["game_theory_mechanism", "argumentation_reasoning", "unclassified"]
dblp_key: ""
doi: "10.65109/JWXO7778"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JWXO7778.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "strict_complete_preferences", "existence_not_estimation", "high_dimension_possible", "arbitrary_norm_conjecture_open"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Real Preferences under Arbitrary Norms

## 一句话总结

本文把“排名由到 voter 的距离表示”的空间偏好模型从 Euclidean/Manhattan 推至所有 \(p\)-norm：对 \(n\) 个不同偏好类型、\(m\) 个 alternatives 的严格完整偏好 profile，只要 \(d\ge\min\{n,m-1\}\)，就可作 rank-preserving \(\ell_p\) 嵌入；并证明任意 norm 下两个 voter 类型可嵌入 \(\mathbb R^2\)。这是存在性理论，不是从数据学习 embedding 或证明低维现实偏好一定适配。

## 方法与证据

- 设 alternatives \(A\) 与 voters \(V\)，每个 voter 给出严格、完整的 weak order（§1）；rank-preserving embedding 要求 \(a_j\succeq_i a_k\) 当且仅当 \(\lVert v_i-a_j\rVert\le\lVert v_i-a_k\rVert\)（Definition 1）。相同 ranking 的 voters 可共用坐标，所以 \(n\) 是 distinct preference types。它不覆盖 ties、缺失/噪声排序、上下文依赖偏好、策略性报告或 cardinal utility。
- Theorem 1：对所有 \(1\le p\le\infty\)，任意上述 profile 在 \(d\ge\min\{n,m-1\}\) 时可 rank-embed 到 \((\mathbb R^d,\lVert\cdot\rVert_p)\)。论文称证明为 constructive and geometric，并将 \(p\downarrow1\) 的行为用于说明 \(\ell_1\) 需要不同构造；extended abstract 未给完整构造、复杂度、数值稳定性或实现代码，故不能据此宣称可直接计算实用 embedding。
- Theorem 2：仅有两类 voter 时，任意 \(m\) 个 alternatives 的 profile 对 \(\mathbb R^2\) 上任意 norm 都可 rank-embed。证明依赖一个并非完全显式的几何构造；结论是低人数类型的存在性，不能推出两维模型会对真实群体数据拟合良好。
- 与既有 Euclidean/Manhattan 结果相比，本文统一了所有 \(p\)-norm；但对一般 arbitrary norm 的高维结论没有证明。作者明确提出 conjecture：是否任意 norm 也在 \(d\ge\min\{n,m-1\}\) 时可嵌入（§3）。因此“arbitrary norms”应限于双 voter 的 Theorem 2，或 \(p\)-norm 的 Theorem 1。
- 没有实证、simulation、真实选举/推荐数据、baseline fitting comparison、估计误差、runtime 或 user study。作者也指出需要后续 simulations/empirical studies、一般 norm 的理论、bound tightness 和低维 profile 研究；证据只支持所述数学存在性。

## 适用边界与复现

- 可作为社会选择、投票、设施选址或推荐系统中“ordinal data 是否可被某个距离模型一致表示”的建模前置定理；不能替代偏好 elicitation、表示学习、因果验证、策略鲁棒机制设计或对齐评估。实际采用前仍须验证低维/选定 norm 是否适配，而非因高维存在性就默认空间解释成立。
- 复现应取得 full version [45] 的完整证明，明确 \(n\) 是去重后的 preference types、\(m\)、\(d\)、norm 与输入 strict/complete 条件；构造坐标后逐 voter、逐 alternative pair 检查双向距离不等式。还应报告坐标尺度、数值精度、构造时间/内存及当 \(d\) 接近 \(\min\{n,m-1\}\) 时的失败/边界例。
- 应补测真实或合成 ranking 的 ties、partial orders、噪声/缺失反馈、不同 \(p\) 与非 \(p\) norms、低维约束、out-of-sample rankings、拟合误差及与 Euclidean/Manhattan/非空间模型的比较。对 recommender 或 human-feedback 系统，应审计群体覆盖、少数偏好扭曲、策略性排名和由距离代理引发的公平性影响。
- 本文的“faithful”仅指给定 ordinal order 的距离顺序完全对应，不表示距离大小是人的真实 utility，也不保证集体规则的 welfare、distortion、privacy 或公平。用于高影响决策时需保留原始排序、进行 sensitivity analysis，并让领域人员审核 norm、维数与解释是否合理。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的计算社会选择/空间偏好理论 extended abstract。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/JWXO7778.pdf) 核验 Definition 1、Theorem 1 的全部 \(p\)-norm 维数条件、Theorem 2 的 two-voter arbitrary-norm 结论，以及 §3 对一般 norm 高维情形仍为 conjecture 的限制；未将这些存在性结果写成偏好学习、低维经验拟合或一般 arbitrary-norm 定理。
