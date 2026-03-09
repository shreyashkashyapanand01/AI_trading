from datetime import datetime, timezone
from uuid import uuid4

from app.agents.behaviour_agent import coach
from app.analysis.metrics_calculator import compute_metrics
from app.analysis.pattern_detector import detect_mistakes


def run_trade_analysis(trades: list[dict]) -> dict:
    metrics = compute_metrics(trades)
    mistakes = detect_mistakes(trades, metrics)
    coaching = coach(mistakes)

    risk_score = int(min(100, 20 + len(mistakes) * 15 + metrics["lossStreakFrequency"] * 20))

    return {
        "analysisId": uuid4().hex[:8],
        "generatedAt": datetime.now(timezone.utc),
        "riskScore": risk_score,
        "traderType": coaching["traderType"],
        "mistakes": mistakes,
        "metrics": metrics,
        "summary": coaching["summary"],
        "suggestions": coaching["suggestions"],
    }
