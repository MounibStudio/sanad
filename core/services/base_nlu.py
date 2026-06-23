"""Abstract interface for Natural Language Understanding (NLU) / FAQ matching.

Dev B (knowledge app) provides the concrete implementation.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from knowledge.models import FaqEntry  # imported at type-check time only


class BaseNLUService(ABC):
    """Contract for matching a user question to the closest FAQ entry."""

    @abstractmethod
    def match(self, text: str) -> "FaqEntry | None":
        """Find the best FAQ entry for the given Darija/Arabic text.

        Args:
            text: Transcribed or typed user question in Darija/Arabic.

        Returns:
            The best-matching FaqEntry, or None if no match is confident
            enough to surface to the user.
        """
