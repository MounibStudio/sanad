from django.shortcuts import render


def index(request):
    """Dev B: replace this placeholder with the FAQ search UI."""
    return render(request, 'knowledge/index.html')
