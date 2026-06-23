from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .utils import save_a11y_settings

# (value, display label, preview font-size) — used in settings.html
FONT_CHOICES = [
    ("normal",  "عادي",       "1.25rem"),
    ("large",   "كبير",       "1.5rem"),
    ("xlarge",  "كبير جداً",  "1.875rem"),
]


@require_http_methods(["GET", "POST"])
def settings_view(request):
    if request.method == "POST":
        font_size = request.POST.get("font_size", "normal")
        high_contrast = request.POST.get("high_contrast") == "on"
        save_a11y_settings(request, font_size=font_size, high_contrast=high_contrast)
        next_url = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/"
        return redirect(next_url)

    return render(request, "accessibility/settings.html", {"font_choices": FONT_CHOICES})
