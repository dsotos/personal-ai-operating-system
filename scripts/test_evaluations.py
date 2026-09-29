#!/usr/bin/env python3
"""Validate synthetic routing expectations against the public contract.

This checks declared policy consistency; it does not pretend to run an AI router.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples" / "routing-evaluations.json"

RULES = {
    "quick": ("fast-local", "none-or-supplied-context", {"local-read", "deterministic-scripts"}),
    "capture": ("knowledge-capture", "provenance-required", {"knowledge-read", "knowledge-write", "local-validation"}),
    "research": ("source-backed", "dated-source-backed", {"web-search", "source-extraction", "knowledge-read"}),
    "writing": ("drafting", "supplied-context-or-cited-sources", {"local-drafting", "style-checks", "knowledge-read"}),
    "content": ("channel-adaptation", "canonical-thesis-and-relevant-sources", {"local-drafting", "source-lookup", "knowledge-read"}),
    "deep": ("deep-reasoning", "assumptions-evidence-and-review", {"specialist-skills", "read-only-tools", "delegation"}),
    "operations": ("controlled-operation", "pre-post-state-and-read-back", {"named-operational-tool", "verification-read-back"}),
}

fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
ids = {item["id"] for item in fixtures}
required_ids = {
    "quick-format", "capture-decision", "research-current", "writing-rewrite",
    "content-adapt", "deep-architecture", "operations-approved",
    "ambiguous-routing", "restricted-context", "missing-authorization",
    "tool-failure", "post-publication-discrepancy",
}
assert required_ids <= ids, sorted(required_ids - ids)
assert set(RULES) == {"quick", "capture", "research", "writing", "content", "deep", "operations"}

for item in fixtures:
    category = item["category"]
    lane, evidence, allowed_tools = RULES[category]
    assert item["lane"] == lane, item["id"]
    assert item["evidence"] == evidence, item["id"]
    assert set(item["tools"]).issubset(allowed_tools), item["id"]
    assert item["approval"] in {"sí", "no", "escalar"}, item["id"]
    assert item["approval_reason"].strip(), item["id"]
    if item["data_class"] == "Restricted":
        assert item["approval"] == "escalar", item["id"]
        assert item["tools"] == [], item["id"]
    if item["id"] in {"ambiguous-routing", "missing-authorization", "tool-failure", "post-publication-discrepancy"}:
        assert item["approval"] == "escalar", item["id"]

print(f"routing evaluations: passed ({len(fixtures)} synthetic cases)")
print("mechanical policy checks passed; human review remains required for ambiguous and consequential cases")
