# Example ledgers

Three filled-in ledgers, plus one broken one so you can see what the checker catches. The agent names are roles, not products. Swap in whatever you actually pay for.

| File | Who it fits |
|---|---|
| `solo-founder.csv` | One person, a flat chat as the front door, a metered builder, a research agent, a phone concierge |
| `creator.csv` | A daily content lane that posts on its own, with the disclosure and the 80 percent stop written into Boundary |
| `small-agency.csv` | Client work split by client, with client data kept to its own rows and a dated fallback on a blocked standing task |
| `messy-week.csv` | What a week looks like before the ledger: two owners, a duplicate, done with no result, a standing lane with no stop |

Try it:

```
python3 tools/ledger_check.py examples/messy-week.csv
python3 tools/ledger_check.py examples/creator.csv
```
