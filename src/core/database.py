from collections.abc import AsyncGenerator

import structlog
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.core.settings import settings

logger = structlog.get_logger()

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=settings.APP_DEBUG,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise


async def init_database_client() -> None:
    try:
        async with engine.connect() as async_conn:
            await async_conn.execute(text("SELECT 1"))
            logger.info("database.connection.success", message="Conexão com o banco de dados bem sucedida.")
    except Exception as e:
        logger.error("database.connection.erro", error=str(e), message="Erro ao se conectar ao banco de dados.")
        raise


async def close_database_client() -> None:
    try:
        await engine.dispose()
        logger.info("database.connection.closed", message="Conexão com o banco de dados fechada.")
    except Exception as e:
        logger.error(
            "database.connection.close_error", error=str(e), message="Falha ao fechar conexões com o banco de dados."
        )
