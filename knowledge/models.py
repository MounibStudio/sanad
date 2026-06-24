from django.db import models

class FaqEntry(models.Model):
    """
    Une entrée FAQ : question en darija + réponse simplifiée + référence légale.
    """

    CATEGORY_CHOICES = [
        ('cin',         'Carte Nationale d\'Identité'),
        ('naissance',   'Acte de naissance'),
        ('location',    'Contrat de location'),
        ('travail',     'Contrat de travail'),
        ('tribunal',    'Convocation tribunal'),
        ('heritage',    'Héritage'),
        ('cnss',        'CNSS / Sécurité sociale'),
        ('autre',       'Autre'),
    ]

    # La question en darija (ex: "kif ndir CIN dyali?")
    question_darija = models.TextField(
        verbose_name="Question en Darija"
    )

    # Mots-clés pour le matching NLU (séparés par des virgules)
    keywords = models.CharField(
        max_length=255,
        verbose_name="Mots-clés",
        help_text="Ex: cin, carte, identité, renouveler"
    )

    # La réponse simplifiée en darija
    answer_darija = models.TextField(
        verbose_name="Réponse simplifiée en Darija"
    )

    # L'article de loi de référence
    legal_reference = models.CharField(
        max_length=255,
        verbose_name="Référence légale",
        help_text="Ex: Dahir n° 1-08-214 du 23 décembre 2008"
    )

    # La catégorie du document
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='autre',
        verbose_name="Catégorie"
    )

    # Avertissement juridique affiché à l'utilisateur
    disclaimer = models.TextField(
        verbose_name="Avertissement",
        default="Hada tawjih gha, machi avis juridique officiel."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "FAQ Entry"
        verbose_name_plural = "FAQ Entries"
        ordering = ['category']

    def __str__(self):
        return f"[{self.category}] {self.question_darija[:50]}"