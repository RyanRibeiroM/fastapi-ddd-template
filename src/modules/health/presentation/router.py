import structlog
from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util.typing import Annotated

from src.core.database import get_db

logger = structlog.get_logger()
router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, summary="Endpoint para verificar se a API está online")
async def health_check(db: Annotated[AsyncSession, Depends(get_db)]) -> dict[str, str]:
    try:
        await db.execute(text("SELECT 1"))
        db_status = "online"
        logger.info("health.database.success", message="Sucesso ao verificar a saúde do banco de dados.")
    except Exception as e:
        db_status = "offline"
        logger.error("health.database.failed", error=str(e), message="Falha ao verificar a saúde do banco de dados.")
    return {"status": "ok", "api": "online", "database": db_status}
