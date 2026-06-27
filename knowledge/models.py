from django.db import models


class FaqEntry(models.Model):
    """
    Une entrée FAQ : question en darija + réponse simplifiée + référence légale.
    """

    answer_arabizi = models.TextField(blank=True, null=True)
    disclaimer_arabizi = models.TextField(blank=True, null=True)

    CATEGORY_CHOICES = [
        ('cin',       'Carte Nationale d\'Identité'),
        ('naissance', 'Acte de naissance'),
        ('location',  'Contrat de location'),
        ('travail',   'Contrat de travail'),
        ('tribunal',  'Convocation tribunal'),
        ('heritage',  'Héritage'),
        ('cnss',      'CNSS / Sécurité sociale'),
        ('autre',     'Autre'),
    ]

    question_darija = models.TextField(
        verbose_name="Question en Darija"
    )
    keywords = models.CharField(
        max_length=255,
        verbose_name="Mots-clés",
        help_text="Ex: cin, carte, identité, renouveler"
    )
    answer_darija = models.TextField(
        verbose_name="Réponse simplifiée en Darija"
    )
    legal_reference = models.CharField(
        max_length=255,
        verbose_name="Référence légale",
        help_text="Ex: Dahir n° 1-08-214 du 23 décembre 2008"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='autre',
        verbose_name="Catégorie"
    )
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


class LegalDocument(models.Model):
    """
    Un chunk de texte extrait d'un PDF juridique marocain.
    """

    source_file = models.CharField(max_length=500)
    page_number = models.IntegerField(default=0)
    content = models.TextField()
    category = models.CharField(
        max_length=100,
        default='autre',
        help_text="Ex: travail, famille, penal, commerce..."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Document Juridique"
        verbose_name_plural = "Documents Juridiques"

    def __str__(self):
        return f"{self.source_file} — Page {self.page_number}"