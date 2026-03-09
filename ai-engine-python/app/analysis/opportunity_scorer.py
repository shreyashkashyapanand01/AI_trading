
def score_candidate(stock_result: dict) -> float:
    score = 0.0
    signals = stock_result["signals"]
    indicators = stock_result["indicators"]

    if signals["technical"] == "bullish":
        score += 40
    if signals["sentiment"] == "positive":
        score += 25
    if signals["fundamental"] in {"strong", "fair"}:
        score += 15

    rsi = indicators["rsi"]
    if 45 <= rsi <= 65:
        score += 20
    elif rsi > 75:
        score -= 15

    return round(max(0, min(100, score)), 2)
