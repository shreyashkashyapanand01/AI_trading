UNIVERSES = {
    "NIFTY50": ["TCS", "INFY", "RELIANCE", "HDFCBANK", "ICICIBANK", "LT", "SBIN", "ITC"],
    "BANKNIFTY": ["HDFCBANK", "ICICIBANK", "SBIN", "AXISBANK", "KOTAKBANK", "PNB"],
}


def get_universe(name: str) -> list[str]:
    return UNIVERSES.get(name.upper(), UNIVERSES["NIFTY50"])
