---
title: "Reinforcement Learning for Falsification of Dynamic Driving Scenarios"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["safety_verification", "robotics_embodied", "agent_engineering"]
dblp_key: ""
doi: "10.65109/PFBJ1092"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PFBJ1092.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03u"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "simulation-only", "metric-temporal-logic", "adversarial-testing", "scenario-template-dependence"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Reinforcement Learning for Falsification of Dynamic Driving Scenarios

## 一句话总结

该工作把 SAC 用作仿真驾驶系统的 falsification 工具：对手车辆在自身保持安全的约束下，搜索会使被测 ACC+MOBIL 车辆违反安全规格的连续 throttle/steer 场景，并同 cross-entropy sampling 比较效率、覆盖与质量。这是用于发现测试反例，而非生成现实道路攻击策略。

## 方法与证据

- Scenic/VerifAI 场景以 MTL robustness 表达对手安全与受害车间距违反；SAC observation 是 346 维 LiDAR stack，action 为连续加速/转向，reward 依 trajectory robustness 和推进/速度项构成（§2）。
- 评测 platoon 和 multi-lane highway；系统被测对象为带 lane-changing (MOBIL) 的 ACC。ScenicGym 重复实例化优化后，在 84/200/323 road-unit maps 上吞吐提高 82.8%/47.8%/6.0%（§2）。
- Table 1（4 iterations、每次 1000 samples）：platoon 中 CE/SAC 反例数 527.75/103.75、TPS 3.6/7.3；multi-lane 中 117.75/154.75、TPS 2.2/7.2。SAC 在 multi-lane 效率更高，在 platoon 更低；其 coverage/quality 指标也随 scenario 有取舍（§3）。

## 适用边界与复现

- 反例只覆盖 Scenic template、传感器模拟、ACC/MOBIL及所选 MTL property；不表示真实车辆或交通系统不安全。质量/多样性 scores 的特征选择会影响算法结论。
- 复现需公开 Scenic scripts、地图/交通参数、SUT、MTL formulas、state/reward/termination、SAC/CE hyperparams、并行环境、random seeds、QED feature definitions和仿真版本。应把发现的反例用于回归测试、工程审查和安全改进，而非实际道路尝试。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/PFBJ1092.pdf) 人工核对测试框架和 Table 1；本条目仅作防御性安全验证分析。
