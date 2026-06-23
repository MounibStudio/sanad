"""Abstract interface for Automatic Speech Recognition (ASR).

Dev A (voice app) provides the concrete implementation.
"""
from abc import ABC, abstractmethod


class BaseASRService(ABC):
    """Contract for converting spoken audio to Moroccan Darija text."""

    @abstractmethod
    def transcribe(self, audio_data: bytes) -> str:
        """Transcribe raw audio bytes to a Darija/Arabic text string.

        Args:
            audio_data: Raw audio bytes (WAV or WebM captured from the browser).

        Returns:
            Transcribed text in Darija/Arabic script.

        Raises:
            ValueError: If audio_data is empty or in an unsupported format.
        """
