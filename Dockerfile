# Dockerfile for DotaMetaAnalyzer
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
COPY requirements.txt ./

WORKDIR /app

FROM python:3.11-slim

