from fastapi import APIRouter

from app.pipelines.trade_pipeline import run_trade_analysis
from app.schemas.trade_schema import TradeAnalyzeRequest, TradeAnalyzeResponse

router = APIRouter()


@router.post("/analyze-trades", response_model=TradeAnalyzeResponse)
def analyze_trades(payload: TradeAnalyzeRequest) -> TradeAnalyzeResponse:
    trades = [trade.model_dump() for trade in payload.trades]
    result = run_trade_analysis(trades)
    return TradeAnalyzeResponse(**result)
