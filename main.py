#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

One short plan: an AI agent turns $100 into money in 30 days by
auditing small Shopify stores and selling audit reports + fix packs.
Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "Day 1: list 100 slow Shopify stores (free list). "
    "10-min audit each: speed, broken links, trust badges. "
    "Email one free fix; sell a $49 audit + $149 fix pack on Gumroad. "
    "$100 buys domain + Apollo credits, 500 emails. "
    "4 audits + 2 packs/wk = ~$494/wk. Owners already pay for CRO."
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(ENTRY) <= 280 or not ENTRY.strip():
        raise SystemExit(f"entry invalid: {len(ENTRY)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
