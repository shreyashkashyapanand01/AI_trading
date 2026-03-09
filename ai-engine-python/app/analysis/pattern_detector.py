
def detect_mistakes(trades: list[dict], metrics: dict[str, float]) -> list[str]:
    mistakes: list[str] = []
    if metrics["avgLossHoldMinutes"] > metrics["avgWinHoldMinutes"] * 1.8 and metrics["avgWinHoldMinutes"] > 0:
        mistakes.extend(["cutting_winners_early", "holding_losers_too_long"])

    if metrics["lossStreakFrequency"] > 0.35:
        mistakes.append("revenge_trading")

    if metrics["positionSizeVariance"] > 0.45:
        mistakes.append("inconsistent_position_size")

    if len(trades) > 25:
        mistakes.append("overtrading")

    return sorted(set(mistakes))
