FROM python:3.11.12-alpine3.21
WORKDIR /app
RUN apk add --no-cache --no-check-certificate \
    postgresql-dev \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
