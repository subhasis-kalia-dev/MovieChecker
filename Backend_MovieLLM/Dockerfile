# === Backend Dockerfile for uv + FastAPI ===
FROM python:3.14-slim


WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Install uv
RUN pip install --no-cache-dir uv

# Install dependencies using uv directly (no process substitution)
RUN uv pip install --system .

# Copy backend source code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI via uv
CMD ["uv", "run", "fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
