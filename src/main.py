"""Starter entry point for the FinRAG Engine."""

from __future__ import annotations


def build_sample_summary(topic: str, evidence: list[str]) -> str:
    """Build a simple sample response from a topic and evidence list."""
    evidence_text = " ".join(evidence)
    return f"Summary for {topic}: {evidence_text}"


if __name__ == "__main__":
    summary = build_sample_summary(
        topic="quarterly revenue",
        evidence=[
            "Revenue grew 12% QoQ.",
            "Operating margin improved to 18%.",
        ],
    )
    print(summary)
