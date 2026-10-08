#!/usr/bin/env python3
"""Summarise shipment ETAs from a CSV export (playground)."""
import csv, sys

def load(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def summarise(rows):
    late = [r for r in rows if r.get("status") == "late"]
    return {"total": len(rows), "late": len(late)}

if __name__ == "__main__":
    rows = load(sys.argv[1])
    print(summarise(rows))
