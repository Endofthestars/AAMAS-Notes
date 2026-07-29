---
title: "IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "planning_scheduling", "generative_agents"]
dblp_key: ""
doi: "10.65109/BRAG3288"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BRAG3288.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-02b"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["gui_grounding_fragility", "limited_trace_corpus", "mixed_benchmark_suite", "in_house_evaluation_component", "retrieval_memory_growth", "shared_memory_privacy", "no_high_risk_action_guardrails"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents

## 一句话总结

IntentCUA 将桌面交互 trace 编成 environment/action/keyword/description 的多视图 intent embedding，以 HDBSCAN 聚成 intent groups（IG）与 subgroups（SG），把重复 action pattern 变成带槽位的 skill hints，并让 Planner、Plan-Optimizer、Critic 共享 plan memory、检索并补全计划。在 286 个混合 GUI 任务上报告 74.83% success、SER 0.91 与 1.46 分钟平均延迟，优于 UI-TARS-1.5/UFO2；但对 popup/遮挡的 grounding 仍会失败，且真实高风险 computer-use 需要额外权限与安全控制。

## 方法与证据

- 离线管线把 control trace 表为 \([E,A,D]\)、browsing trace 表为 \([E,K,D]\)，multi-view encoder 用 contrastive、prediction、reconstruction 损失将其对齐到共享 embedding；先按环境聚 IG，再以 HDBSCAN 划分更细 SG（§3.1--§3.2）。SG 保存 centroid、代表 traces、support count 与从 action sequence 抽象出的 parameterized verb--argument skill schema。
- 在线 Planner 对 plan units 在 IG gate 后检索 SG：完整 hit 复用用户批准的 global plan，partial hit 注入 skill hints 填 gap，miss 则据模板合成计划。Plan-Optimizer 在当前 GUI grounding 下执行，Critic 返回 success/retryable/blocked 并触发局部修正（§4--Algorithm 1）。共享 plan memory 因而同时是效率资产与可能包含用户跨应用历史的敏感数据。
- GUI state 来自可操作组件枚举、窗口标题/panel/component-count metadata；当意外 popup 遮挡组件时，论文的 case study 显示 grounding 会失败并导致错误 retry（§5.3）。这不是对任意动态 UI、权限对话框或恶意页面的稳健性保证。
- trace mining 使用 18 sessions 的 30 active hours、113 trace files、36 domains；评测为 286 个真实 GUI tasks：100 in-house、116 WebVoyager、70 ScreenAgent，横跨 63 domains，其中仅 22 与 trace domains 重叠（34.92%）（§5.1）。这有 65.07% 未见领域，但也意味着数据规模/标注来源与公开 benchmark 完全可复现实况需要进一步审查。
- 全系统 ablation 从 planner-executor baseline \(B\) 的 22.73% success/33.78% completion，加入 greedy trace retrieval 到 46.43%/57.41%，再加入 IG/SG retrieval + representation 到 54.64%/77.56%；完整 \(B+T_{SG}+Z+S_{SG}+PM\) 达 74.83%/91.14%（Table 1）。组件有互补贡献，但表中部分组合不单调，不能将任一单组件视为独立充分原因。
- 对 UI-TARS-1.5 和 UFO2 的 end-to-end 比较：IntentCUA 在 WebVoyager/ScreenAgent/in-house 分别 71.6/77.1/78.0%，overall 74.8%；UFO2 为 69.0/41.4/38.0%，overall 51.2%；UI-TARS-1.5 为 35.9/42.9/46.0%，overall 38.8（Table 2）。所有 agent 使用相同 atomic GUI interface 与 timeout policy，仍须关注具体模型版本、任务适配与评价判定。
- 长度分桶中，IntentCUA 10--15、15--20、20--25 steps 为 85.9/72.5/65.0% success，>30 steps 仍 42.9%；SER 0.91（UI-TARS 0.85、UFO2 0.82），平均 latency 1.46 min（UFO2 6.63、UI-TARS 9.82）（§6）。延迟收益可能随 memory 规模增长改变；作者也指出 retrieval efficiency 会波动。
- 作者建议 graph retrieval、lightweight vision cues 以改善动态/视觉变化界面；论文未给出敏感操作授权、数据最小化、审计日志、欺骗 UI 防护、支付/删除等高影响动作确认机制（§7）。

## 适用边界与复现

- 适用于有大量经许可、可去标识化的重复 desktop workflow trace，且任务可分解成可检索 intent/skill 的企业内部辅助自动化。优先从只读、可逆、人工确认的事务试点。
- 不应用于直接执行转账、发送、删除、账号权限修改、医疗/法律提交等高影响操作；memory 检索与 LLM 计划应受 least privilege、action allowlist、target/value 二次确认、sandbox、截图/DOM 对齐核验、审计和 kill switch 约束。
- 复现应公开或受控提供 113 traces、intent labels/views、encoder/HDBSCAN/阈值、slot template、agent prompts/models、timeout、任务完成判定与每基准任务清单；分别重跑 Table 1、Table 2、SER/latency 和 step bins，并区分首次任务、已命中记忆任务和未见 domain。
- 部署前应做 popup、A/B UI、权限对话、错位控件、网络故障、提示注入、恶意网页、memory 污染/泄露与大规模 memory 延迟的红队测试；失败时应停在 blocked/请求人工，而非重复点击或自行扩大权限。

## 与 AAMAS 的关系与核验说明

这是 AAMAS 的 computer-use agent、技能抽象、记忆检索与多 agent planning 工作。笔记依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/BRAG3288.pdf) 核验 §3--§6 的 trace/SG/plan-memory 机制、286-task 组成、ablation、baseline 比较与 failure case；没有将受控基准的 success/效率数字泛化为开放桌面上的安全自治能力。
