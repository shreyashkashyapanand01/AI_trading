from app.agents.decision_agent import decide
from app.agents.fundamental_agent import analyze as fundamental_analyze
from app.agents.news_agent import analyze as news_analyze
from app.agents.technical_agent import analyze as technical_analyze
from app.tools.market_data_tool import get_price_series


def run_stock_analysis(symbol: str) -> dict:
    series = get_price_series(symbol)
    technical = technical_analyze(series)
    news = news_analyze(symbol)
    fundamental = fundamental_analyze(symbol)
    decision = decide(technical, news, fundamental)

    return {
        "symbol": symbol.upper(),
        "summary": decision["summary"],
        "risk_level": decision["risk_level"],
        "confidence": decision["confidence"],
        "signals": {
            "technical": technical["trend"],
            "sentiment": news["sentiment"],
            "fundamental": fundamental["quality"],
        },
        "indicators": {
            "momentum": round(technical["momentum"], 2),
            "volatility": round(technical["volatility"], 2),
            "rsi": round(technical["rsi"], 2),
            "sentiment_score": round(news["sentiment_score"], 2),
        },
    }
