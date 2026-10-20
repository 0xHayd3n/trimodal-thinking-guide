# 3. Automation patterns and the enterprise pipeline

[Home](../README.md) · [Previous](02-framework-and-architecture.md) · [Next: evidence](04-evidence-and-limitations.md)

## Four levels, multiple configurations

V/Table VI distinguishes manual, semi-automated, automated, and autonomous decision making. Semi-automation includes assistance with either fast or slow thinking. The surrounding prose says organizations should choose for the particular decision's context, domain, and risk, and that people remain accountable for decisions and outcomes. [V, PDF p. 10](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

| Level | Reading of the source's configuration | Architecture question |
| --- | --- | --- |
| 1. Manual | People make decisions without AI and retain control | What evidence and support do they need? |
| 2. Semi-automated | AI augments fast or deliberate work; humans remain in the loop with full control | Which exact step is assisted and who accepts it? |
| 3. Automated | Much of the fast/slow decision work is automated, with humans in the loop | At what point can a person intervene effectively? |
| 4. Autonomous | The system can adapt and respond without human intervention in the decision process | What operating boundaries and accountability remain? |

The right column is a companion exercise. This is not a certification scale, an instruction to maximize autonomy, or a demonstrated sequence of organizational maturity. The source allows more patterns from combinations of the roles. Its language about intervention describes a configuration; it does not show that any configuration is safe.

**Extraction boundary:** the attachment's Table VI right edge is clipped in the Library text representation. This guide relies on the readable level labels and surrounding section V prose. It does not reconstruct missing cell wording or a precise control allocation beyond that evidence. [Provenance](../metadata/paper.json)

## Five implications: proposed benefits

VI/Table VII discusses five areas. [VI, PDF pp. 10-12](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

1. **Social:** consider bias, ethical concerns, and potential harm while defining the decision architecture.
2. **Economic:** align technology selection with real needs to avoid waste and failed adoption.
3. **Understanding:** use a shared architecture vocabulary to explain system elements to technical and nontechnical audiences.
4. **Architecture discipline:** treat AI as part of enterprise design, with application, data, and algorithm responsibilities made visible.
5. **Adaptive framework and pipeline:** extend the author's adaptive enterprise architecture work with decision and algorithm domains.

These are motivations, interpretations, and anticipated benefits. The paper does not measure a reduction in harm, cost, project failure, or misunderstanding. An architecture diagram can clarify a responsibility while leaving the quality of its implementation unresolved.

## Broader enterprise architecture

VI discusses existing architecture frameworks, including Adaptive EA, TOGAF, Zachman, Federal EA, and EIRA. Gill argues for explicit attention to AI system architecture in this broader discipline. This is the author's 2024 framing; do not treat its assessment of frameworks as a current inventory of their 2026 capabilities. [VI, PDF pp. 11-12](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

Figure 4 presents Human-centric Adaptive EA Framework v5.0. The associated prose adds **decision architecture** in the human layer and **algorithm architecture** alongside application and data in the technology layer. The framework also discusses environmental factors, human interaction, business, information, social/professional domains, facilities, protection, and observability. These place AI in organizational surroundings instead of treating it as an isolated model.

The prose's reference to Figure 5 while discussing framework domains appears inconsistent with the displayed Figure 4 caption. Use the caption and the complete [map](05-paper-map.md) to navigate, and preserve this as a source cross-reference issue rather than silently renumbering the figures.

## The five-stage pipeline

Figure 5 and its accompanying text present an iterative pipeline. The summary below is an original paraphrase of that text. [VI, Figure 5, PDF p. 13](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

| Stage | Purpose in the source | Example artifact to prepare (companion suggestion) |
| --- | --- | --- |
| Initiate | Establish stakeholders' vision and scope for AI in decision making | A statement of the decision and who is affected |
| Discover | Specify the decision catalog and connected architecture at the chosen automation level | Decision record plus application/data/algorithm views |
| Implement | Develop the roadmap and incremental implementation plan | A staged delivery plan with explicit dependencies |
| Govern | Guide implementation against its intended design | Review criteria and named accountable reviewers |
| Adapt | Handle changes in architecture or implementation | A change record and reconsideration of assumptions |

The paper describes the stages as iterative. It does not supply a mandatory project management method, stage durations, or an experimentally optimized ordering. Its "Implement" discussion emphasizes roadmap/planning; a reader should not infer that a working implementation was built and evaluated in the paper.

## The research agenda

The closing questions concern switching conditions, each system's degrees of freedom, control flow and allocation, navigation, observability, information traceability, and interfaces. These are crucial open details: they expose what a future implementation must specify. [VI, PDF p. 13](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

For example, an escalation policy that always chooses deliberate analysis may consume too much time; one that almost never escalates may preserve fast mistakes. A controller needs a defensible policy and evidence about its tradeoffs. This example illustrates the unanswered problem; it is not a result reported by Gill.
