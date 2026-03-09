
def compute_metrics(trades: list[dict]) -> dict[str, float]:
    if not trades:
        return {
            "avgWinHoldMinutes": 0.0,
            "avgLossHoldMinutes": 0.0,
            "lossStreakFrequency": 0.0,
            "positionSizeVariance": 0.0,
        }

    wins = [t for t in trades if t["profitLoss"] > 0]
    losses = [t for t in trades if t["profitLoss"] <= 0]

    avg_win_hold = sum(t["holdingMinutes"] for t in wins) / len(wins) if wins else 0.0
    avg_loss_hold = sum(t["holdingMinutes"] for t in losses) / len(losses) if losses else 0.0

    loss_streaks = 0
    for i in range(1, len(trades)):
        if trades[i - 1]["profitLoss"] <= 0 and trades[i]["profitLoss"] <= 0:
            loss_streaks += 1

    sizes = [t["quantity"] * t["entryPrice"] for t in trades]
    avg_size = sum(sizes) / len(sizes)
    variance = sum((s - avg_size) ** 2 for s in sizes) / len(sizes)

    return {
        "avgWinHoldMinutes": round(avg_win_hold, 2),
        "avgLossHoldMinutes": round(avg_loss_hold, 2),
        "lossStreakFrequency": round(loss_streaks / max(1, len(trades) - 1), 2),
        "positionSizeVariance": round(variance**0.5 / avg_size if avg_size else 0.0, 2),
    }
