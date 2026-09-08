"""Base agent abstraction for FinRAG workflows."""

from __future__ import annotations


class BaseAgent:
    """Simple base class for agent implementations."""

    def __init__(self, name: str):
        self.name = name

    def run(self, prompt: str) -> str:
        return f"{self.name} processed: {prompt}"
