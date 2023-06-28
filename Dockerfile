# Base image
FROM python:3.9-slim-buster

WORKDIR /app

COPY api /app/api/
COPY run.py /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=/app/api/

CMD ["python", "run.py"]
