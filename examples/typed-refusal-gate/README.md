# typed-refusal in front of a cited brief

A gate that decides before a word of the diligence brief is written. Every field a buyer needs before an LOI must be
present in the documents and carry a source; otherwise the gate refuses, names the gap, and the refusal becomes the
request list for the seller. Nothing is filled in.

- Gate: [typed-refusal](https://github.com/GrayWolfOne21/typed-refusal) v0.1.1 by Andrew Stevens (Loretta Compliance), MIT.
- Deal: the synthetic Project Sentinel documents, public at https://os.devaland.com/static/sample-sources/
- Locators in Loretta's format: `<Document_Name> :: <Page_Number> :: <Section_or_Block_ID>`, each with the SHA-256 of
  the document it points to.

```bash
pip install "git+https://github.com/GrayWolfOne21/typed-refusal@892b0a0"
python3 gate_sentinel.py      # downloads the four PDFs, checks their hashes, writes receipt.json
```

## Result on Sentinel (8 October 2026, see receipt.json)

| Field | Gate | Why |
|---|---|---|
| ttm_period_end | NOT_READY | no document states it |
| revenue_by_customer_3y | NOT_READY | the CIM gives one period, top five accounts only |
| historical_financial_summary | DATA_NULL | CIM p.21 says figures are "summarized here", and there are none |
| officer_compensation | DATA_NULL | Tax return p.2: "compensation of officers ... summarized here", no figure |
| balance_sheet_amounts | DATA_NULL | FS p.3 lists the categories, no amounts |
| ttm_revenue, reported and adjusted EBITDA, largest customer share, change-of-control review | present and sourced | |

Status DATA_NULL, so the brief is not written. The five gaps become the request list for the seller. On the five
fields the documents do state, the same gate accepts.

## What the seal covers

Checked in the script, not assumed:
- A refusal seals the gap (status, the missing and empty fields, the reasons) and carries no values, by design.
- On ACCEPT, a changed value changes the seal.
- On ACCEPT, a moved locator or a changed document digest changes the seal: since v0.1.1 the seal binds the source
  chain. That fix followed a finding from running v0.1.0 on this example (8 October 2026). The example also keeps its own
  evidence digest over the seal and every locator and document hash, as an independent cross-check.
