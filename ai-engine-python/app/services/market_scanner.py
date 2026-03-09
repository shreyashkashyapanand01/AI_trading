from app.analysis.opportunity_scorer import score_candidate
from app.pipelines.stock_pipeline import run_stock_analysis


def scan_symbols(symbols: list[str]) -> list[dict]:
    output = []
    for symbol in symbols:
        analysis = run_stock_analysis(symbol)
        score = score_candidate(analysis)
        output.append(
            {
                "symbol": analysis["symbol"],
                "score": score,
                "summary": analysis["summary"],
                "signals": analysis["signals"],
            }
        )
    output.sort(key=lambda item: item["score"], reverse=True)
    return output
