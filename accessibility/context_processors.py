from .utils import get_a11y_settings


def a11y_settings(request):
    """Inject accessibility preferences into every template context."""
    return get_a11y_settings(request)
