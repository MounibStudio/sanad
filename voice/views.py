from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def ask(request):
    return render(request, "voice/ask.html")
