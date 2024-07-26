FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["sh", "-c", "celery -A task_manager worker --loglevel=info & celery -A task_manager flower --port=5555 & gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000"]
