# 6. Discussion and design exercises

[Home](../README.md) · [Previous: source map](05-paper-map.md) · [Evidence boundaries](04-evidence-and-limitations.md)

## Worked example: routing equipment-service requests

**This entire example is original companion teaching material. It was not implemented or evaluated by Gill or by this repository.** It illustrates how to use the proposed vocabulary without claiming benefits in advance.

A service team receives equipment fault reports. A familiar low-risk report may allow a routine response; an unusual report may require an engineer's investigation. Incorrect advice can damage equipment, so some actions require explicit human approval.

| Decision element | Example design choice |
| --- | --- |
| Context and domain | An internal equipment-service desk |
| Decision maker and frame | The service lead owns escalation; the question is which investigation path to take |
| Alternatives | Routine instructions, additional evidence, specialist review, immediate shutdown request |
| Time, cost, criticality | Response time matters, but risk can justify additional delay |
| Information and logic | Current report, service history, and a documented escalation policy |
| Preferences and outcome | Safe restoration of service with traceable responsibility |
| Limitations, risks, biases | Incomplete reports, unfamiliar devices, overconfidence in frequent fault categories |
| Automation level | Semi-automated routing with consequential actions approved by a person |

The table groups all 16 source decision elements for teaching. The source supplies the checklist, not these choices. [IV.A/Table I, PDF p. 7](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

## Assign responsibilities across the views

**Fast role:** suggest a familiar category using the report. **Slow role:** compare history and constraints when the case is unusual or ambiguous. **Control role:** enforce escalation boundaries, record the evidence and mode selection, and transfer the case to a person when required. These are proposed responsibilities for this example, not proven mappings from a particular model technology to human cognition.

In the application view, identify the requester, interface, triage application, processing agents, and service environment. In the data view, record which histories and device records are accessible, how updates arrive, and what the downstream reviewer actually sees. In the algorithm view, identify the classifier or model, input representation, recommendation output, and versioned processing logic. [IV.C-E, PDF pp. 8-10](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

A subtle failure would be passing only the fast role's proposed category to the slow role. The slow process might then analyze the wrong frame thoroughly. A design could instead preserve the original report and show the tentative category as a hypothesis. This is an original failure scenario to investigate, not an observed trimodal failure.

## Use the pipeline

Initiate by agreeing on the decision and stakeholders. Discover by completing the catalog and architecture views. Implement through a roadmap that begins with human-reviewed suggestions. Apply governance across this work using criteria tied to the original requirements, and adapt whenever devices, report types, or policies change. Figure 5's Govern & Adapt arrow spans all three panels; these are not steps postponed until after implementation. These actions illustrate the source's five iterative responsibilities, without treating the pipeline as validated project management. [VI/Figure 5, PDF p. 13](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

## What an evaluation would need

There is no experiment to replicate directly from v1. A future evaluation would first operationalize the conceptual roles, then compare clearly specified designs.

1. Define a task and an accountable decision owner. Specify the harms, permitted actions, and escalation boundary.
2. Implement the fast, slow, and control responsibilities with enough detail to reproduce them. Record what each process can observe and change.
3. Choose comparison systems. For example, compare a fixed workflow with and without the proposed control policy while accounting for differences in compute, evidence, and human attention.
4. Fix evaluation data and assess representative difficult cases, including incomplete evidence, conflicting recommendations, and controller failures.
5. Measure more than correctness: delay, resources, escalation usefulness, human intervention, and relevant harm indicators may matter. Define denominators and uncertainty before inspecting outcomes.
6. Test whether changes follow from the control policy rather than extra compute, extra evidence, or different human review.
7. Report limits and negative results, including any tradeoff between speed and decision quality.

This is a **companion research proposal**. No measurements, sample sizes, thresholds, or success rates are supplied or implied.

## Discussion prompts

- Does every design need a separate control component, or can control responsibilities be distributed? What would distinguish these empirically?
- How would the system detect that the original decision frame was wrong?
- Can a person intervene in time, or does "human in the loop" merely describe a nominal interface?
- How will the controller be monitored without assuming an endlessly reliable hierarchy of controllers?
- Which parts of an architecture explanation help users understand decisions, and which require separate user research?
- How should disagreements between stakeholders be represented rather than hidden in a single preference score?

Answer with the [claim types](../metadata/claims.json) in mind: a design question or hypothetical example is not a reported result.
