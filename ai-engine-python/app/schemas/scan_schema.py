from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    universe: str = Field(default="NIFTY50")
    limit: int = Field(default=5, ge=1, le=20)


class OpportunityItem(BaseModel):
    symbol: str
    score: float
    summary: str
    signals: dict[str, str]


class ScanResponse(BaseModel):
    universe: str
    generatedAt: str
    opportunities: list[OpportunityItem]
