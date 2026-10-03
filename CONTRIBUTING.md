# Contributing

Contributions are welcome if they keep the ledger small.

**Good contributions**
- A new example ledger for a real kind of operator (add a CSV to `examples/` that passes `tools/ledger_check.py`, plus a line in `examples/README.md`).
- A sample brief that uses the Job / Inputs / Constraints / Stop / Done shape.
- A stop message you actually use.
- A checker fix with a short test case.
- A resource link: well-known, free to read, and about running agents safely or about ownership and review in general.

**Out of scope**
- New ledger columns. Priority, due date, and budget go in Boundary or Result.
- Rankings or comparisons of models or vendors.
- Tools that have an agent manage the other agents.
- Affiliate or referral links.

**How**
1. Open an issue first for anything bigger than a typo.
2. Keep pull requests to one change.
3. Run `python3 tools/ledger_check.py` on any CSV you add.

By contributing you agree that your contribution is licensed under the MIT License in `LICENSE`.
