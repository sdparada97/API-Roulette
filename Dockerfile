# Base image
FROM python:3.9-slim-buster

WORKDIR /app

COPY app/* /app/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0","--port=80","--debug"]
