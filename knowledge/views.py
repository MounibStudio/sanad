from django.shortcuts import render
from .services import MockNLUService
from institutions.services import MockGeoService


def index(request):
    """
    Page principale — affiche le formulaire de question.
    """
    return render(request, 'knowledge/index.html')


def reponse(request):
    """
    Page réponse — reçoit la question, cherche la FAQ
    et les institutions proches, affiche le résultat.
    """

    # 1. Récupérer la question posée par l'utilisateur
    question = request.GET.get('question', '').strip()

    if not question:
        return render(request, 'knowledge/index.html', {
            'erreur': 'Kteb su2al men fadlek'
        })

    # 2. Utiliser le NLU pour trouver la bonne FAQ
    nlu = MockNLUService()
    faq = nlu.match(question)

    # 3. Si aucune FAQ trouvée
    if not faq:
        return render(request, 'knowledge/reponse.html', {
            'question': question,
            'faq': None,
            'institutions': [],
        })

    # 4. Utiliser GeoService pour trouver les institutions proches
    # Coordonnées par défaut — Casablanca
    geo = MockGeoService()
    institutions = geo.nearest(faq.category, 33.5731, -7.5898)

    # 5. Afficher la page réponse
    return render(request, 'knowledge/reponse.html', {
        'question': question,
        'faq': faq,
        'institutions': institutions,
    })