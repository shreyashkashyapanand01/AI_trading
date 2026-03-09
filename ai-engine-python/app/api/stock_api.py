from fastapi import APIRouter

from app.pipelines.stock_pipeline import run_stock_analysis
from app.schemas.stock_schema import StockAnalyzeRequest, StockAnalyzeResponse

router = APIRouter()


@router.post("/analyze-stock", response_model=StockAnalyzeResponse)
def analyze_stock(payload: StockAnalyzeRequest) -> StockAnalyzeResponse:
    result = run_stock_analysis(payload.symbol.strip().upper())
    return StockAnalyzeResponse(**result)
