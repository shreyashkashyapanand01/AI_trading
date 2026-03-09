from app.tools.indicator_tool import momentum, rsi, sma, volatility


def analyze(price_series: list[float]) -> dict:
    short = sma(price_series, 20)
    long = sma(price_series, 50)
    mom = momentum(price_series)
    vol = volatility(price_series)
    rsi_val = rsi(price_series)

    trend = "bullish" if short > long else "bearish"
    if abs(short - long) < 0.5:
        trend = "sideways"

    return {
        "trend": trend,
        "momentum": mom,
        "volatility": vol,
        "rsi": rsi_val,
    }
