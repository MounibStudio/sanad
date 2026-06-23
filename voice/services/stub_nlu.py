"""Temporary NLU stub so the voice app works before Dev B ships knowledge/.

FakeEntry is duck-type-compatible with knowledge.models.FaqEntry:
it exposes the same .question and .answer attributes the template reads.
Swap StubNLUService for the real NLUService once Dev B merges.
"""
from __future__ import annotations

from dataclasses import dataclass
from core.services.base_nlu import BaseNLUService


@dataclass
class FakeEntry:
    question: str
    answer: str


_FAQ: list[tuple[str, FakeEntry]] = [
    (
        "بطاقة",
        FakeEntry(
            question="كيفاش نجدد بطاقة الوطنية؟",
            answer=(
                "باش تجدد بطاقة الوطنية ديالك، خاصك تمشي للمقاطعة "
                "بالوثائق: صورة الحالة المدنية، جوج صور، ودفع الرسوم."
            ),
        ),
    ),
    (
        "زواج",
        FakeEntry(
            question="شنو هي وثائق عقد الزواج؟",
            answer=(
                "لعقد الزواج خاصك: عقد الميلاد، شهادة الإقامة، "
                "جوج صور، وشهادة الأهلية من المحكمة."
            ),
        ),
    ),
    (
        "ميلاد",
        FakeEntry(
            question="كيفاش نسجل مولود جديد؟",
            answer=(
                "تسجيل المولود يتدار في الحالة المدنية خلال 30 يوم من الولادة. "
                "خاصك شهادة الولادة من الطبيب وبطاقة الوالدين."
            ),
        ),
    ),
    (
        "إقامة",
        FakeEntry(
            question="كيفاش نستخرج شهادة الإقامة؟",
            answer=(
                "شهادة الإقامة تتصدر من المقاطعة ديالك. خاصك بطاقة الوطنية "
                "وشهادة السكنى من رئيس الحي."
            ),
        ),
    ),
]

# Fallback used when no keyword matches
_DEFAULT = FakeEntry(
    question="سؤال عام",
    answer=(
        "شكرا على سؤالك. هاد المعلومة ما كاينة مزال في القاعدة. "
        "مشاور موظف مختص في أقرب مصلحة إدارية."
    ),
)


class StubNLUService(BaseNLUService):
    """Keyword-based FAQ matcher. Replace with Dev B's real NLUService."""

    def match(self, text: str) -> FakeEntry:
        for keyword, entry in _FAQ:
            if keyword in text:
                return entry
        return _DEFAULT
