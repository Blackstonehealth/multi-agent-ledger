<!-- DRAFT. Replace https://gumroad.com/l/cwwwo with the real Lemon Squeezy link before the repo goes public. Remove this comment before publishing. -->

# Multi-Agent Ledger

**A free, plain-text system for running two or more AI agents without duplicated work, surprise bills, or "done" reports for work that doesn't exist.**

A human governs a workforce of agents with one front door, one owner per task, one ledger, a finished brief, and a result they opened themselves. Not a ranking of models. Not a prompt pack.

You don't need another agent to coordinate the ones you have. You need a ledger. This repo gives you one, plus examples, sample briefs, copy-paste stop messages, and a small checker that flags the usual mistakes.

## 30-second quickstart

1. Copy [`ledger.csv`](ledger.csv) into a spreadsheet, or [`ledger.md`](ledger.md) into a notes file.
2. Add one row for every job your agents are doing right now. Give each row **exactly one** owner.
3. If two agents are on the same job, keep the further-along one and paste the stop line from [`stop-messages.md`](stop-messages.md) to the other.
4. Send your next job as one finished brief ([`briefs/`](briefs/)). Mark it done only after you've opened the result yourself.

Optional: `python3 tools/ledger_check.py ledger.csv` flags rows with two owners, duplicate tasks, missing boundaries, standing lanes with no stop, and "done" with nothing opened. It uses only the standard library and needs no install.

## The five principles

1. **One front door.** All the thinking, drafting, and deciding happens in one agent. Pick it for judgment, memory, reliability, and the cost of an hour of talk. If a metered agent is spending the week on conversation, it can't be the front door.
2. **One owner per task.** The same task never goes to two agents. If you can't name one owner, split the task or delete it. You are the router.
3. **One ledger.** Six columns: Task, Owner, Boundary, Cadence, Status, Result. If a job isn't in it, it isn't assigned. Don't add columns.
4. **A finished brief.** Dispatch, don't discuss. Each brief covers the job, the inputs, the constraints, the stop, and what done looks like. No follow-up chat.
5. **A result you opened yourself.** The agent saying it's done doesn't make it done. Done is the file, link, or log you opened.

## What's in here

```
ledger.csv            blank ledger with two example rows
ledger.md             the same ledger as a markdown table
examples/             filled-in ledgers: solo founder, creator, small agency, and a messy week
briefs/               sample dispatch briefs: one-off build, one-off research, standing lane
stop-messages.md      copy-paste stop, correction, and out-of-lane lines
tools/ledger_check.py lints a ledger CSV against the rules above
```

## Boundaries, in one paragraph

Unless a row grants it, no agent sends a message, posts in public, pays or subscribes, or deletes anything. Reading, drafting, and organizing are fine inside the task. Any lane that runs on its own stops at 80 percent of its weekly allowance unless you wrote a different number. A lane that can post without asking is the riskiest grant you can give. Don't copy it into health, finance, or anything you can't retract.

## Further reading

Well-known, free resources on building and running agents safely. They aren't affiliated with this repo.

- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) — Anthropic's guide to when to use agents vs simple workflows.
- [A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — OpenAI's guide (PDF), including guardrails and human intervention.
- [Model Context Protocol](https://modelcontextprotocol.io) — the open standard many agents use to connect to tools and data.
- [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — Simon Willison on why private data + untrusted content + outbound actions is the dangerous combination.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — common security risks, including excessive agency.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — the reference framework for governing AI risk.
- [Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) — why each agent gets only the logins it needs.
- [Responsibility assignment matrix (RACI)](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix) — the older human version of "one owner per task."
- [Postmortem culture](https://sre.google/sre-book/postmortem-culture/) — Google SRE book chapter; a good model for the weekly review.
- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — a large community list of agent products and frameworks.

PRs that add resources are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Paid edition

The free repo is enough to start. The paid edition, **The Multi-Agent Operating System** ($39), adds what the repo doesn't have:

- **The full playbook (16-page PDF):** how to clear work already in flight, authority rules and spend stops, how results come back, what to do when it wobbles, the weekly review, and the monthly drop that decides which subscriptions keep their seat.
- **A worked example:** one week with three agents, including the ledger, a duplicate caught, the stop message sent, and the scored test.
- **An editable spreadsheet ledger (xlsx):** Ledger, Lanes, and Weekly Review tabs, owner and status dropdowns, and an 80 percent stop check on every lane.
- **Printable forms:** the ledger, the lane worksheet, and the dispatch brief.

You are not buying AI advice. You are buying the operating system: the ledger, the dispatch brief, the authority rules, the spend stops, and the review that keeps you from becoming the full-time coordinator of your own agents.

No course, no call, no community. Refunds within seven days if you ask. **[Get it here →](https://gumroad.com/l/cwwwo)**

## License

Everything in this repository is MIT licensed (see [LICENSE](LICENSE)). The paid playbook and its templates are sold separately, are not in this repository, and are not covered by this license.
