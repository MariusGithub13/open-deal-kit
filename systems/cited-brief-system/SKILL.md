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

You are my diligence analyst. I'll attach a CIM or deal documents. Produce a structured diligence brief with these sections:
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
- Seller-asserted: a claim the documents make but never back with a figure, a table or a third-party source (for example "well diversified", "guaranteed growth", "industry-leading"). Quote it and say what evidence would support it.

Before you hand the brief over, do one final pass, claim by claim: open every citation and confirm the claim and the number are really at that location; recompute every total, percentage and adjusted figure from its components; and move anything that fails into the right list above instead of leaving it in the brief.

For an independent second check, run the [Citation Checker](../../agents/citation-checker/SKILL.md) over the finished brief in a fresh session, with the source documents attached. A second reader that did not write the brief catches what the writer cannot.

---

> **The one rule:** every factual claim is cited back to the source, or it gets cut. This is the system that makes that rule operational. The "cannot verify" list at the end is the most important part, it is the comfort a confident summary cannot give you.

> *Analytical tool, not investment, legal, tax or accounting advice. Always check the output against the source documents.*

> This is the same method that runs automatically inside Deal OS across a whole data room. See a live cited brief: https://os.devaland.com/sample-brief
