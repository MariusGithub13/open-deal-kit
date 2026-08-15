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
