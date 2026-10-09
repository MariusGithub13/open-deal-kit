#!/usr/bin/env python3
"""typed-refusal in front of a cited brief, on the synthetic Project Sentinel deal.

The gate decides BEFORE a word of the brief is written: every field a buyer needs before an LOI must be present
in the documents and carry a source. A refusal is not an error; it is the request list for the seller.

Gate: typed-refusal v0.1.1 by Andrew Stevens (Loretta Compliance), MIT, https://github.com/GrayWolfOne21/typed-refusal
  pip install "git+https://github.com/GrayWolfOne21/typed-refusal@892b0a0"
Documents: the four synthetic Sentinel PDFs published at https://os.devaland.com/static/sample-sources/
Locator format (Loretta's): "<Document_Name> :: <Page_Number> :: <Section_or_Block_ID>"

Run: python3 gate_sentinel.py            (downloads the four PDFs, checks their SHA-256, writes receipt.json)
"""
import hashlib, json, sys, urllib.request
from typed_refusal import Contract, FieldRule, evaluate
from typed_refusal.contract import Source
from typed_refusal.gate import seal

BASE = "https://os.devaland.com/static/sample-sources/"
DOCS = ("Project_Sentinel_CIM.pdf", "Sentinel_Financial_Statements.pdf",
        "Sentinel_2025_Tax_Return.pdf", "Sentinel_Management_Call_Notes.pdf")
def sha(name):
    req = urllib.request.Request(BASE + name, headers={"User-Agent": "gate-sentinel/1.0 (open-deal-kit example)"})
    with urllib.request.urlopen(req, timeout=60) as r: return hashlib.sha256(r.read()).hexdigest()
digest = {name: sha(name) for name in DOCS}

# The fields a buyer needs before an LOI. Values are taken ONLY from what the documents state.
contract = Contract(name="sentinel-pre-loi", fields=tuple(FieldRule(n) for n in (
    "ttm_revenue", "ttm_period_end", "reported_ebitda", "adjusted_ebitda", "largest_customer_share",
    "revenue_by_customer_3y", "change_of_control_review", "historical_financial_summary",
    "officer_compensation", "balance_sheet_amounts")))

payload = {
    "ttm_revenue": "$6.21M",
    # ttm_period_end: no document states it                      -> missing  -> NOT_READY
    "reported_ebitda": "$1.08M",
    "adjusted_ebitda": "$1.42M",
    "largest_customer_share": "22.0% (Northgate, $1,366,000 of $6,210,000)",
    # revenue_by_customer_3y: one period, top five accounts only  -> missing  -> NOT_READY
    "change_of_control_review": "not undertaken by the seller",   # a stated fact, and a risk: the gate checks presence, not merit
    "historical_financial_summary": None,  # CIM p.21: "summarized here", no table         -> present, empty -> DATA_NULL
    "officer_compensation": None,          # Tax p.2: "compensation of officers ... summarized here", no figure -> DATA_NULL
    "balance_sheet_amounts": None,         # FS p.3: categories listed, no amounts         -> DATA_NULL
}
def src(field, doc, page, block):
    return Source(field, doc, f"{doc} :: Page {page} :: {block}", digest[doc])
sources = [
    src("ttm_revenue", "Project_Sentinel_CIM.pdf", 6, "Section 5 Para 1"),
    src("reported_ebitda", "Sentinel_Financial_Statements.pdf", 4, "Para 1"),
    src("adjusted_ebitda", "Sentinel_Financial_Statements.pdf", 4, "Para 1"),
    src("largest_customer_share", "Project_Sentinel_CIM.pdf", 9, "Section 8 Para 1"),
    src("change_of_control_review", "Project_Sentinel_CIM.pdf", 19, "Section 18 Para 1"),
    src("historical_financial_summary", "Project_Sentinel_CIM.pdf", 21, "Section 20 Para 1"),
    src("officer_compensation", "Sentinel_2025_Tax_Return.pdf", 2, "Schedules Para 1"),
    src("balance_sheet_amounts", "Sentinel_Financial_Statements.pdf", 3, "Para 1"),
]

d = evaluate(contract, payload, sources)
s1, s2 = seal(d), seal(evaluate(contract, payload, sources))

# Evidence digest (ours, not part of typed-refusal). Since v0.1.1 the seal itself binds the sources; the digest is kept
# as an independent cross-check over the seal and every locator and document hash.
def evidence(seal_hex, srcs):
    rows = sorted((x.field, x.source_id, x.locator, x.digest) for x in srcs)
    return hashlib.sha256(json.dumps([seal_hex, rows], separators=(",", ":")).encode()).hexdigest()
e1 = evidence(s1, sources)

# The open path: the same gate on the five fields the documents DO state. It accepts, and the values enter the seal.
stated = ("ttm_revenue", "reported_ebitda", "adjusted_ebitda", "largest_customer_share", "change_of_control_review")
c_ok = Contract(name="sentinel-stated-fields", fields=tuple(FieldRule(n) for n in stated))
p_ok = {k: payload[k] for k in stated}
src_ok = [x for x in sources if x.field in stated]
d_ok = evaluate(c_ok, p_ok, src_ok); s_ok = seal(d_ok); e_ok = evidence(s_ok, src_ok)
s_ok_tampered = seal(evaluate(c_ok, dict(p_ok, largest_customer_share="15.0%"), src_ok))
moved = [Source(x.field, x.source_id, x.locator.replace("Page 9", "Page 10"), x.digest) for x in src_ok]
s_ok_moved = seal(evaluate(c_ok, p_ok, moved)); e_ok_moved = evidence(s_ok_moved, moved)
s_refused_tampered = seal(evaluate(contract, dict(payload, largest_customer_share="15.0%"), sources))

requests = [f"{f}: not in any of the four documents. Please provide it, with the document and page." for f in d.not_ready] + \
           [f"{f}: the document shows it but leaves it empty ({next(x.locator for x in sources if x.field == f)}). Please provide the figures." for f in d.data_null]

receipt = {
    "contract": d.contract, "status": d.status, "brief_written": d.ok,
    "accepted": d.accepted, "not_ready": list(d.not_ready), "data_null": list(d.data_null), "reasons": list(d.reasons),
    "seal": s1, "evidence_digest": e1,
    "sources": [{"field": x.field, "locator": x.locator, "sha256": x.digest} for x in sources],
    "documents": {n: {"url": BASE + n, "sha256": h} for n, h in digest.items()},
    "request_list_for_seller": requests,
    "open_path": {"contract": d_ok.contract, "status": d_ok.status, "accepted": d_ok.accepted, "seal": s_ok, "evidence_digest": e_ok},
    "checks": {
        "refusal: same input, same seal": s1 == s2,
        "refusal: a changed value leaves the seal unchanged (by design, a refusal seals the gap and carries no values)": s_refused_tampered == s1,
        "accept: a changed value changes the seal": s_ok_tampered != s_ok,
        "accept: a moved locator changes the seal (v0.1.1 binds the source chain)": s_ok_moved != s_ok,
        "accept: a moved locator changes the evidence digest": e_ok_moved != e_ok,
    },
    "gate": "typed-refusal v0.1.1 @ 892b0a0",
}
json.dump(receipt, open("receipt.json", "w"), indent=2)
print(json.dumps({k: receipt[k] for k in ("status", "brief_written", "not_ready", "data_null", "seal", "evidence_digest", "open_path", "checks")}, indent=2))
print("\nRequest list for the seller:"); [print(" -", r) for r in requests]
