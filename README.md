# The Deal Team

**Twenty Claude agents, one for every job in a deal — from the first teaser to the IC memo.**

Built for searchers, independent sponsors and small funds who don't have a ten-person deal team behind them. Each agent has one job, a copy-ready prompt, and one rule running through all of them:

> **Every factual claim is cited back to the source it came from — or it gets cut before you ever see it.**

Most people use Claude to *summarise* a document. In a deal, the summary is the one thing you can't afford to trust — if it invents an EBITDA figure or quietly softens a customer-concentration risk, that's not a typo, it's a blown deal. So this pack is built the other way round: small, single-job agents that show their work and tell you when something they need is missing, rather than guessing.

These are the same diligence patterns that run inside [Deal OS](https://devaland.com) — open-sourced so you can run them yourself.

---

## The bench — 20 agents, 5 stages

The agents are ordered to follow a real deal. Feed the output of one into the next, and run the **Citation Checker** over any brief before you rely on it.

### I · Sourcing — *find the right businesses and start real conversations*
| # | Agent | Does |
|---|-------|------|
| 01 | [Deal Scout](skills/deal-scout/SKILL.md) | Builds a focused list of acquisition targets that fit your thesis |
| 02 | [Thesis Builder](skills/thesis-builder/SKILL.md) | Sharpens a vague "I want to buy a business" into a precise, testable thesis |
| 03 | [Outreach Writer](skills/outreach-writer/SKILL.md) | Owner-direct outreach that gets replies without sounding like a broker |
| 04 | [Teaser Requester](skills/teaser-requester/SKILL.md) | The note that gets an owner or broker to share the teaser or financials |

### II · Screening — *decide fast what's worth your time*
| # | Agent | Does |
|---|-------|------|
| 05 | [Teaser Analyzer](skills/teaser-analyzer/SKILL.md) | Reads a teaser and tells you what's really being sold |
| 06 | [Quick-Screen Scorer](skills/quick-screen-scorer/SKILL.md) | Scores a deal against your thesis in minutes so you can pass fast |
| 07 | [Red-Flag Scanner](skills/red-flag-scanner/SKILL.md) | Hunts for the early warning signs that kill deals later |
| 08 | [Go / No-Go Agent](skills/go-no-go-agent/SKILL.md) | Forces a clean decision so you don't drift into dead deals |

### III · Diligence — *read the deal properly, every claim cited*
| # | Agent | Does |
|---|-------|------|
| 09 | [CIM Reader](skills/cim-reader/SKILL.md) | Reads a full CIM and produces a cited, plain-English brief |
| 10 | [Financials Analyst](skills/financials-analyst/SKILL.md) | Turns the financials into plain-English signal and red flags |
| 11 | [Customer-Concentration Agent](skills/customer-concentration-agent/SKILL.md) | Stress-tests revenue quality and customer risk |
| 12 | [Market Sizer](skills/market-sizer/SKILL.md) | Sanity-checks the market story a seller tells |
| 13 | [Citation Checker](skills/citation-checker/SKILL.md) | Audits any AI or analyst summary back against the source |

### IV · Valuation — *frame a price with the logic shown, not false precision*
| # | Agent | Does |
|---|-------|------|
| 14 | [Comps Finder](skills/comps-finder/SKILL.md) | Frames a valuation range using comparable logic |
| 15 | [LBO Sketcher](skills/lbo-sketcher/SKILL.md) | Sketches whether the deal works on leverage, roughly |
| 16 | [Multiple Sanity-Checker](skills/multiple-sanity-checker/SKILL.md) | Catches when you're about to overpay |

### V · Process & Close — *run a tight process from question list to signed memo*
| # | Agent | Does |
|---|-------|------|
| 17 | [Question-List Builder](skills/question-list-builder/SKILL.md) | Writes the diligence question list you'd have forgotten |
| 18 | [Management-Meeting Prep](skills/management-meeting-prep/SKILL.md) | Gets you ready to run a sharp management meeting |
| 19 | [IC Memo Writer](skills/ic-memo-writer/SKILL.md) | Turns your diligence into a clean investment-committee-style memo |
| 20 | [Data-Room Tracker](skills/data-room-tracker/SKILL.md) | Keeps the closing process organised so nothing slips |

---

## How to use them

Each agent is a single `SKILL.md` with a copy-ready prompt. Two ways to run it:

**1. Copy-paste (no setup).** Open [claude.ai](https://claude.ai), copy the prompt from any agent's `SKILL.md`, paste it as your first message, then attach or paste the deal (teaser, CIM, P&L, your thesis). For an agent you'll reuse, create a Claude Project and paste the prompt into the project's custom instructions — then every chat in that project *is* that agent.

**2. Install as Claude skills.** Each folder under `skills/` is a self-contained Claude skill. Drop the ones you want into your skills directory (e.g. `~/.claude/skills/` for [Claude Code](https://claude.com/claude-code), or your Claude.ai skills) and Claude will reach for the right agent when you describe what you're doing.

```bash
git clone https://github.com/MariusGithub13/open-deal-team.git
cp -r open-deal-team/skills/* ~/.claude/skills/
```

### The one habit that makes this work
When an agent gives you a number that matters, **check the citation it points to.** Every figure should trace back to a line in your document. If it can't, treat it as unverified. That single habit is the difference between *using* AI on a deal and *trusting* it.

---

## See it run on a live deal

These prompts give you the diligence *discipline*. [Deal OS](https://devaland.com) is the same discipline as a product — citations verified against the source automatically, contradictions flagged across a whole data room, briefs you can hand to an IC.

**→ Here's a real, source-cited brief on a live deal: https://os.devaland.com/sample-brief**

---

## One honest note

These agents are analytical tools to speed up your own judgement and help you read deals faster. They are **not** investment, legal, tax or accounting advice, and they don't replace your own verification or your advisers. Always check an agent's output against the source documents — which is exactly what the cited rule is designed to let you do.

## License

[MIT](LICENSE) — use them, fork them, adapt them to your own thesis. Compiled by Marius Andronie · [Devaland · Deal OS](https://devaland.com).
