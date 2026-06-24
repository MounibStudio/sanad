from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .services.stub_nlu import StubNLUService

_nlu = StubNLUService()


@require_http_methods(["GET", "POST"])
def ask(request):
    question = ""
    answer = None

    if request.method == "POST":
        question = request.POST.get("question_text", "").strip()
        if question:
            entry = _nlu.match(question)
            answer = entry.answer if entry else "ما لقيناش جواب على سؤالك. حاول مرة أخرى."

    return render(request, "voice/ask.html", {"question": question, "answer": answer})
