# AI Trading Coach Blueprint (Consolidated)

## Product goal
Build an AI trading mentor that studies market conditions and trader behavior, then delivers explainable guidance and proactive risk alerts.

## Scope boundaries
- No trade execution
- No brokerage integration
- No exact price prediction

## Layered architecture
`React UI -> Spring Boot Controller -> FastAPI AI Engine -> Market/News Data`

- Spring Boot is responsible for auth, persistence, scheduling, and orchestration.
- FastAPI AI engine is responsible for analysis and explainable output generation.

## MVP delivered in this repo
### AI engine endpoints
- `POST /api/v1/analyze-stock`
- `POST /api/v1/analyze-trades`
- `POST /api/v1/scan-market`
- `POST /api/v1/analyze-portfolio`

### AI modules implemented
- Market analyzer (technical + sentiment + fundamental synthesis)
- Behaviour analyzer (metrics + mistake detection + coaching)
- Opportunity scanner (universe scan + ranking)
- Portfolio monitor (daily movement + risk/improvement labels)

## Recommended next implementation
1. Build Spring Boot controllers/services that call each endpoint.
2. Persist stock/trade reports and portfolio alerts in DB.
3. Add scheduler in Spring Boot for periodic portfolio monitoring.
4. Add React pages for search, upload, scan, holdings, and report history.
