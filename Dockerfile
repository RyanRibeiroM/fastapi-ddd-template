FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY --from=ghcr.io/astral-sh/uv:0.7 /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY ./src ./src
COPY ./migrations ./migrations
COPY alembic.ini ./

RUN adduser --disabled-password  --gecos "" --uid 1000 appuser && chown -R appuser:appuser /src

USER appuser

EXPOSE 8000

CMD [ "uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]
