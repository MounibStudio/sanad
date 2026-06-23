"""Abstract interface for Geolocation / nearest institution lookup.

Dev B (institutions app) provides the concrete implementation.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from institutions.models import Institution  # imported at type-check time only


class BaseGeoService(ABC):
    """Contract for finding nearby institutions relevant to a legal topic."""

    @abstractmethod
    def nearest(
        self,
        topic: str,
        lat: float,
        lon: float,
        max_results: int = 5,
    ) -> "list[Institution]":
        """Return institutions near (lat, lon) that handle the given topic.

        Args:
            topic: Legal or administrative topic keyword (e.g. "عقد الزواج").
            lat: User's latitude in decimal degrees.
            lon: User's longitude in decimal degrees.
            max_results: Maximum number of institutions to return.

        Returns:
            Ordered list of Institution objects (nearest first), possibly empty.
        """
