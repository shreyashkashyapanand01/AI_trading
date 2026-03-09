from fastapi import APIRouter

from app.pipelines.portfolio_pipeline import run_portfolio_analysis
from app.schemas.portfolio_schema import PortfolioRequest, PortfolioResponse

router = APIRouter()


@router.post("/analyze-portfolio", response_model=PortfolioResponse)
def analyze_portfolio(payload: PortfolioRequest) -> PortfolioResponse:
    holdings = [h.model_dump() for h in payload.holdings]
    result = run_portfolio_analysis(holdings)
    return PortfolioResponse(**result)
