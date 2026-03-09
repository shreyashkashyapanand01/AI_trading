import math
import random


def get_price_series(symbol: str, periods: int = 120) -> list[float]:
    seed = sum(ord(c) for c in symbol.upper())
    rng = random.Random(seed)
    base = 100 + seed % 200
    series: list[float] = []
    for i in range(periods):
        drift = math.sin(i / 18) * 0.4 + (seed % 7 - 3) * 0.02
        noise = rng.uniform(-0.9, 0.9)
        base = max(5, base + drift + noise)
        series.append(round(base, 2))
    return series
