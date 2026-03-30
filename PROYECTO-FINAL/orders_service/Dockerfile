# ---------- Stage 1: Builder ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Instalar poetry
RUN pip install --no-cache-dir poetry

# Copiar archivos de dependencias
COPY pyproject.toml poetry.lock* ./

# Configurar poetry para instalar en sistema
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim

WORKDIR /app

# Crear usuario no-root
RUN useradd -m appuser

# Copiar dependencias instaladas
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar código fuente
COPY src ./src
COPY alembic.ini .
COPY migrations ./migrations

# Variable de entorno
ENV PYTHONPATH=/app/src

# Cambiar a usuario seguro
USER appuser

EXPOSE 8000

CMD ["uvicorn", "orders_service.api.main:app", "--host", "0.0.0.0", "--port", "8000"]