from datetime import datetime, timezone

from app.analysis.daily_movement_analyzer import analyze_movement
from app.tools.market_data_tool import get_price_series


def run_portfolio_analysis(holdings: list[dict]) -> dict:
    rows = []
    risk_count = 0
    for holding in holdings:
        series = get_price_series(holding["symbol"])
        movement = analyze_movement(series, holding["avgPrice"])
        if movement["signal"] == "risk_increasing":
            risk_count += 1
        rows.append(
            {
                "symbol": holding["symbol"].upper(),
                "quantity": holding["quantity"],
                "avgPrice": holding["avgPrice"],
                **movement,
            }
        )

    summary = (
        f"{risk_count} holding(s) show increasing risk."
        if risk_count
        else "No immediate risk spikes detected across holdings."
    )

    return {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "holdings": rows,
        "summary": summary,
    }
