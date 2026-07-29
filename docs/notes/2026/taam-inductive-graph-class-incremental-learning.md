---
title: "TAAM:Inductive Graph-Class Incremental Learning with Task-Aware Adaptive Modulation"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "safety_verification", "planning_scheduling"]
dblp_key: ""
doi: "10.65109/WSBG8309"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WSBG8309.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["task_module_growth", "task_id_inference_dependency", "inductive_split_scope", "fixed_sgc_backbone", "benchmark_reimplementation", "graph_shift_coverage", "no_privacy_audit"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# TAAM:Inductive Graph-Class Incremental Learning with Task-Aware Adaptive Modulation

## 一句话总结

TAAM 在 graph class-incremental learning 中冻结共享 SGC backbone、为每个新任务训练并冻结一个 node-attentive Neural Synapse Modulator（NSM），再以 Anchored Multi-hop Propagation（AMP）在没有 task ID 时选择模块；在八个按训练/测试子图隔离的基准上得到很高 AA 和 0% AF，但该“零遗忘”依赖任务级参数隔离和近乎完美 task retrieval，并以每任务新增模块/分类器为代价，尚不等于固定容量或真实动态图上的长期无条件泛化。

## 方法与证据

- 论文针对 GCIL：任务逐步到来、inference 时没有 task ID，既要留住旧类又要区分类间相似任务（§1、§3）。与传统同一 evolving graph 上的 transductive 切分不同，作者将每任务的 \(G^{train}_k\) 与未见 \(G^{test}_k\) 设为完全独立子图，强调其为更严格的 inductive scenario（§3.1）。这验证对未见 graph structures 的迁移，但也改变了既有 benchmark/方法的适用条件。
- TAAM 使用固定的两层 Simplifying Graph Convolution backbone。新任务到来时新建 NSM：由 task embedding 生成 feature-wise linear modulation，对节点表示作多头、node-attentive 调制；只训练该 NSM 与相应分类器，之后冻结（§4--§5.1）。因此避免回放历史图数据，但 task 数增加仍线性积累 experts、embeddings 和 classifier 参数。
- AMP 基于多尺度邻域传播形成 task prototype，在测试图上先推断 task affiliation，再调用对应 NSM；论文称有理论 grounding，并在 Figure 4 与 TPP 的 Laplacian smoothing 比较中报告接近完美 task-ID accuracy（§4、§5.4）。若 task identification 错误，参数隔离本身无法挽救，可能把输入交给错误 expert；图中没有以显著 task ambiguity、开放集或 adversarial shift 系统量化这种失配。
- 数据覆盖 CoraFull、Arxiv、Citeseer、Reddit、Products、Photo、Computer、WikiCS，共 3--35 个任务，最大 Products 约 245 万节点（Table 2）。训练每任务 200 epochs，Adam lr 0.005、weight decay \(5\times10^{-4}\)，task embedding dimension 6、NSM 2 heads；baseline 超参按原论文配置，并使用同一组 random seeds（§5.1）。
- Table 1 中 TAAM 在八个数据集均报最高非 Joint/Oracle AA 与 0.0% AF，例如 Products 92.9% AA、PDGNNs 45.2%，Computer 97.5% 与 TPP 19.9%；表中的 Joint 可访问所有任务数据、Oracle 还访问 task IDs，故只是参照上界，不是公平 continual baseline（§5.2）。零 AF 应解读为已选择正确冻结模块后旧任务性能未被新任务参数更新破坏，而非不需要存储 task-specific state。
- 消融移除 task-aware module 后性能大幅下降且出现遗忘；移除 NSM 保持 0 AF 但 AA 显著下降，说明隔离带来稳定性而细粒度调制提供 plasticity（Table 3）。Table 4 给出 TAAM 每任务新增约 0.02M--3.0861M float32 参数、平均 AA 92.9，TPP 为 0.01M--1.7949M / 64.3；文章的“轻量”是相对多数 replay methods 的参数/运行成本，不是零增长。

## 适用边界与复现

- 适用于任务可分、能为每一类图分布保留 expert、并且允许模型容量随任务增大的离线/批式 continual graph classification；不宜直接推断到无清晰任务边界、关系持续重连、标签语义漂移、单图 transductive 传播、严格固定内存或毫秒级在线系统。
- 复现需公开八数据集的 task/class 划分、训练/测试 subgraph 分离代码、所有 seeds、backbone/NSM/LoRA/AMP 细节、prototype 构造、统一/分离 classifier、baseline 实现与预训练成本。应同时报告 AA、AF、task-ID accuracy、每任务/总参数、峰值内存、训练/推理时间、任务数量增长曲线及误路由后的性能。
- 必须做对 task boundary 噪声、类重叠、OOD/novel task、边/特征漂移、长 sequence（远超 35 tasks）、不平衡类、私有/敏感图和攻击性 task-ID spoofing 的评估；“不回放”降低原始历史数据存储，并不自动构成隐私保证，prototypes/参数仍可能泄漏信息。
- 若被用于风险敏感的推荐、社交/金融图或药物筛选，应将 AMP confidence、未知任务检测、资源上限、回滚/人工审查与公平性/隐私评估置于模型外层；高 AA 或 0 AF 不能单独保证群体稳定性、因果有效性或安全决策。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 continual graph learning、模块化 agent engineering 与可靠任务路由论文。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/WSBG8309.pdf) 核验 inductive subgraph 定义、冻结 SGC/每任务 NSM、AMP task-ID 机制、八数据集、训练配置、Table 1/3/4 的 AA/AF/参数结果与 benchmark 对比方式；没有把参数隔离的零 AF、有限 task sequence 或不回放数据夸写为固定成本、现实动态图的完全遗忘消除或隐私认证。
