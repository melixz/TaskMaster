FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["gunicorn", "TaskMaster.wsgi:application", "--bind", "0.0.0.0:8000"]
