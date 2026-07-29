---
title: "Combinatorial Optimization of Antibody Libraries via Constrained Integer Programming"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["applications", "planning_scheduling", "safety_verification"]
dblp_key: ""
doi: "10.65109/DUGN7746"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DUGN7746.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "computational_biomedical_design", "in_silico_proxy_objectives", "no_wet_lab_validation", "not_clinical_evidence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Combinatorial Optimization of Antibody Libraries via Constrained Integer Programming

## 一句话总结

ProtLib-Designer（PLD）把 cold-start antibody library design 表为 constrained ILP：以 ProtBERT 的 sequence score 和 AntiFold 的 antigen-conditioned inverse-folding score 的逐位点加性变化为目标，并通过 solve-and-remove、Hamming exclusion 及 position/substitution frequency caps 生成固定大小且可控多样性的 mutant library。三组 antibody–antigen 系统显示更好的模型/“oracle” proxy 指标；它生成的是体外筛选候选库，不是已证实的结合、特异性、可制造性、疗效或临床安全性。

## 方法与证据

- 输入 wild-type antibody \(w\) 和 mutable interface positions \(r\)，目标是构造 \(K\) 个 mutants，在无 target-specific experimental fitness data 的 cold start 下提升预测目标并控制 diversity（§1）。“cold start”并不消除对结构/模型训练分布的依赖，也不解决 target-specific epistasis、表达、稳定性、免疫原性或实验测量误差。
- 每个 substitution 的 PLM intrinsic score 与 AntiFold（含 antigen context）extrinsic score 是相对 wild type 的 log-probability change（Eq. 1），并假定可跨 position 相加。binary variables \(z_{ij}\) 在 scalarized weighted ILP 中选择 mutation，CBC 求解（Eq. 2，§2）。加性模型不能表达高阶 mutation interactions；分数不是 binding affinity、activity 或 developability 的直接观测。
- 每次按 Dirichlet 采 \(\lambda^{(k)}\) 解 ILP，随后排除既选 mutant 的 Hamming ball、限制 mutation position 次数 \(\delta_1\) 和具体 substitution 次数 \(\delta_2\)（Eq. 3）。当 \(\epsilon=0\) 保证 K 个 unique mutants，但 uniqueness/diversity 不保证覆盖真实 fitness landscape 或筛选命中率；\(\delta\) 与 objective weights 是人为风险/覆盖选择。
- 实验为 Trastuzumab/HER2（10 positions）、D44.1/HEL（34）、Spesolimab/IL36R（47），每系统 K=1000、5–8 mutations；比较 LMG、MODIFY、SPEA2，以 entropy、BEU、HV和 Trastuzumab 的 oracle fitness proxy 评估（§3）。没有 wet-lab synthesis/binding/functional assays、independent prospective validation 或患者数据。
- Table 1（Trastuzumab）PLD(div.) entropy 3.22、BEU 4.62、HV 2232、oracle 58.2%，PLD(no div.) 61.8%；LMG/MODIFY oracle 为 17.1/18.6%。较大系统报告 D44.1 BEU 1.84 vs LMG 10.81、Spesolimab −7.28 vs 4.50。作者明确承认依赖 structural context 与 learned-score fidelity，未来才考虑 richer quadratic interactions（§4）。

## 适用边界与复现

- 适合 early-stage computational candidate-library prioritization，不能用于诊断、治疗、患者选择、给药或声称某序列为有效/安全抗体。任何候选必须经过合法的实验设计、表达/纯化、结合/功能/特异性、毒理/免疫原性和监管要求的逐级验证。
- 复现需给三系统的 structures/chain/interface positions、wild types、ProtBERT/AntiFold versions/checkpoints/inputs、score sign/normalization、ILP objective/weights、\(K,\epsilon,\delta_1,\delta_2\)、Dirichlet seeds/CBC settings、LMG/MODIFY/SPEA2 configs及全部 metrics。验证 ILP feasibility、Hamming constraints、runtime/scaling和在不同 weights 下的 Pareto/entropy tradeoff。
- 应做 prospective wet-lab holdout：合成代表性 mutants，测 binding affinity/specificity/function/expression/stability/developability，并比较模型 calibration 与真实 hits；测试 epistasis、结构不确定、不同 antigens、mutation budget、off-target 和 distribution shift。序列设计与实验还应遵守机构生物安全、知识产权、数据和伦理审查；模型 proxy 不能替代生物实验或临床证据。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 combinatorial optimization/AI for biology 扩展摘要。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/DUGN7746.pdf) 核验 PLD 的 score/ILP/diversity constraints、三系统、Table 1及作者限制；没有把 in-silico/oracle proxy 优势写成抗体结合、药物有效、安全或临床结果。
