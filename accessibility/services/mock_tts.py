from core.services.base_tts import BaseTTSService


class MockTTSService(BaseTTSService):
    """Fake TTS — returns empty bytes.

    Text-to-speech is handled client-side by the browser's Web Speech API
    (window.speechSynthesis). This class satisfies the backend contract so
    voice/views.py can import and call it without a real TTS engine.
    """

    def synthesize(self, text: str, lang: str = "ar-MA") -> bytes:
        if not text:
            raise ValueError("text is empty")
        # Real impl will return audio bytes (WAV/MP3).
        # Browser SpeechSynthesis handles playback in the prototype.
        return b""
