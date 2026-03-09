
def analyze(symbol: str) -> dict:
    score = (sum(ord(c) for c in symbol.upper()) % 100) / 100
    if score > 0.66:
        quality = "strong"
    elif score > 0.33:
        quality = "fair"
    else:
        quality = "weak"
    valuation = "expensive" if score > 0.7 else "reasonable" if score > 0.4 else "cheap"
    return {"quality": quality, "valuation": valuation, "quality_score": score}
