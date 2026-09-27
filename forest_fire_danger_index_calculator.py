import math


FFDI_EPSILON = 1e-6

TEMP_MIN = -10.0
TEMP_MAX = 50.0
RH_MIN = 0.0
RH_MAX = 100.0
WIND_MIN = 0.0
WIND_MAX = 200.0
DF_MIN = 0.0
DF_MAX = 10.0

CLASSIFICATION_RANGES = [
    (11.0, "Low", "#2e7d32", "#ffffff"),
    (23.0, "Moderate", "#fbc02d", "#111111"),
    (49.0, "High", "#ef6c00", "#ffffff"),
    (99.0, "Very High", "#d32f2f", "#ffffff"),
]


def _to_float(value, name):
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a number.")


def _validate_range(value, minimum, maximum, name):
    if value < minimum or value > maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}.")
    return value


def classify_ffdi(ffdi_value):
    for threshold, label, background_color, text_color in CLASSIFICATION_RANGES:
        if ffdi_value <= threshold:
            return label, background_color, text_color
    return "Extreme", "#b71c1c", "#ffffff"


def _badge_html(label, background_color, text_color):
    return (
        f'<span style="background-color:{background_color};'
        f"color:{text_color};padding:8px 16px;border-radius:16px;"
        f'font-weight:bold;display:inline-block;">{label}</span>'
    )


def _gauge_html(ffdi_value, background_color):
    capped_value = max(0.0, min(100.0, float(ffdi_value)))
    return (
        '<div style="width:100%;max-width:420px;background-color:#e0e0e0;'
        'border-radius:10px;overflow:hidden;height:22px;">'
        f'<div style="width:{capped_value:.2f}%;background-color:{background_color};'
        'height:22px;"></div>'
        '</div>'
        f'<p style="margin-top:6px;font-size:14px;color:#333333;">'
        f'FFDI: {ffdi_value:.2f}</p>'
    )


def calculate_ffdi(temperature, relative_humidity, wind_speed, drought_factor):
    try:
        temp_value = _to_float(temperature, "Temperature")
        rh_value = _to_float(relative_humidity, "Relative Humidity")
        wind_value = _to_float(wind_speed, "Wind Speed")
        df_value = _to_float(drought_factor, "Drought Factor")

        temp_value = _validate_range(temp_value, TEMP_MIN, TEMP_MAX, "Temperature")
        rh_value = _validate_range(rh_value, RH_MIN, RH_MAX, "Relative Humidity")
        wind_value = _validate_range(wind_value, WIND_MIN, WIND_MAX, "Wind Speed")
        df_value = _validate_range(df_value, DF_MIN, DF_MAX, "Drought Factor")

        effective_df = df_value if df_value > 0 else FFDI_EPSILON

        exponent = (
            -0.45
            + 0.987 * math.log(effective_df)
            - 0.0345 * rh_value
            + 0.0338 * temp_value
            + 0.0234 * wind_value
        )

        ffdi_raw = 2.0 * math.exp(exponent)

        if math.isnan(ffdi_raw) or math.isinf(ffdi_raw):
            raise ValueError("FFDI calculation produced an invalid result.")

        ffdi_display = round(ffdi_raw, 2)
        label, background_color, text_color = classify_ffdi(ffdi_display)

        return {
            "success": True,
            "ffdi": ffdi_display,
            "classification": label,
            "background_color": background_color,
            "text_color": text_color,
            "badge_html": _badge_html(label, background_color, text_color),
            "gauge_html": _gauge_html(ffdi_display, background_color),
            "error": "",
        }

    except ValueError as exc:
        return {
            "success": False,
            "ffdi": None,
            "classification": "Invalid",
            "background_color": "#d32f2f",
            "text_color": "#ffffff",
            "badge_html": "",
            "gauge_html": "",
            "error": str(exc),
        }
    except Exception as exc:
        return {
            "success": False,
            "ffdi": None,
            "classification": "Error",
            "background_color": "#d32f2f",
            "text_color": "#ffffff",
            "badge_html": "",
            "gauge_html": "",
            "error": f"Unexpected error: {exc}",
        }
