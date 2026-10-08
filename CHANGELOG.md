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

## 2026-10-08 (evening)

### Changed
- **Cited Brief System v1.4.** Three rules from Arnstein's (StrategistKit) third blind test, run on v1.3 from
  the Agensi version (on Claude, not Agensi's run_skill model): a subtler set of three planted errors, 3/3 caught
  and 0 false positives, plus a regression on the earlier four inputs, 4/4 and 0 false positives, with no item in
  two lists in any of the four runs. His three points:
  a conflict that depends on a fact the materials do not state (which line a cost was booked on) goes under
  *missing*, naming that fact; it is *contradicted* only when the stated figures cannot both be true whatever that
  fact turns out to be. A strength cannot rest on a figure or trend that also appears under risks. And
  **normalising cuts both ways**: when one-off costs are added back, one-off income (an asset or surplus-stock sale,
  an insurance payout, a release of provisions) is taken out too, and the strictest figure is shown beside the
  seller's, with the gap under *contradicted*. His run had found that last one unprompted; it is now a rule.
  One more line from our own second reader: an evidence request named inside a *seller-asserted* item is not
  listed again under *missing*.
  Tested the same day on a new synthetic deal with four planted errors (one-off income left inside adjusted
  EBITDA, a falling margin presented as a strength, a cost conflict that depends on the booking line, a headcount
  stated two ways on the same date) against a neutral control: all four caught and classed as the rules say, the
  control returned *contradicted* "none found"; an independent second reader checked 78 claims, 0 wrong numbers.
  Regression on Project Sentinel: the same contradiction and missing items as v1.3. One change in behaviour:
  v1.4 keeps no strengths on Sentinel, where v1.3 kept two (the recurring-revenue share has no table behind it,
  and the prior years are not dated). That is the stricter rule working, and it is stated here so it is not a
  surprise.

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
