"""Session-backed helpers for reading and writing accessibility preferences."""

FONT_SIZES = ("normal", "large", "xlarge")


def get_a11y_settings(request) -> dict:
    return {
        "a11y": {
            "font_size": request.session.get("a11y_font_size", "normal"),
            "high_contrast": request.session.get("a11y_high_contrast", False),
        }
    }


def save_a11y_settings(request, *, font_size: str | None = None, high_contrast: bool | None = None) -> None:
    if font_size is not None and font_size in FONT_SIZES:
        request.session["a11y_font_size"] = font_size
    if high_contrast is not None:
        request.session["a11y_high_contrast"] = bool(high_contrast)
