from django.shortcuts import render


def index(request):
    """Dev A: replace this placeholder with the voice recording UI."""
    return render(request, 'voice/index.html')
