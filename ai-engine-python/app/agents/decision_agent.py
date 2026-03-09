
def decide(technical: dict, news: dict, fundamental: dict) -> dict:
    trend = technical["trend"]
    rsi = technical["rsi"]
    sentiment = news["sentiment"]
    valuation = fundamental["valuation"]

    risk_level = "medium"
    notes: list[str] = []

    if trend == "bullish" and sentiment == "positive":
        notes.append("Structure is improving with supportive sentiment")
    if rsi > 70:
        notes.append("Price is overheated; short-term pullback risk is elevated")
        risk_level = "high"
    elif rsi < 35:
        notes.append("Stock is oversold; downside pressure may be maturing")

    if trend == "bearish":
        notes.append("Trend remains weak; avoid aggressive entries")
        risk_level = "high"

    if valuation == "expensive":
        notes.append("Valuation looks stretched relative to baseline")
    elif valuation == "cheap":
        notes.append("Valuation appears favorable for deeper review")

    if not notes:
        notes.append("Mixed signals: monitor for clearer confirmation")

    confidence = 0.55
    if trend == "bullish" and sentiment == "positive":
        confidence += 0.15
    if risk_level == "high":
        confidence -= 0.1

    return {
        "summary": " ".join(notes),
        "risk_level": risk_level,
        "confidence": max(0.0, min(1.0, confidence)),
    }
