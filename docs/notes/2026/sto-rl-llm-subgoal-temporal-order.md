---
title: "STO-RL: Offline RL Under Sparse Rewards via LLM-Guided Subgoal Temporal Order"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "generative_agents"]
dblp_key: ""
doi: "10.65109/EHJQ3648"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/EHJQ3648.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["fixed_subgoal_order_assumption", "llm_mapping_error", "offline_dataset_coverage", "reward_shaping_scope", "sparse_reward_benchmark_only", "no_real_world_safety_validation"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# STO-RL: Offline RL Under Sparse Rewards via LLM-Guided Subgoal Temporal Order

## 一句话总结

STO-RL 用 LLM 从 task instruction/environment description 生成有序 subgoals，并生成 state-to-subgoal-stage mapping；再以该 stage 的 potential-based reward shaping 把 sparse terminal reward 变为 dense temporal-progress signal，最后在增广 offline dataset 上训练 policy。作者在 CliffWalking、FourRoom、PointMaze-UMaze、PointMaze-Medium 报告相对 goal-conditioned/hierarchical offline RL 的更快收敛、更高 success 和更短轨迹。方法的 policy-invariance/shaping论证依赖成功轨迹存在固定有序 subgoal chain 与正确阶段映射；不证明任意真实任务、错误 LLM plan 或离线数据缺失时仍安全有效。

## 方法与证据

- problem 是预收集 dataset 上的 finite-horizon goal-reaching MDP，原 reward 仅在到达 goal state 时为 1（§3.1）。offline RL 不进行额外交互，因而无法纠正 dataset coverage 外 action/state 的 value extrapolation、错误 dynamics或危险行为。
- 关键假设：任何 successful trajectory 都按 \(G_1,\ldots,G_K\) 的固定顺序完成 subgoals，并能给每一 state 分配 progress index \(k_t\)（Def. 1, §3.2）。具有可交换、并行、循环、分支、多策略或需回退的任务未必满足该结构；错误顺序会使 shaping 误奖/误罚。
- LLM 接收 language task instruction 和 state-space/environment description，输出 ordered subgoals 及 state-to-stage mapping \(h\)（Fig. 1, §3）。LLM 的 world knowledge、prompt、环境符号化和 mapping 可审计性决定结果；论文的“noisy/imperfect plan robustness”是其 simulator ablation，不是对开放世界计划正确性的保证。
- shaped reward 采用 potential-based form \(r'=r+\gamma\Phi(s_{t+1},t+1)-\Phi(s_t,t)\)，potential 使用 time/progress index；Theorem 1 说明在其定义下 positive subgoal progress 得到严格更高 shaped reward（§3）。该局部 preference 不是现实最优/安全 trajectory 证明，也不排除 mapping 错误、reward hacking或任务规范本身不完整。
- 训练用 shaped augmented dataset，与 offline goal-conditioned/hierarchical baselines比较。论文称在离散 CliffWalking/FourRoom 和连续 PointMaze-UMaze/Medium 中改善 success/trajectory length，并做 LLM sequence noise ablation（§1, §4–5）。这些标准环境的状态/语言描述和目标规则远小于真实机器人、医疗或驾驶的感知、因果与安全复杂度。
- 作者表示 LLM 可生成 zero/few-shot temporal plan，且结果对部分顺序噪声有竞争力（§1）。这不能说明不需要领域专家：subgoal semantics、forbidden states、negative constraints、dataset bias和任务成功定义仍需由应用方验证。

## 适用边界与复现

- 适用于结构化、串行 goal-reaching simulation 的 offline reward shaping 研究，尤其当任务说明和 state predicates 足以让人/LLM明确 subgoal order。
- 不应将 LLM subgoals直接用于执行控制或安全关键 sparse-reward决策。须有 human/domain review、hard constraints/guardrails、OOD detection、offline policy evaluation、uncertainty estimates、counterfactual data checks与保守 fallback。
- 复现应固定 datasets、goal/state descriptions、LLM model/version/prompt、subgoal/mapping parser、potential parameters、offline RL backbone、seeds和 success/length metrics；分别测 perfect、permuted、partial/noisy plan，且检查 shaped reward 是否改变原任务 policy ranking。
- 后续应处理 branching/parallel/temporally uncertain subgoals、learned or verified state mapping、multi-modal perception、negative/avoidance objectives、distribution shift及 real-world offline data；也需报告 LLM cost、failure cases和人工修订率。

## 与 AAMAS 的关系与核验说明

这是 AAMAS offline RL、LLM planning 和 reward shaping 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/EHJQ3648.pdf) 核验 ordered-subgoal/mapping pipeline、fixed-order assumption、PBRS formula/Theorem 1及四个 benchmark 范围；没有把 simulator shaping gain 写成开放世界计划正确性、真实安全或通用 offline RL 保证。
