from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analyze_stock() -> None:
    response = client.post("/api/v1/analyze-stock", json={"symbol": "tcs"})
    body = response.json()
    assert response.status_code == 200
    assert body["symbol"] == "TCS"
    assert set(body["signals"].keys()) == {"technical", "sentiment", "fundamental"}
    assert set(body["indicators"].keys()) >= {"momentum", "volatility", "rsi"}


def test_analyze_trades() -> None:
    payload = {
        "trades": [
            {
                "symbol": "INFY",
                "side": "BUY",
                "quantity": 10,
                "entryPrice": 1500,
                "exitPrice": 1490,
                "entryTime": "2024-01-10T10:15:22Z",
                "exitTime": "2024-01-10T11:02:10Z",
                "holdingMinutes": 47,
                "profitLoss": -100,
            },
            {
                "symbol": "TCS",
                "side": "BUY",
                "quantity": 10,
                "entryPrice": 3500,
                "exitPrice": 3525,
                "entryTime": "2024-01-11T10:15:22Z",
                "exitTime": "2024-01-11T10:25:10Z",
                "holdingMinutes": 10,
                "profitLoss": 250,
            },
        ]
    }
    response = client.post("/api/v1/analyze-trades", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "analysisId" in body
    assert "riskScore" in body
    assert "metrics" in body


def test_scan_market() -> None:
    response = client.post("/api/v1/scan-market", json={"universe": "NIFTY50", "limit": 3})
    assert response.status_code == 200
    body = response.json()
    assert len(body["opportunities"]) == 3


def test_analyze_portfolio() -> None:
    response = client.post(
        "/api/v1/analyze-portfolio",
        json={"holdings": [{"symbol": "TCS", "quantity": 5, "avgPrice": 3500}]},
    )
    assert response.status_code == 200
    body = response.json()
    assert len(body["holdings"]) == 1
    assert "summary" in body
