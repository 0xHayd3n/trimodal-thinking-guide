# 4. Evidence, limitations, and provenance

[Home](../README.md) · [Previous](03-patterns-and-pipeline.md) · [Next: complete map](05-paper-map.md)

## What kind of paper is this?

The studied v1 is an exploratory, purpose-driven review and conceptual proposal. It adapts ideas from decision science and related theories to organize AI architecture. The abstract's language about demonstrating use refers to conceptual application through architecture diagrams, classifications, tables, and a pipeline. It does not describe a controlled experiment. [Abstract and VI, PDF pp. 1-2, 10-13](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

The source contains no original empirical results section, recruited sample, benchmark protocol, trained trimodal system, experimental comparison, statistical test, or measured deployment outcome. No such result is added in this repository. The structured [claims](../metadata/claims.json) mark proposals and arguments rather than inventing an accuracy, cost, or fairness leaderboard.

## What the argument supports

It supplies a coherent vocabulary for asking who decides, what information is exchanged, and how fast/slow processes might be coordinated. It also gives requirements elements and architecture views that readers can use to organize a design review. This establishes what the author proposes and how he connects the ideas. It does not establish that using the proposal improves a system compared with alternatives.

| Overstatement to avoid | Source-grounded formulation |
| --- | --- |
| System 3 eliminates bias | Gill proposes a control role intended to monitor and mitigate bias |
| Trimodal systems are more accurate or efficient | The source motivates this architecture but does not measure that comparison |
| Humans have a proven independent third thinking system | The paper proposes System 3 for conceptual architecture using several theoretical lenses |
| The pipeline reduces AI project failures | Reduced waste is an expected benefit requiring future evidence |
| An autonomous system removes human accountability | The source explicitly retains human accountability for decisions and outcomes |
| Software classification proves human-like intelligence | The source uses human decision making as a design lens, not a cognitive equivalence test |

## The project-failure statistic

VI cites RAND [36] when motivating economic value and mentions more than 80% project failure. This is an external background assertion, not a sample or outcome measured by Gill. This guide does not independently validate the figure, denominator, or causal interpretation. Do not subtract it from a hypothetical trimodal success rate, describe it as the paper's experiment, or use it as evidence that the framework prevents failure. [VI, PDF p. 11; reference 36, PDF p. 15](https://doi.org/10.36227/techrxiv.173153092.25969269/v1)

## Open implementation questions

- **Controller reliability:** who monitors control decisions and handles a biased or unavailable control process?
- **Operational criteria:** how are switching, intervention, disagreement, and acceptable delay defined?
- **Measurement:** what observable signals correspond to stability, bias, decision quality, or meaningful human control?
- **Conflicting goals:** which stakeholder's preferences dominate when objectives differ?
- **Interface losses:** what information is dropped, transformed, or incorrectly summarized between roles?
- **Boundary cases:** when is a distinct control component helpful, and when can responsibilities be embedded in another design?

These are companion analysis questions informed by III.C and the closing research agenda. They are not failures observed in an evaluated trimodal implementation.

## Source and version boundaries

The actual attached **v1.pdf**, Library identifier `libfile_f09aa41527648191a79175c41740225a`, was read in full: 16 PDF pages, including the cover, manuscript, references, and biography. The readable content pins the title, author, TechRxiv v1 DOI, posting date, and CC BY 4.0 notice. The same author is named Asif Gill in the title and Asif Q. Gill in the biography. The source's posting date and manuscript-header date differ; both are retained. [Paper metadata](../metadata/paper.json)

The source is **not substituted** with the later IEEE journal article. Public search identifies a later publication, but its pagination and wording are outside this guide's studied version. Public TechRxiv access encountered a site challenge during preparation. The Library byte-download helper also failed at Windows extended-attribute handling; no binary digest or public/attachment byte equality is asserted.

Library supplied complete page text, but several table rows were clipped at the right edge and page images were returned as asset pointers without viewable pixels in this environment. Therefore, figure discussion is grounded in captions and surrounding prose; **it is not a pixel-level inspection or a reconstruction of all diagram labels**. Table descriptions are original explanatory summaries, using readable labels and prose. These limits especially affect Table VI's detailed control wording and the rightmost descriptions in Tables II-IV and VII.

## Copyright and maintenance

Only original companion explanations and small bibliographic/structural identifiers are included. The paper PDF, full text, original tables/figures, and any source code are not redistributed. [ATTRIBUTION.md](../ATTRIBUTION.md) separates the paper's authorship and license from this guide.

Documentation checks can establish link, metadata, and citation consistency. They cannot establish conceptual validity, empirical effectiveness, current legal compliance, or the status of later framework versions. Recheck the exact primary source before revising a substantive claim.
