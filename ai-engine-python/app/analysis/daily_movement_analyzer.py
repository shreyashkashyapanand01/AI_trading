
def analyze_movement(series: list[float], avg_price: float) -> dict:
    current = series[-1]
    daily_change_pct = ((series[-1] - series[-2]) / series[-2]) * 100 if len(series) > 1 else 0.0
    pnl_pct = ((current - avg_price) / avg_price) * 100

    signal = "stable"
    if daily_change_pct < -2.5:
        signal = "risk_increasing"
    elif daily_change_pct > 2.5:
        signal = "improving_conditions"

    return {
        "currentPrice": round(current, 2),
        "dailyChangePct": round(daily_change_pct, 2),
        "unrealizedPnlPct": round(pnl_pct, 2),
        "signal": signal,
    }
