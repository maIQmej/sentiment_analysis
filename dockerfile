# ============================
#  Stage 1: builder
# ============================
FROM python:3.12-slim AS builder
WORKDIR /app

# Paquetes de sistema necesarios para compilar (ligeros)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl && \
    rm -rf /var/lib/apt/lists/*

# Instala deps en un prefix temporal para copiar al stage final
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

# ============================
#  Stage 2: runtime
# ============================
FROM python:3.12-slim
WORKDIR /app

# Copia las dependencias ya instaladas
COPY --from=builder /install /usr/local

# Copia solo tu código
COPY app/ app/
COPY client.py .
COPY requirements.txt .

# Evita prompts y define cache de HuggingFace en el contenedor
ENV HF_HOME=/root/.cache/huggingface
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Arranque del servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
