🧾 Orders Service — Arquitectura Hexagonal (Clean Architecture)
Servicio backend de gestión de órdenes implementado con Arquitectura Hexagonal (Clean Architecture) usando:

✅ FastAPI
✅ SQLAlchemy
✅ Alembic
✅ Pydantic Settings
✅ Docker multistage (non-root)
✅ CI/CD con GitHub Actions
✅ Ruff + MyPy + Pytest
✅ Auditoría de dependencias (pip-audit)

🏗 Arquitectura
El proyecto sigue el patrón Hexagonal / Ports & Adapters.

                 ┌────────────────────┐
                 │       FastAPI      │  ← Adaptador HTTP
                 └─────────┬──────────┘
                           │
                 ┌─────────▼──────────┐
                 │    Application     │  ← Casos de uso
                 │  (Use Cases)       │
                 └─────────┬──────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
┌───────▼────────┐  ┌──────▼────────┐  ┌──────▼────────┐
│ Repository Port│  │ Event Port     │  │ Domain Model   │
│ (Interface)    │  │ (Interface)    │  │ (Entities)     │
└───────┬────────┘  └──────┬────────┘  └───────────────┘
        │                  │
┌───────▼────────┐  ┌──────▼────────┐
│ SQLAlchemy     │  │ RabbitMQ /    │
│ Adapter        │  │ Dummy Adapter │
└────────────────┘  └───────────────┘

Capas
Domain → Entidades y reglas de negocio
Application → Casos de uso y puertos
Infrastructure → DB, configuración, mensajería
API → Adaptador HTTP (FastAPI)

📂 Estructura del Proyecto

PROYECTO-FINAL/orders_service/
│
├── src/orders_service/
│   ├── domain/
│   ├── application/
│   │   ├── ports/
│   │   └── use_cases/
│   ├── infrastructure/
│   │   ├── db/
│   │   └── config.py
│   └── api/
│
├── migrations/
├── tests/
├── Dockerfile
├── alembic.ini
└── pyproject.toml

🚀 Ejecutar Localmente
1️⃣ Instalar dependencias
poetry install

2️⃣ Definir variable de entorno
export DATABASE_URL=sqlite:///./orders.db
En Windows:
$env:DATABASE_URL="sqlite:///./orders.db"

3️⃣ Ejecutar migraciones
poetry run alembic upgrade head

4️⃣ Levantar servidor
poetry run uvicorn orders_service.api.main:app --reload

Abrir:
http://127.0.0.1:8000/docs

🐳 Ejecutar con Docker
Construir imagen
docker build -t orders-service .

Ejecutar contenedor
docker run -p 8000:8000 \ -e DATABASE_URL=sqlite:///./orders.db \ orders-service

✅ El contenedor corre como usuario non-root (appuser).

🧪 Ejecutar Tests
poetry run pytest --cov

Incluye:

✅ Unit tests (dominio)
✅ Unit tests (casos de uso con mocks)
✅ Integration tests (API)

✅ Calidad de Código
Lint
poetry run ruff check .

Tipado estático
poetry run mypy src

Auditoría de dependencias
poetry run pip-audit

🤖 CI/CD
Pipeline implementado con GitHub Actions:

✅ Ruff
✅ MyPy
✅ Pytest + Coverage
✅ pip-audit
El pipeline se ejecuta automáticamente en cada push o pull request.

🔐 Seguridad
Configuración desacoplada con pydantic-settings
Variables de entorno obligatorias
No se almacenan secretos en el código
Docker con usuario non-root
Auditoría automática de dependencias

📊 Decisiones Técnicas
Arquitectura Hexagonal para bajo acoplamiento
Repository Pattern para separar dominio de infraestructura
Alembic para versionado de esquema
SQLite para desarrollo (migrable a PostgreSQL)
FastAPI por tipado fuerte y documentación automática
Poetry para gestión moderna de dependencias

🏁 Estado del Proyecto
✅ Listo para producción básica
✅ Arquitectura limpia validada
✅ Calidad automatizada
✅ CI en verde
✅ Docker seguro

👨‍💻 Autor
Irving Delgado
Curso Python Backend — Axity
