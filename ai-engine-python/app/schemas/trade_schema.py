from datetime import datetime

from pydantic import BaseModel, Field


class TradeItem(BaseModel):
    symbol: str
    side: str
    quantity: float = Field(..., gt=0)
    entryPrice: float = Field(..., gt=0)
    exitPrice: float = Field(..., gt=0)
    entryTime: datetime
    exitTime: datetime
    holdingMinutes: float = Field(..., ge=0)
    profitLoss: float


class TradeAnalyzeRequest(BaseModel):
    trades: list[TradeItem] = Field(default_factory=list)


class TradeAnalyzeResponse(BaseModel):
    analysisId: str
    generatedAt: datetime
    riskScore: int
    traderType: str
    mistakes: list[str]
    metrics: dict[str, float]
    summary: str
    suggestions: list[str]
