FROM cgr.dev/chainguard/python:latest-dev AS builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app

#RUN python -m venv /app/venv
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/dependencies -r requirements.txt
# Stage 2: Final Runtime Image
FROM cgr.dev/chainguard/python:latest

WORKDIR /app
ENV PYTHONUNBUFFERED=1
#ENV PATH="/app/venv/bin:$PATH"
ENV PYTHONPATH=/app/dependencies
COPY src/app.py ./
COPY --from=builder /app/dependencies /app/dependencies


ENTRYPOINT [ "python", "/app/app.py" ]
