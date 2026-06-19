# Contributing

These agents come from running real deals. If you've improved one — or built a new agent that earns its place on the bench — contributions are welcome.

**The one rule.** Every agent in this pack enforces the same discipline: *a factual claim about the deal is cited to its source, or it gets cut.* A contribution that lets an agent assert numbers it can't trace won't be merged. Keep agents narrow (one job), honest (they say "not stated" instead of guessing), and grounded (they ask for missing inputs rather than inventing them).

**To add or change an agent**
1. Each agent lives in `skills/<slug>/SKILL.md` with YAML frontmatter (`name`, `description`) and a copy-ready prompt.
2. Keep the structure consistent with the existing agents: role, when-to-use, what-you-get-back, the prompt, the cited rule, the honest-note disclaimer.
3. If you add an agent, add it to the bench table in `README.md`.
4. Open a PR describing the deal situation it's for and what it returns.

**Not legal/financial advice.** Agents here are analytical tools, not investment, legal, tax or accounting advice. Contributions should preserve that framing.
