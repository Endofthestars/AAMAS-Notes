---
title: "Raise BDI Agents, First Steps"
conference: "AAMAS"
year: 2026
track: "doctoral_consortium"
topics: ["agent_engineering", "human_agent_interaction", "argumentation_reasoning", "generative_agents"]
dblp_key: ""
doi: "10.65109/JYPA1233"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JYPA1233.pdf"
code_url: ""
note_status: "reviewed"
review_route: "spark_dual_pass_terra_targeted"
review_batch: "2026-batch-05b"
spark_draft_verdict: "source_grounded_draft_needs_revision"
spark_qa_verdict: "pass_after_validation_quantification_virtual_embodiment_and_future_status_revision"
spark_consistency: "pass"
risk_level: "high"
risk_tags: ["doctoral_research_overview", "virtual_bdi_embodiment", "jason_cartago_godot", "rcc_spatial_reasoning", "llm_mediated_chatbdi", "temper_personality_model", "author_reported_validation_without_metrics", "github_url_absent", "no_physical_robot_or_safety_evidence", "future_collaboration_exploration_and_stabilization"]
escalation_model: "gpt-5.6-terra"
escalation_reason: "targeted_validation_virtual_embodiment_llm_personality_and_future_feature_boundary_check"
escalation_verdict: "pass_after_author_reported_validation_and_no_deployment_inference_boundaries"
generated_by: "GPT-5.3-Codex-Spark"
reviewed_by: "GPT-5.3-Codex-Spark independent QA; GPT-5.6 Terra targeted implementation-evidence check; Codex source reconciliation"
reviewed_at: "2026-07-30"
---

# Raise BDI Agents, First Steps

## 一句话总结

VEsNA 把 Jason BDI mind 接到 Godot 三维虚拟 body，并以 CArtAgO artifacts、RCC 空间关系、局域 KQML 通信、LLM-mediated ChatBDI 与 Temper 扩展形成可交互原型；作者报告多项评估和案例，但这篇三页概述没有给任何定量结果，不能据此推断语言可靠性、真实人格、物理具身、安全性或生产可用性。

## 当前实现范围

VEsNA（Virtual Environments via Natural Language Agents）是 Jason 的扩展，并使用 JaCaMo 的 CArtAgO infrastructure 管理 workspace 与 objects。当前 agent side 使用 Jason，virtual-environment side 使用 Godot；作者称全部代码在 GitHub，但本稿没有仓库 URL（§1，p. 4002）。

Figure 2 把 agent 分为：

- **mind**：维护 beliefs/goals、选择策略、解释环境信号、响应事件并感知 artifacts；
- **body**：执行 mind 指令、报告环境事件，并反馈 action progress 与 failure。

二者通过 WebSocket 交换 JSON messages。RCC–Regions 与 Workspace–Objects 是 mind/body 间的 digital-twin component pairs；其他组件可能只存在一侧（§2，pp. 4002--4003）。

这是 Godot 中的虚拟三维具身。论文没有物理机器人、真实传感器、执行器误差或现实环境部署证据。

## 空间推理与移动

mind 使用 Region Connection Calculus（RCC）以 region 关系谓词推理空间语义，而不是直接依靠坐标。body 保留 regions 的物理表示，负责路径规划与移动到 mind 指定的位置（§2，p. 4003）。

该分工说明 VEsNA 如何把符号空间关系接到虚拟运动执行，但概述没有给地图规模、路径算法、动态障碍、规划成功率或延迟。当前地图必须预先已知，在线探索仍是未来问题。

## CArtAgO artifacts

VEsNA artifacts 继承 CArtAgO 的 observable properties 与 operations interface，并加入 position、occupancy 和 portability。两种类型是：

- **situated**：固定在原位，并配置 maximum number of simultaneous users；本稿没有给该上限的具体值；
- **grabbable**：可移动，同一时刻只能由一个 agent 持有。

作者报告以 coffee-preparation scenario 评估该特性：agent 需要找到 grabbable cup 与 situated coffee machine 并组合使用。三页稿没有完成率、并发冲突、baseline 或失败轨迹，因此它是被命名的案例，不是可量化性能结论（§2，p. 4003）。

## Situated Communication

VEsNA 修改 Jason 的 `.send` internal action，使 agents 只有在同一 room 时才能通信。支持：

1. **private**：只向指定 agent 发送；
2. **public**：向 target agents 发送，同时可被同房间其他 agents overhear。

如果 intended receiver 不在房间，旁听到消息的其他 agent 可以依据自身设计处理请求或信息。这是 locality-aware delivery semantics；概述没有评测消息丢失、拥塞、错误接手、隐私或对抗窃听。

## ChatBDI 的双向语言桥

### `nl2kqml`

用户自然语言消息先按 KQML illocutionary force 分类，再用预训练语言模型产生 embedding，并与 agent beliefs 和/或 plans 匹配最合适的 template。另一个组件——当前是 LLM——利用该 template 生成最终内容，再作为标准 KQML message 交付给 receivers（§2，p. 4003）。

### `kqml2nl`

agent 要与用户通信时，LLM 把内部 KQML message 转成自然语言。

作者在摘要中把 `nl2kqml` pipeline evaluation 列为已做工作，但本稿没有模型名、prompt、数据集、样本量、accuracy、semantic error、hallucination、用户评测或 latency。因此该结构提供了符号接口，不证明 LLM mediation 可靠、faithful 或安全。

## Temper：人格与 mood 进入 plan selection

Temper 包含 immutable part 与 mutable mood。plans 带 temper annotation，也可带改变 temper 的 effects。agent 可以选择与当前 temper 最相似的 plan，或按权重随机选择。表示是 model-agnostic 的，但当前实现和实验采用 Big Five personality model（§2，p. 4003）。

摘要报告评估了 temper-driven plan selection，并提到与 Untold Games 合作的复杂 multi-agent scenario；正文仅说该工作在合作 master thesis 中测试，详情见 [5]。仓库另有 [VEsNA-Pro: Exploiting BDI Agents with Propensities for Emergent Narrative](./vesna-pro-bdi-propensities-emergent-narrative.md) 的独立全文笔记；其理论、原型和问卷数字不能倒灌为本概述自身披露的结果。

Temper 是设计者选择的状态维度与 plan-selection rule。它不证明 agent 拥有人类人格、情绪、心理真实性或稳定的用户感知。

## 作者报告的验证与证据缺口

摘要列举：

- `nl2kqml` natural-language pipeline evaluation；
- temper-driven plan selection assessment；
- 与 Untold Games 合作的 complex multi-agent scenario；
- 扩展 BDI syntax/semantics 的理论贡献。

正文还命名 Office default test scene 与 coffee scenario。所有这些只能写成“作者报告已评估/测试”，因为本稿没有样本量、baseline、metric、数值、统计检验、运行时间、错误分析、统一实验协议或代码链接。

## Future Work

§3（pp. 4003--4004）明确列为后续：

1. **Collaborative Plans**：正在开发 collaborative annotation、协作需求与 failure handling；
2. **Exploration**：运行时构建 spatial representation；作者明确说已有 feasibility study 和 initial steps，但尚无 significant results；
3. **Sight**：感知 object 消失或被另一 agent 持有；
4. **Learning**：以逻辑形式从预定义 actions/plans 学习高层 plans，第一步是生成 runtime execution traces；
5. **User in environment**：用户控制 avatar 或通过 VR 沉浸；
6. **Stabilization**：探索面向 Unity/Unreal 的 C-based Jason，整合组件并以未来目标改善第三方实用性与可靠性。

这些都不是已完成能力，尤其不能把“第三方可用”写成已验证交付。

## 与 AAMAS 的关系与核验说明

VEsNA 连接 BDI programming、virtual embodiment、agent communication、spatial reasoning 与人机语言交互。笔记依据 [AAMAS 官方 PDF](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/JYPA1233.pdf) 核对 Figures 1--2、§2 组件与 §3 路线，并将所有验证保留为未量化的作者报告。
