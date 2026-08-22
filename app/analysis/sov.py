def calculate_sov(recommendations: dict) -> dict:

    total = sum(recommendations.values())

    if total == 0:
        return {
            brand: 0.0
            for brand in recommendations
        }

    return {
        brand: round((count / total) * 100, 2)
        for brand, count in recommendations.items()
    }