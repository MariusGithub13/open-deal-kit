# Contributing

These agents come from running real deals. If you've improved one, or built a new agent that earns its place on the bench, contributions are welcome.

**The one rule.** Every agent in this pack enforces the same discipline: *a factual claim about the deal is cited to its source, or it gets cut.* A contribution that lets an agent assert numbers it can't trace won't be merged. Keep agents narrow (one job), honest (they say "not stated" instead of guessing), and grounded (they ask for missing inputs rather than inventing them).

**To add or change an agent**
1. Each agent lives in `agents/<slug>/SKILL.md` with YAML frontmatter (`name`, `description`) and a copy-ready prompt. Systems live in `systems/<slug>/SKILL.md`; prompts and the skills catalog are in `prompts/` and `skills/`.
2. Keep the structure consistent with the existing agents: role, when-to-use, what-you-get-back, the prompt, the cited rule, the honest-note disclaimer.
3. If you add an agent, add it to the bench table in `agents/README.md` (and the main `README.md` if it changes the kit overview).
4. Open a PR describing the deal situation it's for and what it returns.

**Not legal/financial advice.** Agents here are analytical tools, not investment, legal, tax or accounting advice. Contributions should preserve that framing.

**Checks.** `python3 tests/check_kit.py` runs on every push: each agent and system has `name` and `description`
front matter, every relative link resolves, the README's counts (20 agents, 4 systems, 100+ prompts, 50+ skills)
still hold, and the one Python example compiles. Run it before opening a PR; it needs nothing installed.

**Reporting a wrong output.** Open an issue with the agent or system you used, the prompt exactly as you pasted it,
the passage of the document it read (redacted as you need), the output, and the claim that had no page behind it
or cited the wrong one. A fabricated figure that slipped through is the report that matters most.
