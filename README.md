# TaskMaster

## Описание проекта

`TaskMaster` - это система управления задачами, включающая API для управления задачами, асинхронную обработку задач,
мониторинг задач, поиск задач и контейнеризацию приложения. Проект создан с использованием Django, Django REST
Framework, Celery, RabbitMQ, Flower, Elasticsearch и Docker.

## Установка

```bash
git clone https://github.com/melixz/TaskMaster
cd TaskMaster
pip install -r requirements.txt
```

## Использование

1. Настройте переменные окружения в файле `.env`:
   ```sh
   POSTGRES_USER=ваш_пользователь
   POSTGRES_PASSWORD=ваш_пароль
   POSTGRES_DB=ваша_бд
   POSTGRES_HOST=ваш_хост
   CELERY_BROKER_URL=amqp://rabbitmq
   CELERY_RESULT_BACKEND=rpc://
   ```

2. Запустите Docker контейнеры:
   ```sh
   docker-compose up --build
   ```

3. Взаимодействуйте с API через endpoints:
    - Получение списка задач: `GET /api/tasks/`
    - Создание задачи: `POST /api/tasks/`
    - Обновление задачи: `PUT /api/tasks/{id}/`
    - Удаление задачи: `DELETE /api/tasks/{id}/`
    - Запуск обработки задачи: `POST /api/tasks/{id}/start_processing/`

4. Мониторинг Celery задач доступен по адресу: `http://localhost:5555`

5. Поиск задач через Elasticsearch:
   ```sh
   curl -X GET "localhost:9200/tasks/_search?q=title:НазваниеЗадачи"
   ```

### Таблица сервисов

| Сервис                     | Локальный хост          | Описание функций                                                              |
|----------------------------|-------------------------|-------------------------------------------------------------------------------|
| API задач                  | `http://localhost:8000` | Управление задачами: создание, чтение, обновление, удаление, запуск обработки |
| Celery мониторинг (Flower) | `http://localhost:5555` | Мониторинг состояния задач и активности воркеров                              |
| Elasticsearch              | `http://localhost:9200` | Поиск задач по названию и описанию                                            |

## Технологии

- Python 3.9+
- Django
- Django REST Framework
- Celery: для асинхронной обработки задач
- RabbitMQ: в качестве брокера сообщений для Celery
- Flower: для мониторинга Celery задач
- Elasticsearch: для поиска задач
- PostgreSQL: в качестве базы данных
- Docker и Docker-compose: для контейнеризации приложения

## Текущие возможности

- Создание, чтение, обновление и удаление задач через REST API
- Асинхронная обработка задач с использованием Celery и RabbitMQ
- Мониторинг состояния задач через Flower
- Поиск задач по названию и описанию через Elasticsearch
- Контейнеризация всех компонентов системы с использованием Docker

## Цель проекта

Проект предназначен для управления задачами, автоматизации их обработки и обеспечения удобного интерфейса для
мониторинга и поиска задач.

## Примеры API запросов

### Создание задачи

```sh
curl -X POST http://localhost:8000/api/tasks/ \
-H "Content-Type: application/json" \
-d '{"title": "Новая задача", "description": "Описание задачи"}'
```

### Получение списка задач

```sh
curl -X GET http://localhost:8000/api/tasks/
```

### Обновление задачи

```sh
curl -X PUT http://localhost:8000/api/tasks/1/ \
-H "Content-Type: application/json" \
-d '{"title": "Обновленная задача", "description": "Обновленное описание", "status": "in_progress"}'
```

### Удаление задачи

```sh
curl -X DELETE http://localhost:8000/api/tasks/1/
```

### Запуск обработки задачи

```sh
curl -X POST http://localhost:8000/api/tasks/1/start_processing/
```

### Поиск задач через Elasticsearch

```sh
curl -X GET "localhost:9200/tasks/_search?q=title:НазваниеЗадачи"
```

## Демонстрация работы Flower

Для мониторинга Celery задач через Flower, откройте веб-браузер и перейдите по адресу:

```sh
http://localhost:5555
```