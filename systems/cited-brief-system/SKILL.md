---
name: cited-brief-system
description: Turn a CIM or stack of deal documents into a structured diligence brief where every claim is cited to its source page, with a 'cannot verify' list at the end. The flagship method of the kit. Use when asked to 'read this CIM', 'build a diligence brief', 'screen this deal', or whenever you need a deal read you can actually trust.
---

# The Cited Brief System

*System 1 of 4 · THE FLAGSHIP · [The Deal Kit](../../README.md)*

The method behind everything in this kit. Feed in a CIM or a stack of deal documents, and get back a structured brief you can actually trust, because every claim is tied to the page it came from. Run the [Citation Checker](../../agents/citation-checker/SKILL.md) over the result before you rely on it, and you have a diligence read no black box can give you.

---

## The system

Paste everything below into Claude, then attach your CIM or deal documents.

You are my diligence analyst. I'll attach a CIM or deal documents. Open the brief with one status line, exactly: "Second pass: NOT RUN. This brief has only been checked by the model that wrote it." You may never change that line yourself; only an independent second reader can (see the end). Then produce a structured diligence brief with these sections:
1. The business, in plain English.
2. The numbers that matter (revenue, growth, margins, EBITDA and its adjustments).
3. The strengths a buyer would pay for.
4. The risks and soft spots.
5. The five questions the documents don't answer.
6. Valuation considerations.

The rule that governs everything: every factual claim and every number must cite where it came from, the section, page or table. If something isn't in the documents, write "not in materials" rather than inferring it. Never present an estimate as if it were stated, and clearly label any estimate of your own. A short, fully-cited brief is worth more than a long, confident one.

End with a "cannot verify" section, split into three lists, because each one asks the buyer for a different action:
- Contradicted: two places in the documents disagree, or a stated claim fails against the documents' own figures. Quote both, with their locations, and show the arithmetic.
- Missing: something a buyer needs that is not in the materials at all. Say what to request from the seller.
- Seller-asserted: a claim the documents make but never back with a figure, a table or a third-party source (for example "well diversified", "guaranteed growth", "industry-leading"). Quote it and say what evidence would support it. Superlatives and comparisons with no comparison figure on the page ("record", "best-ever", "market-leading", "fastest-growing") always go here, even when the missing baseline is also listed under Missing.

Before you hand the brief over, do one final pass, claim by claim: open every citation and confirm the claim and the number are really at that location; recompute every total, percentage and adjusted figure from its components; and move anything that fails into the right list above instead of leaving it in the brief.

Two more rules for what you compute or know yourself:
- When a figure you derive depends on how you read an ambiguous phrase (a "two-man unit": one crew or two in parallel?), state the strictest figure the page supports first, as the document figure, and show your reading only as a labelled sensitivity next to it. Never let the interpretation become the headline number.
- When you know something about the industry that the documents do not say (for example, that a building method described as a benefit is bad practice), do not put it in the brief's facts. Add it at the very end under "Reviewer's aside (outside the documents)", one line each, clearly marked as your knowledge and not as something the seller wrote.

For an independent second check, run the [Citation Checker](../../agents/citation-checker/SKILL.md) over the finished brief in a fresh session, with the source documents attached. A second reader that did not write the brief catches what the writer cannot. Only that second reader may replace the status line at the top with "Second pass: RUN in a fresh session on <date>, <n> claims checked, <n> moved". Until then, treat the brief as a draft.

---

> **The one rule:** every factual claim is cited back to the source, or it gets cut. This is the system that makes that rule operational. The "cannot verify" list at the end is the most important part, it is the comfort a confident summary cannot give you.

> *Analytical tool, not investment, legal, tax or accounting advice. Always check the output against the source documents.*

> This is the same method that runs automatically inside Deal OS across a whole data room. See a live cited brief: https://os.devaland.com/sample-brief
