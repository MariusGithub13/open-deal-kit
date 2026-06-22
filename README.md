# The Deal Kit

**The complete Claude kit for buying a business. 100+ prompts, 50+ skills, 20 agents and 4 systems, for every stage of an acquisition, from the first teaser to the day you sign.**

Built for searchers, independent sponsors and small funds who don't have a ten-person deal team behind them. You're not outgunned on capital, you're outgunned on people: the seller has advisors who built the CIM to look its best, and you have you, a highlighter, and a deadline. This kit is the next best thing to a deal team.

> **One rule runs through all of it: every factual claim is cited back to the page it came from, or it gets cut before you ever see it.**

Most people use Claude to *summarize* a document. In a deal, the summary is the one thing you can't afford to trust, if it invents an EBITDA figure or quietly softens a customer-concentration risk, that's not a typo, it's a blown deal. So this kit is built the other way round: tools that show their work, cite their source, and tell you when something they need is missing rather than guessing. It's the same thinking that runs inside [Deal OS](https://devaland.com), open-sourced so you can run it yourself.

---

## The kit, in four parts

| | Part | What it is |
|---|------|------------|
| **I** | [The Prompt Library](prompts/) | **100+ prompts**, copy-paste, for every deal moment: thesis, CIM, financials, teasers, data room, red flags, valuation, questions and close. |
| **II** | [The Diligence Skills](skills/) | **50+ named tools**, one job each, across financial, red-flags, commercial, process-legal and decision. |
| **III** | [The Deal Team](agents/) | **20 agents**, one for every job in a deal, sourcing to close, each an installable skill with a copy-ready prompt. |
| **IV** | [The Systems](systems/) | **4 systems** that tie it together: the Cited Brief System, the Quick-Screen Scorecard, the Diligence Question Bank and the IC Memo Builder. |

**What's the difference?** Prompts are what you ask in the moment, copy, paste, go. Skills are named tools for one recurring job. Agents are roles you set up once and reuse across a deal. Systems tie it all together into a repeatable method. Use them in any combination.

The flagship is the **[Cited Brief System](systems/cited-brief-system/SKILL.md)** paired with the **[Citation Checker](agents/citation-checker/SKILL.md)**: produce a fully-cited brief on a deal, then audit it back against the source so nothing unverifiable reaches your decision. Start there.

---

## How to use it

**1. Copy-paste (no setup).** Open [claude.ai](https://claude.ai), grab any prompt (from the [prompt library](prompts/), an [agent](agents/), or a [system](systems/)), paste it as your first message, then attach or paste the deal (teaser, CIM, P&L, your thesis). For anything you'll reuse, create a Claude Project and paste the prompt into the project's custom instructions, then every chat in that project *is* that agent.

**2. Install as Claude skills.** Every agent and system is a self-contained Claude skill. Drop the ones you want into your skills directory (e.g. `~/.claude/skills/` for [Claude Code](https://claude.com/claude-code)) and Claude reaches for the right one when you describe what you're doing.

```bash
git clone https://github.com/MariusGithub13/open-deal-kit.git
cp -r open-deal-kit/agents/*  ~/.claude/skills/
cp -r open-deal-kit/systems/* ~/.claude/skills/
```

### The one habit that makes this work
When a tool gives you a number that matters, **check the citation it points to.** Every figure should trace back to a line in your document. If it can't, treat it as unverified. That single habit is the difference between *using* AI on a deal and *trusting* it.

---

## From a kit to a product

This kit gives you the *discipline*, a prompt you run yourself, one document at a time, checking each citation by hand. That's genuinely most of the value, and it's free. Use it and never pay anyone a cent.

[Deal OS](https://devaland.com) is the same discipline enforced automatically, at the scale of a real data room:

| The kit (this repo) | Deal OS |
|---|---|
| You paste one document and run one tool at a time | Reads a whole data room at once |
| Each tool cites its source; you verify by hand | Every citation is verified against the source automatically, unverifiable claims discarded before you see them |
| Contradictions surface only if you run the Citation Checker over each pair yourself | Contradictions flagged across every document at once |
| The output is a chat you copy out | Briefs you can export for an IC or lender, with an auditable trail of what was verified vs held back for your call |

If you only ever use the kit, that's a win, it's yours, MIT, forever. If you're running more than one deal at a time and the by-hand checking stops scaling, that's where the product earns its place.

**→ See it on a live deal, a real, source-cited brief: https://os.devaland.com/sample-brief**

---

## One honest note

This kit is a set of analytical tools to speed up your own judgment and help you read deals faster. It is **not** investment, legal, tax or accounting advice, and it doesn't replace your own verification or your advisers. Always check the output against the source documents, which is exactly what the cited rule is designed to let you do.

## License

[MIT](LICENSE), use it, fork it, adapt it to your own thesis. Compiled by Marius Andronie · [Devaland · Deal OS](https://devaland.com).
