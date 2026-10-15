#!/usr/bin/env python3
"""The kit is prose, so this checks what prose can be checked: every agent and system is a skill file with
`name` and `description` front matter, every relative link resolves, the README's counts hold, and the one
Python example compiles. It asks no model and needs nothing installed."""
import glob, os, py_compile, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errors = []


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return {}
    head = text[4:].split("\n---", 1)[0]
    return dict(line.split(":", 1) for line in head.splitlines() if ":" in line)


agents = sorted(glob.glob("agents/*/SKILL.md"))
systems = sorted(glob.glob("systems/*/SKILL.md"))
for f in agents + systems:
    fm = frontmatter(f)
    for key in ("name", "description"):
        if not fm.get(key, "").strip():
            errors.append(f"{f}: front matter has no {key}")
if len(agents) != 20:
    errors.append(f"README says 20 agents, found {len(agents)}")
if len(systems) != 4:
    errors.append(f"README says 4 systems, found {len(systems)}")

prompts = len(re.findall(r"^\d+\. ", open("prompts/README.md", encoding="utf-8").read(), re.M))
if prompts < 100:
    errors.append(f"README says 100+ prompts, prompts/README.md numbers {prompts}")
rows = re.findall(r"^\| ([^|]+) \| [^|]+ \|$", open("skills/README.md", encoding="utf-8").read(), re.M)
skills = [r for r in rows if r.strip() not in ("Skill",) and not r.startswith("-")]
if len(skills) < 50:
    errors.append(f"README says 50+ skills, skills/README.md lists {len(skills)}")

links = 0
for f in glob.glob("**/*.md", recursive=True):
    for m in re.finditer(r"\]\(([^)]+)\)", open(f, encoding="utf-8").read()):
        target = m.group(1).split()[0].split("#")[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        links += 1
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), target))):
            errors.append(f"{f}: dead relative link {m.group(1)}")

try:
    py_compile.compile("examples/typed-refusal-gate/gate_sentinel.py", doraise=True)
except py_compile.PyCompileError as e:
    errors.append(str(e))

print(f"{len(agents)} agents, {len(systems)} systems, {prompts} prompts, {len(skills)} skills, {links} relative links checked")
for e in errors:
    print("FAIL", e)
print("OK" if not errors else f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
