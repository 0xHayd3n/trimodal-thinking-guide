# 5. Complete paper map

[Home](../README.md) · [Previous](04-evidence-and-limitations.md) · [Next: exercises](06-discussion-and-design.md)

All page references below address the actual **16-page TechRxiv v1 attachment**. PDF page 1 is the posting cover; printed manuscript page 1 starts on PDF page 2. Open the [version DOI](https://doi.org/10.36227/techrxiv.173153092.25969269/v1) or [official PDF endpoint](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.173153092.25969269/v1) beside this map. Access to TechRxiv may require an interactive browser.

## Every section and end matter

| PDF page(s) | Printed page(s) | Source location | What to read for | Guide |
| --- | --- | --- | --- | --- |
| 1 | cover | Posting cover, abstract, keywords, notice | Version, 13 Nov 2024 date, CC BY 4.0, preprint status | [README](../README.md) |
| 2 | 1 | Title, affiliation, 16 Nov header, abstract | Author and date discrepancy, proposal scope | [Evidence](04-evidence-and-limitations.md) |
| 2-3 | 1-2 | I. Introduction | Research question and decision-centered motivation | [Concepts](01-concepts-and-context.md) |
| 3 | 2 | II. Research Background and Motivation | Decision quality, risks, technology-first concerns | [Concepts](01-concepts-and-context.md) |
| 4 | 3 | III opening and III.A | Trimodal framing; fast/intuitive System 1 | [Concepts](01-concepts-and-context.md) |
| 4-5 | 3-4 | III.B | Slow/deliberate System 2 | [Concepts](01-concepts-and-context.md) |
| 5 | 4 | III.C | Why the author proposes System 3 | [Framework](02-framework-and-architecture.md) |
| 5-7 | 4-6 | IV opening | Human information processing; connected architecture views | [Framework](02-framework-and-architecture.md) |
| 7 | 6 | IV.A | Decision requirements and human-in-the-loop needs | [Framework](02-framework-and-architecture.md#decision-requirements-the-complete-checklist) |
| 8 | 7 | IV.B | Intuitive, rational, and control classification | [Framework](02-framework-and-architecture.md#classification-before-implementation) |
| 8-9 | 7-8 | IV.C | Application elements and principal-agent delegation | [Framework](02-framework-and-architecture.md#application-architecture) |
| 9 | 8 | IV.D | Data exchange and data architecture elements | [Framework](02-framework-and-architecture.md#data-architecture) |
| 9-10 | 8-9 | IV.E | Capabilities, algorithm types, data splits, model/output | [Framework](02-framework-and-architecture.md#algorithm-architecture) |
| 10 | 9 | V. Architecture Patterns | Four automation levels and accountability | [Patterns](03-patterns-and-pipeline.md#four-levels-multiple-configurations) |
| 10-13 | 9-12 | VI. Conclusion, Implications and Future Directions | Five implications, adaptive EA, pipeline, unanswered questions | [Patterns](03-patterns-and-pipeline.md) |
| 13 | 12 | Acknowledgment | Thanks to unnamed academic and industry colleagues | [Attribution](../ATTRIBUTION.md) |
| 13-15 | 12-14 | References [1-40] | Sources behind the conceptual argument | [Reference map](#reference-reading-map) |
| 16 | 15 | Author biography | Asif Q. Gill's affiliation and professional context as stated in v1 | [Attribution](../ATTRIBUTION.md) |

**Appendices:** none are present. References and the biography are end matter, not appendices.

## All five figures

| Figure | PDF page | Role in the argument |
| --- | --- | --- |
| 1. Trimodal thinking systems: fast, slow and control | 4 | Environment encloses dashed fast/slow boxes joined by a plain interface/interaction line; dotted control connections have no arrowheads |
| 2. Human-centric AI system architecture conceptualization | 6 | System labels point into corresponding puzzle pieces in a human head, surrounded by sensory/cognitive and role-attribute labels; no system-to-system flow is specified |
| 3. AI system architecture | 6 | Users point into a container with parallel application/data/algorithm pillars; no arrows connect the pillars |
| 4. Human-centric Adaptive EA Framework v5.0 | 12 | Interaction spans Human/Technology/Facility columns; black arrows highlight Decision and Algorithm additions; environment/protection/observability span the base |
| 5. AI system architecture pipeline: based on [5] | 13 | Initiate/Discover/Implement panels are spanned by a double-headed Govern & Adapt arrow; governance and adaptation are not downstream-only sequential boxes |

Library did not supply viewable figure pixels in this environment; the parent reviewer subsequently inspected all five figures in the original attachment and relayed the observations incorporated above and in modules 2-3. The guide does not invent execution flows from conceptual connectors. VI's prose refers to Figure 5 when discussing the framework domains that accompany Figure 4; keep this source inconsistency in mind.

## All seven tables

| Table | PDF page(s) | What it contributes | Guide coverage |
| --- | --- | --- | --- |
| I. Decision Requirement Elements | 7 | Sixteen fields for a decision catalog | [All fields](02-framework-and-architecture.md#decision-requirements-the-complete-checklist) |
| II. AI System Classification | 8 | Three broad roles with examples | [Classification](02-framework-and-architecture.md#classification-before-implementation) |
| III. AI Application Architecture Elements | 8 | Actor, interface, application, agent, environment | [Application](02-framework-and-architecture.md#application-architecture) |
| IV. Data Architecture Elements | 9 | Actor, interface, data system, data | [Data](02-framework-and-architecture.md#data-architecture) |
| V. Algorithm Architecture Elements | 9-10 | Algorithm, input, output, model; heading spans pages | [Algorithm](02-framework-and-architecture.md#algorithm-architecture) |
| VI. Trimodal Thinking, Automation Levels, Patterns | 10 | Four levels; semi-automation has fast and slow variants | [Patterns](03-patterns-and-pipeline.md#four-levels-multiple-configurations) |
| VII. Trimodal Thinking Implications | 10-11 | Five implications; heading and content span pages | [Implications](03-patterns-and-pipeline.md#five-implications-proposed-benefits) |

## Reference reading map

**Table review status:** all seven tables were reviewed in the original attachment. Tables II-IV, VI and VII had source-edge clipping. The parent reviewer recovered the off-page drawing content with widened in-memory page canvases, rendered it, and visually checked the missing descriptions and automation patterns without changing the original PDF. The guide now incorporates that recovered content; the missing-cell limitation is resolved.

This covers the role of **every reference number** in the attachment. It is a navigation aid to the paper's bibliography, not a claim that this guide independently read or verified every cited work. Bibliographic spellings and historical/current claims should be checked against the original works before reuse.

| Source references | Purpose in the paper |
| --- | --- |
| [1] Tekic and Fuller; [2] Grobelnik, Perset, Russell | AI innovation context and AI-system definition |
| [3] Michael, Schoenherr, Vogel | Human leadership, failure, and responsibility in AI decisions |
| [4] Howard and Abbas; [6] Hastie and Dawes; [7] Haselton, Nettle, Andrews | Decision analysis, judgment, uncertainty, and cognitive bias |
| [5] Gill; [10] Gill and Hansnata | Adaptive enterprise architecture and decision catalogs/investment design |
| [8] Kahneman | Fast and slow thinking as the central starting point |
| [9] McCarthy, Minsky, Rochester, Shannon; [37] McCulloch and Pitts | Historical background to AI and neural computation |
| [11] Diane-Gabrielle, Yagoubi, Psyche; [12] Sospeter and colleagues | AI ecosystems, providers, and use-case assessment |
| [13] EU AI Act resource; [14] Australian Government; [15] OECD; [16] NIST | Responsible AI policy/principles/standards context as cited in v1 |
| [17] principal-agent introduction; [18] agent-oriented software engineering; [19] Qumer and Henderson-Sellers | Delegation, agents, and agent behavior |
| [20] Davies; [21] directional-stability/control reference; [22] Lawrence | Homeostasis, control, and human intelligence as conceptual lenses |
| [23] Beshears and Gino | Decision architecture and choice framing |
| [24] Jonkers and colleagues; [25] TOGAF; [26] Zachman; [27] Federal EA; [28] EIRA | Enterprise architecture definitions and frameworks |
| [29-30] Simon | Bounded rationality and constraints on decision making |
| [31] Rogers and colleagues; [32] Atkinson and Shiffrin | Information processing and memory background |
| [33] McCarthy | Intelligence/AI definition |
| [34] Iansiti and Lakhani; [35] Shakarian and colleagues | AI business/algorithm context and neuro-symbolic methods |
| [36] Ryseff and colleagues, RAND | AI project failure motivation; external background rather than original trimodal results |
| [38] Billiris and Gill | Generative AI/copyright concerns |
| [39] Peters, Vold, Robinson, Calvo | Ethical design practice |
| [40] Michael, Pitt, Sargent, Scornavacca | AI automation in higher education |

The biography on PDF page 16 provides source-era professional information about the sole author. This guide does not assert that every title, membership, or publication count remains current.
