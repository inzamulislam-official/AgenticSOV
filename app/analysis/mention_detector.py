import re


def detect_mentions(text: str, brands: list[str]) -> dict:
    results = {}

    text_lower = text.lower()

    for brand in brands:
        pattern = r"\b" + re.escape(brand.lower()) + r"\b"

        matches = re.findall(pattern, text_lower)

        results[brand] = len(matches)

    return results