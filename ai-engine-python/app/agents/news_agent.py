from app.tools.news_tool import get_headlines, score_sentiment


def analyze(symbol: str) -> dict:
    headlines = get_headlines(symbol)
    score = score_sentiment(headlines)
    sentiment = "positive" if score > 0 else "negative" if score < 0 else "neutral"
    return {"sentiment": sentiment, "sentiment_score": score, "headlines": headlines}
