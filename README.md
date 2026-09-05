# fastapi-ddd-template

Para executar o projeto é necessário que o UV esteja instalado na sua máquina.
execute: 
```cmd
    uv sync
```
O uv irá instalar todas as dependências do projeto.

para inicializar:
```cmd
    uv run uvicorn src.main:app --app-dir . --reload
```

A api estara funcionando em **http://127.0.0.1:8000**

Com docker: 
```cmd
    docker compose up -d --build
```