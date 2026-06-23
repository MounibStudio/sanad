"""Abstract interface for Text-to-Speech (TTS).

Dev A (accessibility app) provides the concrete implementation.
"""
from abc import ABC, abstractmethod


class BaseTTSService(ABC):
    """Contract for converting Darija/Arabic text to spoken audio."""

    @abstractmethod
    def synthesize(self, text: str, lang: str = "ar-MA") -> bytes:
        """Synthesize speech from text and return raw audio bytes (WAV/MP3).

        Args:
            text: Arabic or Darija text to speak aloud.
            lang: BCP-47 language tag; defaults to Moroccan Arabic.

        Returns:
            Raw audio bytes ready to be served as an HTTP response
            or written to a temporary file.

        Raises:
            ValueError: If text is empty.
        """
