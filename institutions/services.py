import math
from core.services.base_geo import BaseGeoService
from .models import Institution


class MockGeoService(BaseGeoService):
    """
    Service géolocalisation basique — matching par sujet.
    Retourne les institutions les plus proches selon le topic.
    """

    def nearest(self, topic: str, lat: float, lon: float, max_results: int = 3):
        """
        Cherche les institutions qui traitent le topic donné,
        triées par distance (la plus proche en premier).
        """

        # 1. Chercher toutes les institutions qui traitent ce topic
        topic_lower = topic.lower().strip()
        matching = []

        for institution in Institution.objects.all():
            topics = [t.strip().lower() for t in institution.topics.split(',')]
            if any(topic_lower in t or t in topic_lower for t in topics):
                matching.append(institution)

        # 2. Trier par distance GPS
        def distance(inst):
            return self._calculate_distance(lat, lon, inst.latitude, inst.longitude)

        matching.sort(key=distance)

        # 3. Retourner les max_results plus proches
        return matching[:max_results]

    def _calculate_distance(self, lat1, lon1, lat2, lon2):
        """
        Calcule la distance en km entre deux points GPS.
        Formule de Haversine.
        """
        R = 6371  # Rayon de la Terre en km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = (math.sin(dlat / 2) ** 2 +
             math.cos(math.radians(lat1)) *
             math.cos(math.radians(lat2)) *
             math.sin(dlon / 2) ** 2)

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c