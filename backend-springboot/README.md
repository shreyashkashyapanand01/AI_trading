# Spring Boot Backend (Planned)

This service is the central orchestrator:
- authentication + user workspace APIs,
- persistence of reports/alerts/holdings,
- scheduling for periodic monitoring,
- HTTP calls to Python AI engine.

## First implementation target
- Add `GET /test-ai` endpoint.
- Inside it call `POST http://localhost:8000/api/v1/analyze-stock`.
- Return and log payload to verify Java ↔ Python connectivity.

## Planned package structure
`com.aicoach.{controller,service,dto,entity,repository,config}`

See `docs/blueprint.md` for phased rollout.
