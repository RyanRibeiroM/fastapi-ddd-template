from fastapi import FastAPI

from src.modules.health.presentation.router import router as health_router

app = FastAPI(
    title="DDD Template",
    swagger_ui_parameters={"persistAuthorization": True, "displayRequestDuration": True, "filter": True},
)

app.include_router(health_router, tags=["Monitoramento"])
