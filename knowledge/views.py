from django.shortcuts import render
from .services import GeminiNLUService
from institutions.services import MockGeoService


def index(request):
    """Page d'accueil avec formulaire de question."""
    return render(request, 'knowledge/reponse.html', {})


def reponse(request):
    question = request.GET.get('question', '').strip()

    if not question:
        return render(request, 'knowledge/reponse.html', {})

    # Utiliser Gemini NLU (Groq)
    nlu_service = GeminiNLUService()
    result = nlu_service.match(question)

    if not result:
        return render(request, 'knowledge/reponse.html', {
            'question': question,
            'no_match': True
        })

    # Géolocalisation
    geo_service = MockGeoService()
    nearest_institutions = geo_service.nearest(
        topic=result['category'],
        lat=33.5731,
        lon=-7.5898,
        max_results=3
    )

    context = {
        'question': question,
        'answer_darija': result['answer'],
        'legal_reference': result['legal_reference'],
        'disclaimer': result['disclaimer'],
        'institutions': nearest_institutions,
        'text_dir': result['direction'],
        'text_lang': result['lang'],
    }

    return render(request, 'knowledge/reponse.html', context)