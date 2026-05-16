import requests
from django.core.cache import cache
from rest_framework.exceptions import ValidationError

AIC_BASE_URL = "https://api.artic.edu/api/v1/artworks"


def fetch_artwork(external_id: int) -> dict:
    cache_key = f"aic_artwork_{external_id}"
    cached = cache.get(cache_key)
    if cached:
        return cached

    response = requests.get(f"{AIC_BASE_URL}/{external_id}", params={"fields": "id,title"})

    if response.status_code == 404:
        raise ValidationError(f"Artwork {external_id} not found in Art Institute API.")

    response.raise_for_status()

    data = response.json()["data"]
    cache.set(cache_key, data, timeout=60 * 60)
    return data