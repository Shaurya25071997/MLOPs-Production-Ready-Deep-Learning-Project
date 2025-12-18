FROM python:3.9-slim

WORKDIR /app

COPY . /app

# 🔥 THIS IS THE FIX
ENV PYTHONPATH="/app/src"

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
