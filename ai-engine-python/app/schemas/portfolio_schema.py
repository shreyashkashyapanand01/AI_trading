from pydantic import BaseModel, Field


class Holding(BaseModel):
    symbol: str
    quantity: float = Field(..., gt=0)
    avgPrice: float = Field(..., gt=0)


class PortfolioRequest(BaseModel):
    holdings: list[Holding]


class PortfolioResponse(BaseModel):
    generatedAt: str
    holdings: list[dict]
    summary: str
