
def sma(values: list[float], window: int) -> float:
    return sum(values[-window:]) / window


def momentum(values: list[float], lookback: int = 10) -> float:
    start = values[-lookback]
    end = values[-1]
    return ((end - start) / start) * 100 if start else 0.0


def volatility(values: list[float], window: int = 20) -> float:
    chunk = values[-window:]
    avg = sum(chunk) / len(chunk)
    var = sum((x - avg) ** 2 for x in chunk) / len(chunk)
    return var**0.5


def rsi(values: list[float], window: int = 14) -> float:
    changes = [values[i] - values[i - 1] for i in range(1, len(values))]
    gains = [c for c in changes[-window:] if c > 0]
    losses = [-c for c in changes[-window:] if c < 0]
    avg_gain = sum(gains) / window if gains else 0.0001
    avg_loss = sum(losses) / window if losses else 0.0001
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
