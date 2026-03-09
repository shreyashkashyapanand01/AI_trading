from pydantic import BaseModel, Field


class StockAnalyzeRequest(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=20)


class StockAnalyzeResponse(BaseModel):
    symbol: str
    summary: str
    risk_level: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    signals: dict[str, str]
    indicators: dict[str, float]
