# ---------- Stage 1: Builder ----------
FROM python:3.12 as builder

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

COPY src/packaging_lab ./packaging_lab

CMD ["uvicorn", "packaging_lab.main:app", "--host", "0.0.0.0", "--port", "8000"]