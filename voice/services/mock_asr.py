import itertools
from core.services.base_asr import BaseASRService

_SAMPLES = [
    "كيفاش نجدد بطاقة الوطنية ديالي؟",
    "شنو هي الوثائق اللي خاصني باش نستخرج عقد الزواج؟",
    "فين نمشي باش نسجل ولدي في الحالة المدنية؟",
]
_cycle = itertools.cycle(_SAMPLES)


class MockASRService(BaseASRService):
    """Fake ASR — returns hardcoded darija samples in round-robin.

    Used as a stand-in until a real ASR engine is wired in.
    The browser's SpeechRecognition API handles actual transcription on the
    frontend; this class satisfies the backend contract for testing.
    """

    def transcribe(self, audio_data: bytes) -> str:
        if not audio_data:
            raise ValueError("audio_data is empty")
        return next(_cycle)
