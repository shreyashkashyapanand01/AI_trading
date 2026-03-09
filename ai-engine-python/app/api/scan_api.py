from fastapi import APIRouter

from app.pipelines.scan_pipeline import run_market_scan
from app.schemas.scan_schema import ScanRequest, ScanResponse

router = APIRouter()


@router.post("/scan-market", response_model=ScanResponse)
def scan_market(payload: ScanRequest) -> ScanResponse:
    result = run_market_scan(payload.universe, payload.limit)
    return ScanResponse(**result)
