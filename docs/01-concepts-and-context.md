# 1. Concepts and context

[Home](../README.md) · [Next: framework](02-framework-and-architecture.md) · [Source map](05-paper-map.md)

## Begin with a decision

The paper's research question concerns the **conceptual design of AI architecture**. It is narrower than asking which AI model is most accurate and broader than choosing an API. Gill starts from decisions that involve alternatives, resources, judgments, uncertainty, and possible harm. An enterprise can acquire an impressive model while still failing to identify who needs a decision, when it is needed, or what would count as an acceptable outcome. [I-II, PDF pp. 2-3](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

Decision quality and realized outcomes are different. A reasonable choice can have an unfavorable outcome under uncertainty. Conversely, a lucky outcome does not prove the decision process was good. The source uses this distinction to motivate deliberate requirements work rather than a promise that AI can control every outcome. It also discusses strategic, tactical, and operational decisions; these categories describe organizational scope, not the same thing as the fast/slow/control roles.

The paper connects human-centered design to the whole system: decision framing, authority, bias, application interactions, data, and algorithms. A friendly interface alone would not address these concerns. This is the guide's interpretation of how the argument develops from II to IV, rather than a measured finding.

## Fast and slow as architectural vocabulary

Gill adapts **Daniel Kahneman's** _Thinking, Fast and Slow_ [8]. In the paper's account, System 1 is automatic, associative, intuitive, and capable of rapid pattern recognition. Familiarity lets it respond with little deliberate effort. That same economy can encourage premature conclusions and systematic errors. System 2 is effortful, attentive, evaluative, and deliberate. It can compare alternatives and perform complex analysis, but attention and effort have limits. [III.A-B, PDF pp. 4-5](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

| Role | Useful question when designing software | Caution |
| --- | --- | --- |
| Fast / intuitive | What can a pattern-driven response handle promptly? | Speed or fluency does not establish correctness |
| Slow / rational | What requires explicit comparison, calculation, or additional evidence? | More processing can still rationalize a bad assumption |
| Control | Who observes, allocates authority, and handles escalation? | A control component can itself be wrong or biased |

The questions are original teaching prompts. The source does not specify a latency threshold that separates fast from slow, a universal model class for each role, or an algorithm that identifies the right mode. Do not equate every neural model with System 1 or every rule-based program with System 2 across all uses. In IV.B, the paper classifies some LLM uses as intuitive and complex decision support as rational; these are architectural examples.

## Why propose control?

The source argues that local self-control is not necessarily control of the whole system. If one role passes work too late, dominates the other, or inherits a flawed frame, a fast/slow pair can remain poorly coordinated. Gill therefore proposes System 3 to regulate interfaces, data exchange, feedback, and the allocation of control. [III.C, PDF p. 5](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

Several intellectual lenses support the argument:

- **Principal-agent theory [17]:** delegated action can involve differences between the principal's interests and the agent's behavior. The architecture needs explicit responsibility and contracts.
- **Homeostasis [20]:** maintaining balance motivates regulation as an analogy. A software system does not inherit biological stability merely by using this analogy.
- **Control theory [21]:** observability, feedback, and stability motivate questions about system behavior. The paper does not derive a controller or prove stability.
- **Neil D. Lawrence [22]:** the discussion of human intelligence and the control of cognitive capability motivates attention to coordination.
- **Herbert A. Simon [29-30]:** bounded rationality supports treating time, knowledge, and resources as constraints on deliberation.

The paper's rhetorical claims that control is needed should be read as reasons for a design proposal. The v1 source provides no comparison demonstrating that a separate controller is necessary for every decision system.

## Glossary

| Term | Meaning in this guide |
| --- | --- |
| Trimodal thinking | Gill's proposed fast, slow, and control framing for conceptual architecture |
| Human-centric | Start with human decision needs, limits, and accountability |
| Decision requirement | What a particular decision process needs to accomplish and under what constraints |
| Application architecture | Actors, interfaces, applications, agents, and environment |
| Data architecture | Actors, interfaces, data systems, and the data they manage |
| Algorithm architecture | Processing logic, input, output, and resulting model/product |
| Observability | Ability to obtain evidence about internal behavior and interactions; not a safety guarantee |
| Automation level | An allocation of decision work and intervention between people and AI |
| Enterprise architecture | A broader organizational and technical design context |

## Check your understanding

Explain why a delayed escalation can be an architectural problem even when both the fast and slow components are accurate on their own tests. Then distinguish the paper's proposed solution from evidence that it succeeds. Continue to [module 2](02-framework-and-architecture.md).
