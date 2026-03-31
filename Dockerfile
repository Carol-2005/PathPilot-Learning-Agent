# Use official Python slim image — smaller = faster cold starts on Cloud Run
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (Docker caches this layer — rebuilds are faster)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY pathpilot/ ./pathpilot/
COPY mcp_server/ ./mcp_server/

# Cloud Run sets PORT env var automatically (default 8080)
ENV PORT=8080

# Tell Python not to buffer output (so logs appear immediately in Cloud Run)
ENV PYTHONUNBUFFERED=1

# ADK web server command — host 0.0.0.0 makes it accessible outside the container
CMD ["sh", "-c", "adk web --host 0.0.0.0 --port ${PORT}"]