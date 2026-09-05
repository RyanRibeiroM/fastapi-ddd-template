from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, summary="Endpoint para verificar se a API está online")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "api": "online"}
