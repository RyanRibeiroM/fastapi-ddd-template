# fastapi-ddd-template
Esse projeto é um template em FastAPI que aplica os princípios de DDD (_Domain-Drive Design_) com logs estrurados.

### Execução com o docker
Esse projeto funciona em conteiners, logo é necessário que para executa-lo você tenha o docker instala e inicalizado na sua máquina.

### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/) e Docker Compose instalados.

### Passos para Inicialização

1. **Copie o arquivo de variáveis de ambiente:**
   Na raiz do projeto, crie o seu arquivo `.env` baseado no exemplo fornecido.
   ```bash
   cp .env.example .env
   ```

2. **Inicie todos os containers (em background):**
   ```bash
   docker compose up -d --build
   ```

3. **Acompanhe os logs da API:**
   ```bash
   docker compose logs -f api
   ```

A API estará disponível em: `http://localhost:8000`
O painel Swagger interativo estará em: `http://localhost:8000/docs`

4. **Para desligar a infraestrutura:**
   ```bash
   docker compose down
   ```
