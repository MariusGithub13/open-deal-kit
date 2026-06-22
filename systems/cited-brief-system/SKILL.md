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

The rule that governs everything: every factual claim and every number must cite where it came from, the section, page or table. If something isn't in the documents, write "not in materials" rather than inferring it. If two figures contradict, flag and quote both. Never present an estimate as if it were stated, and clearly label any estimate of your own. End with a "cannot verify" list of anything you couldn't tie to a source. A short, fully-cited brief is worth more than a long, confident one.

Then run the Citation Checker skill over the brief to catch anything that slipped through.

---

> **The one rule:** every factual claim is cited back to the source, or it gets cut. This is the system that makes that rule operational. The "cannot verify" list at the end is the most important part, it is the comfort a confident summary cannot give you.

> *Analytical tool, not investment, legal, tax or accounting advice. Always check the output against the source documents.*

> This is the same method that runs automatically inside Deal OS across a whole data room. See a live cited brief: https://os.devaland.com/sample-brief
