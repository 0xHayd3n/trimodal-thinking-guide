# 2. Framework and architecture

[Home](../README.md) · [Previous](01-concepts-and-context.md) · [Next: patterns](03-patterns-and-pipeline.md)

## The control role is a responsibility, not a supplied algorithm

Section III.C proposes monitoring and regulating the interaction between fast and slow processes. The paper discusses observing irregularities, managing power imbalance, sharing information, actuating a switch, and enabling feedback for adaptation. These describe intended responsibilities. They do not supply a trained router, a switching equation, a confidence cutoff, or an optimization objective. [III.C, PDF p. 5](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

A useful way to read the proposal is to ask what a control role would have to know: the current decision context, what evidence each process used, the consequences of waiting, and who can override the choice. These are companion design questions. An implementation would need to define them and evaluate its answers. Adding another agent is not, by itself, evidence of control.

## From human activity to architecture

IV opens with information processing and human memory as background [31-32]. It then moves through three conceptual steps: understand decision requirements; classify the AI roles needed; and design the connected application, data, and algorithm views. Figures 2-3 summarize this move. [IV, PDF pp. 5-7](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

The memory and sensory discussion is an analogy for identifying capabilities. The source does not specify a faithful cognitive simulation, an artificial emotional life, or a neural implementation of all human faculties. It explicitly cautions against attributing human emotional, physical, and spiritual needs to AI systems in IV.E.

## Decision requirements: the complete checklist

Table I supplies 16 elements for a decision catalog. The following restates their purpose as original questions; it does not reproduce the table descriptions. [IV.A, Table I, PDF p. 7](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

| Element | Question to resolve |
| --- | --- |
| Context | In what organizational, personal, or social setting is the choice made? |
| Domain | Which area of work supplies its meaning and constraints? |
| Cost | What effort or resources can the process consume? |
| Time | How soon must a useful response arrive? |
| Criticality | What depends on the choice, and how consequential is it? |
| Outcome | Which benefit is intended? |
| Decision maker | Who holds the decision responsibility? |
| Frame | What problem and goal are being defined? |
| Alternatives | Which feasible choices are actually available? |
| Preferences | Which priorities influence the comparison? |
| Information | What facts and evidence are available? |
| Decision logic | How are alternatives evaluated? |
| Limitations | What constraints or unknowns remain? |
| Risks | What harms could arise? |
| Biases | Which systematic distortions could influence the process? |
| Automation level | Which decisions remain manual, assisted, automated, or autonomous? |

Keep **outcome**, **logic**, and **accountability** separate. A system might rank choices using a score while the intended human outcome is harder to measure. A complete catalog should expose that gap rather than silently substitute the score for the goal. This is a companion interpretation, not a claim evaluated by the paper.

## Classification before implementation

IV.B/Table II groups systems into intuitive, rational, and control classes. Autopilot and pattern-oriented LLM behavior illustrate the intuitive class; decision support and recommendation illustrate the rational class; governance, quality control, monitoring, and observability illustrate control. [IV.B, PDF p. 8](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

These examples do not establish that an entire self-driving car belongs to just one class, that all recommendations are rational, or that governance can be reduced to a model call. Classify a specific **function in a decision context**, and then identify the interactions it needs. The source presents broad classes; this functional reading is the guide's practical interpretation.

## Application architecture

IV.C/Table III names five elements: **actor, interface, AI application, AI agent, environment**. An actor interacts through an interface; an application offers services and can contain multiple agents; the environment supplies context and changing inputs. Interfaces can include user interfaces, prompts, and APIs. [IV.C, PDF pp. 8-9](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

The principal-agent lens makes delegation explicit. A human principal assigns work to an agent under an agreed contract. In the paper's proposed arrangement, fast and slow agents perform decision work while control agents coordinate and monitor. This does not remove human responsibility or establish that an agent will obey a contract perfectly.

For a concrete design review, identify the principal, delegated action, allowed evidence, escalation path, and consequences of failure. These fields are an original exercise derived from the architecture discussion; they are not a prescribed contract schema in v1.

## Data architecture

IV.D/Table IV names **actor, interface, data system, data**. This view concerns collecting, managing, exchanging, and using information across the decision system. The text mentions warehouses, lakes, lakehouses, meshes, fabrics, exchanges, and other data arrangements as options. It does not benchmark or prescribe one of them. [IV.D, PDF p. 9](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

Control includes the exchange between fast and slow processing as well as data bias. A relevant design question is whether the deliberate process receives raw evidence or only a fast component's summary. A summary can preserve an early mistake; a control log that records only final outputs may fail to reveal it. This example is the guide's interpretation of the interfaces and observability problem.

## Algorithm architecture

IV.E/Table V names **algorithm, input, output, model**. The algorithm processes input; its outputs and resulting product/model are represented explicitly. The source lists supervised, unsupervised, reinforcement, deep, generative, symbolic, and neuro-symbolic approaches. These categories overlap and the paper does not compare their performance. [IV.E, PDF pp. 9-10](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

It also distinguishes training, validation, test, and live production data. These are general architecture considerations, **not datasets collected or evaluated for trimodal thinking**. A live system may change its operating conditions after deployment; representing production data separately helps expose that issue.

## Read the three views together

| View | What it makes visible | What it cannot establish alone |
| --- | --- | --- |
| Application | Who interacts, delegates, and acts | Whether the information is adequate |
| Data | Which information is available and exchanged | Whether the decision logic is suitable |
| Algorithm | How processing turns inputs into outputs | Whether the intended human outcome is achieved |

The next [module](03-patterns-and-pipeline.md) connects these views to automation choices. A complete architecture must resolve their boundaries together; v1 provides a conceptual decomposition rather than a ready-to-deploy specification.
