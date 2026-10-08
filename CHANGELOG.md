# Changelog

All notable changes to The Deal Kit are recorded here.
Dates are the day the work landed on `main`.

The one rule the whole kit is built on does not change: **every factual claim is
cited back to the page it came from, or it gets cut before you ever see it.**

## Unreleased

### Added
- This changelog, so anyone arriving at the kit can see what moved and when
  rather than reading commit messages.

### Clarified
- **How the kit's "skills" relate to Anthropic's Agent Skills.** They are not the
  same thing, and the shared word causes confusion. A skill in this kit is a
  *named job written in prose*: you hand Claude one line, such as *"Act as the
  Add-Back Auditor and classify every EBITDA adjustment in the attached
  financials as legitimate, arguable or aggressive, with the reason and the
  page."* It needs no installation and works in any Claude surface.
  Agent Skills are a packaged, installable format that did not exist when this
  kit was first published. Packaging the diligence skills in that format is on
  the list, and until it is done, nothing here requires it.

## 2026-10-08 (later the same day)

### Changed
- **Cited Brief System v1.3.** Three changes, all from a second blind paired test by
  Arnstein (StrategistKit), four planted errors against a clean control, 4/4 caught and
  0 false positives on v1.1, with three points left open:
  every "cannot verify" item now goes in **exactly one list**, with a precedence rule
  (a forward-looking claim is *seller-asserted*, with the history quoted beside it, never
  *contradicted*; a point told outside the attached documents is *missing*; two figures
  that may cover different periods are *missing* until the periods are known); the
  final pass now checks **strengths** as well as numbers, so a strength with no cited
  basis leaves the strengths section; and the final pass tests **relationships across
  pages** (a change between periods against the one-off items and drivers stated
  elsewhere), not only totals within one table. The v1.2 line that let a superlative's
  missing baseline appear under both *seller-asserted* and *missing* is replaced.
  Tested the same day with a blind run on the synthetic Project Sentinel deal and an
  independent second reader (about 110 claims, every number correct, 8 moved). The run
  still counted the seller's numbers adding up, and the seller's candour, as strengths,
  so the rule now names both as never a strength, and the cross-page check names an
  add-back dated to a different period from the earnings it adjusts.

## 2026-10-08

### Changed
- **Cited Brief System v1.2.** Four changes, all from an adversarial test on Agensi by
  Loretta Compliance (a four-page roofing CIM with planted traps; their verdict: "it held"):
  the brief now opens with a status line, *"Second pass: NOT RUN"*, that only an
  independent second reader in a fresh session may change, so the writer's own check
  can never pass for an independent one; superlatives with no comparison figure on the
  page ("record", "best-ever") always go under *seller-asserted*; a figure that depends
  on reading an ambiguous phrase is shown only as a labelled sensitivity, after the
  strictest figure the page supports; and industry knowledge the documents do not state
  goes into a separate *Reviewer's aside (outside the documents)*, never into the facts.

## 2026-10-07

### Changed
- **Cited Brief System v1.1.** The "cannot verify" list is now three lists, because
  each asks the buyer for a different action: *contradicted* (two places disagree,
  both quoted with the arithmetic), *missing* (not in the materials, with what to
  request) and *seller-asserted* (claimed but never backed by a figure or source).
  The brief now ends with a built-in final pass: open every citation, recompute every
  total and percentage, and move anything that fails into the right list. The
  Citation Checker stays the independent second read, run in a fresh session.
  Both changes were suggested by StrategistKit, who tested v1.0 on Agensi with four
  planted errors (caught 4 of 4, no false positives on a clean control).

## 2026-06-22

### Added
- **Expanded from the agent set into the full kit**, in four parts: the Prompt
  Library (100+ prompts across thesis, CIM, financials, teasers, data room, red
  flags, valuation and close), the Diligence Skills (50+ named tools), the Deal
  Team (20 installable agents) and the Systems (Cited Brief, Quick-Screen
  Scorecard, Diligence Question Bank, IC Memo Builder).

## 2026-06-21

### Changed
- Removed em dashes across the README and every skill, for a plainer register
  that reads as written by a person. Contributed as the repository's first pull
  request.

## 2026-06-20

### Changed
- Americanised spelling across the README and all skills, since most readers of
  a small-acquisitions kit are working to US conventions.

### Removed
- A temporary helper used to prepare the launch article, once that article was
  published.

## 2026-06-19

### Added
- **The Deal Team: 20 cited Claude diligence agents**, the kit's first release.
  Built for searchers, independent sponsors and one-person funds, where the
  buyer is not outgunned on capital but on people.
