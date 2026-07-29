---
title: "Active Inference through Incentive Design in Partially Observable Markov Decision Processes"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["planning_scheduling", "game_theory_mechanism", "agent_engineering"]
dblp_key: ""
doi: "10.65109/GILC9892"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GILC9892.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03d"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_check"
spark_consistency: "manual_check"
risk_level: "high"
risk_tags: ["extended_abstract_only", "incentive_manipulation", "softmax_best_response_assumption", "simulated_gridworld", "inference_not_ground_truth"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Active Inference through Incentive Design in Partially Observable Markov Decision Processes

## 一句话总结

论文让部分观察 leader 以 side payments 改变不同 follower types 的最优行为，以降低其类型 posterior entropy，并惩罚支付成本。softmax/entropy-regularized best response 使 bi-level 问题可降为单层梯度优化；在随机 10×10 gridworld，5 types 下平均 true-positive rate 从 28.73% 提至 57.12%。这是在模型准确、激励可行的模拟证据，不构成对真实人/员工/用户的监测、操控或意图识别授权。

## 方法与证据

- 将 follower type 与 state 组成 HMM augmented state，观测函数可随 type 变；目标最小化 \(H(T|O_{0:T})+\lambda h(x)\)（Definitions 1--2、Problem 1）。
- follower 被假定 entropy-regularized optimal，best response 唯一；据此用 softmax temporal consistency 与 HMM observable operators 做 first-order/hypergradient 优化（§2）。
- 实验为 FoV false-negative .05 的随机 10×10 gridworld、五 types、20 个可支付 states、\(\lambda=.1\)；收敛后 entropy 2.0457 到 .8652、cost 5.2590，5 experiments 的 TPR 如上（§3）。

## 适用边界与复现

- 激励改变被观察者行为，必须做知情、同意、合法性、操纵/歧视和成本上限审查；entropy 降低不等于类型真实、意图正确或合理干预。
- 复现需公开 MDP/types/priors/observation model、softmax temperature、payments domain/cost、horizon、gradient配置和每个 seed；对 model misspecification、战略抵抗与隐私风险测试。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/GILC9892.pdf) 人工核对目标、单层化假设与 gridworld 数值；未将其写成真实意图识别或正当激励证明。
