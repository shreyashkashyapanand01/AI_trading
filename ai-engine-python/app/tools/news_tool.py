POSITIVE_KEYWORDS = {"beat", "upgrade", "growth", "profit", "expansion"}
NEGATIVE_KEYWORDS = {"downgrade", "fraud", "loss", "lawsuit", "decline"}


SYMBOL_NEWS = {
    "TCS": ["Strong profit growth expected", "Brokerage upgrade on IT recovery"],
    "INFY": ["Expansion in EU market", "Margin decline concerns remain"],
    "RELIANCE": ["Retail growth beat expectations"],
}


def get_headlines(symbol: str) -> list[str]:
    return SYMBOL_NEWS.get(symbol.upper(), ["No major headline trend detected"])


def score_sentiment(headlines: list[str]) -> float:
    score = 0
    for headline in headlines:
        words = {w.strip(".,").lower() for w in headline.split()}
        score += len(words & POSITIVE_KEYWORDS)
        score -= len(words & NEGATIVE_KEYWORDS)
    return float(score)
