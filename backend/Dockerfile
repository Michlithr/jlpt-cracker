# Stage 1: The Builder Stage
FROM python:3.11-slim AS builder

# 🛑 CRITICAL FIX: Install system dependencies needed for building asyncpg (libpq-dev) 
# and the C compiler (build-essential)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

# This step will now succeed because the necessary C tools are available
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

# Stage 2: The Runtime Stage (This part is now correct)
FROM python:3.11-slim AS runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY . .

# This command is correct and will now find uvicorn
CMD ["/app/.venv/bin/uvicorn", "jlpt_cracker.main:app", "--host", "0.0.0.0", "--port", "8000"]