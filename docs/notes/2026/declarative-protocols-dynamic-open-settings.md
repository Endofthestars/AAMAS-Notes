---
title: "Discovery and Enactment of Declarative Interaction Protocols in Dynamically Open Settings"
conference: "AAMAS"
year: 2026
track: "research"
topics: ["agent_engineering", "norms_trust_governance", "generative_agents"]
dblp_key: ""
doi: "10.65109/UBWR1103"
official_url: "https://www.ifaamas.org/Proceedings/aamas2026/forms/contents.htm"
pdf_url: "https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UBWR1103.pdf"
note_status: "reviewed"
review_route: "manual_primary_source_check"
review_batch: "2026-batch-03w"
spark_draft_verdict: "incomplete"
spark_qa_verdict: "manual_source_check_pass"
spark_consistency: "manual_check"
risk_level: "medium"
risk_tags: ["extended_abstract_only", "protocol-discovery", "hypermedia-workspace", "role-binding", "prototype-demonstration"]
escalation_model: "none"
escalation_reason: "not_required"
escalation_verdict: ""
generated_by: "Codex"
reviewed_by: "Codex (manual primary-source check)"
reviewed_at: "2026-07-29"
---

# Discovery and Enactment of Declarative Interaction Protocols in Dynamically Open Settings

## 一句话总结

本文将 BSPL 信息协议与 hypermedia-driven interaction 结合，使 agents 在运行时从 workspace 发现协议、参与者与交互控制，再通过 metaprotocol 协商角色并按信息依赖分散执行。其重点是动态开放系统的松耦合协调，不是对任何未知协议的自动语义理解。

## 方法与证据

- 三阶段：hypermedia workspace 内发现候选协议/参与者；用 role-negotiation metaprotocol 绑定参与者；由信息依赖与 hypermedia controls 指引后续执行（§2）。
- workspace 以 body artifacts 表达 agents，暴露其 protocol/role/capability metadata 及可用 controls；BSPL 以信息依赖而非硬消息顺序指定交互，缓解参与者临时不可达造成的阻塞（§1–2）。
- 原型为 rug bazaar：buyer 从单一入口发现 offers、seller 和 Buy protocol，协商 Seller role 后执行 Pay/Give。使用 BSPL Python、Yggdrasil 与 Python/Kiko agents（§3）。

## 适用边界与复现

- 安全、活性和 just-in-time availability 被交给 workspace designers；agents 仍需领域知识来判断 protocol 语义与角色适配性。发现链接不等同于信任、授权或安全执行。
- 复现应公开 workspace ontology、协议/元协议、artifact metadata、链接关系、失败/离开场景、身份授权与 prototype scripts。动态开放部署还需签名、能力最小化、协议验证与审计。

## 与 AAMAS 的关系与核验说明

依据 [AAMAS 官方 PDF（Liverpool 镜像）](https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2026/pdfs/UBWR1103.pdf) 人工核对架构、Buy scenario 和原型；未将市场演示外推为大规模开放网络的可靠性证明。
