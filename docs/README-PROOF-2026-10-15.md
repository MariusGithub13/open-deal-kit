# README proof, 15 October 2026

Everything the README asks a reader to run, run on a clean clone of `main` (commit `e6fefa3`) in a cloud
container: Ubuntu 24.04, Python 3.13.16, outbound network limited to a short allow-list. The kit is prose, so
most of what can be checked is that the files, counts, front matter and links are what the README says they are.

Legend: **passed** means it ran and matched. **not run here** means the container lacks something it needs,
with the reason. **not verified here** means a link the container was not allowed to reach. Nothing below is
inferred; every output line was produced in this session.

## The install commands

```bash
git clone https://github.com/MariusGithub13/open-deal-kit.git
cp -r open-deal-kit/agents/*  ~/.claude/skills/
cp -r open-deal-kit/systems/* ~/.claude/skills/
```

**Failed as written on a fresh home directory**, passed with one extra line:

```
$ cp -r open-deal-kit/agents/* ~/.claude/skills/        (HOME with no .claude/skills yet)
cp: target '/tmp/tmp.W0sVIRLh04/.claude/skills/': No such file or directory
[exit 1]
$ mkdir -p ~/.claude/skills && cp -r open-deal-kit/agents/* ~/.claude/skills/ && cp -r open-deal-kit/systems/* ~/.claude/skills/
25 entries: the 24 skill folders plus one README.md (systems/README.md written over agents/README.md)
$ mkdir -p ~/.claude/skills && cp -r open-deal-kit/agents/*/ ~/.claude/skills/ && cp -r open-deal-kit/systems/*/ ~/.claude/skills/
24 entries, 0 README.md, each folder holds its SKILL.md
```

README corrected: `mkdir -p ~/.claude/skills` added, `*` became `*/`.

## The counts on the first line of the README

| README says | Counted | How |
|---|---|---|
| 100+ prompts | 103 | numbered items in `prompts/README.md` (8 + 20 + 19 + 10 + 10 + 13 + 11 + 12) |
| 50+ skills | 52 | table rows in `skills/README.md` (12 + 12 + 10 + 10 + 8) |
| 20 agents | 20 | `agents/*/SKILL.md` |
| 4 systems | 4 | `systems/*/SKILL.md` |

All 24 `SKILL.md` files open with front matter carrying `name` and `description`. 65 relative links across
every Markdown file resolve. `grep` finds no em dash in the README or any skill file, as the 21 June
changelog entry says. These checks are now `tests/check_kit.py`, run by the workflow on every push:

```
$ python3 tests/check_kit.py
20 agents, 4 systems, 103 prompts, 52 skills, 65 relative links checked
OK
[exit 0]
```

## Every external link, in the README and in the agents' files

Fetched with `curl -L` from the container and, where that was refused, through the session's web fetch tool.

| URL | In | Result |
|---|---|---|
| https://github.com/MariusGithub13/open-deal-kit.git | README | **200**, the repository page |
| https://claude.com/claude-code | README | **200**, the product page |
| https://claude.ai | README | **403** to a non-browser client, with the bot-check page ("Just a moment..."); a browser gets the site. Not dead |
| https://devaland.com | README (3 times) | **not verified here**: the egress proxy refuses the host (`CONNECT tunnel failed, response 403`), and the web fetch tool cannot resolve it |
| https://os.devaland.com/sample-brief | README, the four index READMEs, all 20 agent files, all 4 system files | **not verified here**, same reason. This is the repository's homepage and the kit's one demonstration link, so it is the first thing to check from a normal network |
| https://os.devaland.com/static/sample-sources/ and the four `Sentinel_*.pdf` files | `examples/typed-refusal-gate/` | **not verified here**, same reason |
| https://github.com/GrayWolfOne21/typed-refusal | `examples/typed-refusal-gate/` | **exists** (web fetch tool): description "Fail-closed typed refusal contract...", MIT, 4 commits, no release named v0.1.1. `curl` from the container got 403 from the proxy |

Dead links found: **none**. Links not verifiable from this session: the Devaland ones above. No link was
changed.

## `examples/typed-refusal-gate/`

```
$ pip install "git+https://github.com/GrayWolfOne21/typed-refusal@892b0a0"
Successfully installed typed-refusal-0.1.0
[exit 0]
$ python3 -c "from typed_refusal import Contract, FieldRule, evaluate; from typed_refusal.contract import Source; from typed_refusal.gate import seal"
imports ok
$ python3 gate_sentinel.py
urllib.error.URLError: <urlopen error Tunnel connection failed: 403 Forbidden>
[exit 1]
```

The install **passed** (pip reaches GitHub through the git proxy). The package at the pinned commit reports
version 0.1.0 while the example calls it v0.1.1; the typed-refusal repository has no releases, so "v0.1.1" is the
label the two authors use for that commit. Left as written, noted here. The script itself is **not run here**:
its first step downloads the four PDFs from `os.devaland.com`, which the container cannot reach. The committed
`receipt.json` reads `status DATA_NULL`, `brief_written false`, two `not_ready` and three `data_null` fields, and
all five seal checks `true`, which is what the example README's table says.

## Claims checked by reading

| Claim | Result |
|---|---|
| Each agent is "an installable skill with a copy-ready prompt" | 20 of 20 have front matter and a prompt section |
| The flagship pair, Cited Brief System and Citation Checker, exists at the paths given | both files present |
| MIT licence | `LICENSE` |
| The changelog's version history for the Cited Brief System | dates and version numbers consistent between `CHANGELOG.md` and the skill file |
| "Twenty Claude agents", the GitHub description | 20 folders |

Not checkable here: anything about what the prompts produce when run against a deal. Nothing of that kind was
added to the README.

## What changed in the README, and why

1. `mkdir -p ~/.claude/skills` before the two `cp` lines: without it the install fails on a fresh machine.
2. `agents/*` and `systems/*` became `agents/*/` and `systems/*/`: the bare glob also copies the two index
   READMEs into the skills directory, one over the other.
3. One paragraph saying what the check script verifies and pointing to this document.

Nothing else was changed. `CONTRIBUTING.md` gained two paragraphs (how to run the check, how to report a wrong
output with the input that produced it); the author's text above them is untouched. `SECURITY.md` is new.
