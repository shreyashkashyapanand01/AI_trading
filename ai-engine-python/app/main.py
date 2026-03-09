from fastapi import FastAPI

from app.api.portfolio_api import router as portfolio_router
from app.api.scan_api import router as scan_router
from app.api.stock_api import router as stock_router
from app.api.trade_api import router as trade_router

app = FastAPI(title="AI Trading Coach Engine", version="1.0.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(stock_router, prefix="/api/v1", tags=["stock"])
app.include_router(trade_router, prefix="/api/v1", tags=["trades"])
app.include_router(scan_router, prefix="/api/v1", tags=["scan"])
app.include_router(portfolio_router, prefix="/api/v1", tags=["portfolio"])
