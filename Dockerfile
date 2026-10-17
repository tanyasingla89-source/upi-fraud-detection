FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies first (layer cache)
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy API source and model files
COPY api/ ./api/
COPY model/ ./model/

# Render injects $PORT at runtime; default to 8000 for local runs
ENV PORT=8000

EXPOSE ${PORT}

CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port ${PORT}"]
