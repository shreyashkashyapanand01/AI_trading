SUGGESTION_MAP = {
    "cutting_winners_early": "Use rule-based take-profit targets instead of emotional exits.",
    "holding_losers_too_long": "Define a hard stop-loss before entering each trade.",
    "revenge_trading": "Pause after a loss streak and enforce a cooldown window.",
    "inconsistent_position_size": "Use fixed risk-per-trade (e.g., 1% of capital).",
    "overtrading": "Reduce daily trade count and require setup quality checklist.",
}


def coach(mistakes: list[str]) -> dict:
    if not mistakes:
        return {
            "traderType": "disciplined",
            "summary": "No major behavioural red flags detected in this sample.",
            "suggestions": ["Continue journaling and reviewing trade execution weekly."],
        }

    trader_type = "emotional" if "revenge_trading" in mistakes else "inconsistent"
    suggestions = [SUGGESTION_MAP[m] for m in mistakes if m in SUGGESTION_MAP]
    summary = "Detected behavioural patterns impacting consistency: " + ", ".join(mistakes)
    return {"traderType": trader_type, "summary": summary, "suggestions": suggestions}
