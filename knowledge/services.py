from core.services.base_nlu import BaseNLUService
from .models import FaqEntry


class MockNLUService(BaseNLUService):
    """
    Service NLU basique — matching par mots-clés.
    Reçoit une question en darija et retourne la FaqEntry correspondante.
    """

    def match(self, text: str):
        """
        Cherche la FAQ dont les mots-clés correspondent
        au texte de la question.
        """

        # 1. Nettoyer le texte — tout en minuscules
        text_lower = text.lower().strip()

        # 2. Récupérer toutes les FAQ de la base de données
        all_faqs = FaqEntry.objects.all()

        # 3. Pour chaque FAQ, chercher si un mot-clé est dans la question
        best_match = None
        best_score = 0

        for faq in all_faqs:
            score = 0
            keywords = [k.strip().lower() for k in faq.keywords.split(',')]

            for keyword in keywords:
                if keyword and keyword in text_lower:
                    score += 1

            # Garder la FAQ avec le meilleur score
            if score > best_score:
                best_score = score
                best_match = faq

        # 4. Retourner la meilleure FAQ trouvée (ou None si rien)
        if best_score > 0:
            return best_match

        return None