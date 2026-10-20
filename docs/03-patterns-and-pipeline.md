# 3. Automation patterns and the enterprise pipeline

[Home](../README.md) · [Previous](02-framework-and-architecture.md) · [Next: evidence](04-evidence-and-limitations.md)

## Four levels, multiple configurations

V/Table VI distinguishes manual, semi-automated, automated, and autonomous decision making. Semi-automation includes assistance with either fast or slow thinking. The surrounding prose says organizations should choose for the particular decision's context, domain, and risk, and that people remain accountable for decisions and outcomes. [V, PDF p. 10](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

| Level / variant | System 1 | System 2 | System 3 | Human control stated in Table VI |
| --- | --- | --- | --- | --- |
| 1. Manual | Human | Human | Human | Full control |
| 2. Semi-automated, fast assistance | AI | Human | Human | Humans in the loop, full control |
| 2. Semi-automated, slow assistance | Human | AI | Human | Humans in the loop, full control |
| 3. Automated | AI | AI | Human | Humans in the loop, full control |
| 4. Autonomous | AI | AI | AI | No human intervention; humans have no control |

This is an original reformatted summary of the recovered Table VI, whose pattern column is labeled **Systems 1-3 Patterns**. The distinction between levels 3 and 4 is particularly important: level 3 keeps System 3 human and explicitly retains full human control, whereas level 4 assigns the control role to AI. Human accountability and responsibility nevertheless remain at every level in the surrounding prose. Accountability is therefore not the same as having operational control.

These configurations are not a certification scale, an instruction to maximize autonomy, or a demonstrated sequence of organizational maturity. The source allows additional patterns from combinations of the roles. Its stated allocations describe the proposed configurations; they do not demonstrate that an implementation delivers effective intervention or safety.

**Source-layout and recovery note:** Table VI extends past the original attachment's right page edge. The parent reviewer recovered its off-page drawing content by widening an in-memory page canvas and visually checking the resulting rendering, without modifying the original PDF. The missing table mapping is now resolved; it was not guessed from the adjacent prose. [Provenance](../metadata/paper.json)

## Five implications: proposed benefits

VI/Table VII discusses five areas. [VI, PDF pp. 10-12](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

1. **Social:** consider bias, ethical concerns, and potential harm while defining the decision architecture.
2. **Economic:** use human-centric architecture and pattern-driven, systematic AI adoption to address failure and waste.
3. **Understanding:** use the classification lens and architecture patterns to explain AI systems and their automation levels.
4. **Architecture discipline:** extend broader enterprise architecture through trimodal thinking and explicit AI architecture responsibilities.
5. **Adaptive framework and pipeline:** add trimodal thinking, AI system architecture, and decision architecture domains to the adaptive framework, with a concrete design pipeline.

These are motivations, interpretations, and anticipated benefits. The paper does not measure a reduction in harm, cost, project failure, or misunderstanding. An architecture diagram can clarify a responsibility while leaving the quality of its implementation unresolved.

## Broader enterprise architecture

VI discusses existing architecture frameworks, including Adaptive EA, TOGAF, Zachman, Federal EA, and EIRA. Gill argues for explicit attention to AI system architecture in this broader discipline. This is the author's 2024 framing; do not treat its assessment of frameworks as a current inventory of their 2026 capabilities. [VI, PDF pp. 11-12](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

Figure 4 presents Human-centric Adaptive EA Framework v5.0. Its top **Interaction** band spans three columns. The Human column contains business, information, decision, social, and professional architecture. Technology contains application, data, algorithm, platform, and infrastructure architecture. Facility contains spatial, energy, HVAC, HS, and ancillary architecture. The source does not expand the figure's HS abbreviation in this discussion, so this guide does not guess its expansion. Full-width bands for environment, protection, and observability sit below the columns, above a system-or-ecosystem label. These place AI in organizational surroundings instead of treating it as an isolated model. [Figure 4, PDF p. 12](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

Black arrows highlight the new **Decision** entry in Human and **Algorithm** entry in Technology. They mark additions; they are **not flows between columns**. The parallel application, data, and algorithm entries are also broader technology domains rather than an instruction to process data in a particular sequence.

The prose's reference to Figure 5 while discussing framework domains appears inconsistent with the displayed Figure 4 caption. Use the caption and the complete [map](05-paper-map.md) to navigate, and preserve this as a source cross-reference issue rather than silently renumbering the figures.

## The five-stage pipeline

Figure 5 has three side-by-side panels: **Initiate** defines the AI vision and decision-making scope; **Discover** identifies decision requirements and AI system architecture; **Implement** develops the AI roadmap and implementation plan. A horizontal double-headed **Govern & Adapt** arrow spans all three panels. Governance and adaptation therefore apply across the work, rather than appearing as two downstream-only boxes after implementation. [VI, Figure 5, PDF p. 13](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

The accompanying text calls these **five iterative stages**. The summary below paraphrases those five responsibilities; its row order is not a one-way execution sequence.

| Stage | Purpose in the source | Example artifact to prepare (companion suggestion) |
| --- | --- | --- |
| Initiate | Establish stakeholders' vision and scope for AI in decision making | A statement of the decision and who is affected |
| Discover | Specify the decision catalog and connected architecture at the chosen automation level | Decision record plus application/data/algorithm views |
| Implement | Develop the roadmap and incremental implementation plan | A staged delivery plan with explicit dependencies |
| Govern | Guide implementation against its intended design | Review criteria and named accountable reviewers |
| Adapt | Handle changes in architecture or implementation | A change record and reconsideration of assumptions |

The paper describes the stages as iterative, and the spanning Govern & Adapt arrow reinforces that reading. It does not supply a mandatory project management method, stage durations, or an experimentally optimized ordering. Its "Implement" discussion emphasizes roadmap/planning; a reader should not infer that a working implementation was built and evaluated in the paper.

## The research agenda

The closing questions concern switching conditions, each system's degrees of freedom, control flow and allocation, navigation, observability, information traceability, and interfaces. These are crucial open details: they expose what a future implementation must specify. [VI, PDF p. 13](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

For example, an escalation policy that always chooses deliberate analysis may consume too much time; one that almost never escalates may preserve fast mistakes. A controller needs a defensible policy and evidence about its tradeoffs. This example illustrates the unanswered problem; it is not a result reported by Gill.
