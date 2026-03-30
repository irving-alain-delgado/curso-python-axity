FROM python:3.12-slim

WORKDIR /app

# Crear usuario no root
RUN useradd -m appuser

# Copiar archivos
COPY pyproject.toml poetry.lock* ./
COPY src ./src

# Instalar poetry e instalar dependencias
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# 👇 AGREGAR ESTO
ENV PYTHONPATH=/app/src

# Permisos
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "secure_api.main:app", "--host", "0.0.0.0", "--port", "8000"]