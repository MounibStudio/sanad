from django.db import models


class Institution(models.Model):
    """
    Une institution administrative ou juridique
    qui peut aider l'utilisateur selon son sujet.
    """

    TYPE_CHOICES = [
        ('prefecture',   'Préfecture / Province'),
        ('commune',      'Commune / Arrondissement'),
        ('tribunal',     'Tribunal'),
        ('cnss',         'CNSS'),
        ('inspection',   'Inspection du Travail'),
        ('notaire',      'Notaire'),
        ('autre',        'Autre'),
    ]

    # Nom de l'institution
    name = models.CharField(
        max_length=255,
        verbose_name="Nom de l'institution"
    )

    # Type d'institution
    institution_type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='autre',
        verbose_name="Type"
    )

    # Ville
    city = models.CharField(
        max_length=100,
        verbose_name="Ville"
    )

    # Adresse complète
    address = models.TextField(
        verbose_name="Adresse"
    )

    # Coordonnées GPS
    latitude = models.FloatField(
        verbose_name="Latitude"
    )
    longitude = models.FloatField(
        verbose_name="Longitude"
    )

    # Sujets traités par cette institution (séparés par virgules)
    topics = models.CharField(
        max_length=255,
        verbose_name="Sujets traités",
        help_text="Ex: cin, passeport, résidence"
    )

    # Numéro de téléphone
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Téléphone"
    )

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ['city', 'name']

    def __str__(self):
        return f"{self.name} — {self.city}"