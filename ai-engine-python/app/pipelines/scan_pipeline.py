from datetime import datetime, timezone

from app.data.universe_provider import get_universe
from app.services.market_scanner import scan_symbols


def run_market_scan(universe: str, limit: int) -> dict:
    symbols = get_universe(universe)
    ranked = scan_symbols(symbols)[:limit]
    return {
        "universe": universe.upper(),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "opportunities": ranked,
    }
