#!/usr/bin/env python3
"""ledger_check.py: lint a multi-agent ledger CSV.

Usage:  python3 tools/ledger_check.py ledger.csv

Checks every row against the rules in README.md:
  - exactly one owner per task
  - no task assigned twice
  - every row has a boundary
  - standing rows (cadence other than one-off) name a stop
  - status is one of: pending, in progress, active, blocked, done
  - done rows say what you opened in Result
  - blocked rows say what they are waiting on
  - no extra columns
Standard library only. Exit code 1 if any problems are found.
"""
import csv
import re
import sys

COLUMNS = ["Task", "Owner", "Boundary", "Cadence", "Status", "Result"]
STATUSES = {"pending", "in progress", "active", "blocked", "done"}
MULTI_OWNER = re.compile(r"\s(and|&|\+)\s|[,/;]", re.I)


def check(path):
    problems = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = [h.strip() for h in (reader.fieldnames or [])]
        if header != COLUMNS:
            problems.append(f"header: expected {', '.join(COLUMNS)}; got {', '.join(header)}. Don't add columns.")
            return problems, 0
        seen = {}
        n = 0
        for i, raw in enumerate(reader, start=2):
            row = {k.strip(): (v or "").strip() for k, v in raw.items() if k}
            if not any(row.values()):
                continue
            n += 1
            task, owner = row["Task"], row["Owner"]
            status = row["Status"].lower()
            where = f"line {i} ({task[:40] or 'no task'})"
            if not task:
                problems.append(f"{where}: no Task.")
            if not owner:
                problems.append(f"{where}: no Owner. Name one, split the task, or delete it.")
            elif MULTI_OWNER.search(owner):
                problems.append(f"{where}: Owner '{owner}' looks like more than one. One owner per task.")
            key = task.lower()
            if key and key in seen:
                problems.append(f"{where}: same Task as line {seen[key]}. Keep one; send the stop line to the other owner.")
            seen.setdefault(key, i)
            if not row["Boundary"]:
                problems.append(f"{where}: no Boundary. Default deny is send, post, pay, delete.")
            cadence = row["Cadence"].lower()
            if cadence and cadence != "one-off" and "stop" not in row["Boundary"].lower():
                problems.append(f"{where}: standing row with no stop in Boundary (default: stop at 80 percent of the weekly allowance).")
            if status not in STATUSES:
                problems.append(f"{where}: Status '{row['Status']}' is not one of {', '.join(sorted(STATUSES))}.")
            if status == "done" and not row["Result"]:
                problems.append(f"{where}: marked done with an empty Result. Done means you opened it; write what you opened.")
            if status == "blocked" and not row["Result"]:
                problems.append(f"{where}: blocked with no reason. Write what it is waiting on and who holds it.")
    return problems, n


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    problems, n = check(sys.argv[1])
    for p in problems:
        print("- " + p)
    print(f"{n} rows checked, {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
