FROM python:3.9-slim

WORKDIR /app

COPY requirements-infer.txt .
RUN pip install --no-cache-dir -r requirements-infer.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]