# FastAPI CRUD Service

Простой REST API сервис с CRUD операциями и SQLite базой данных.

## Установка
```bash
# Клонировать репозиторий
git clone https://github.com/kif1r4ek/fastapi-crud-service.git
cd fastapi-crud-service

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Установить зависимости
pip install -r requirements.txt
```

## Запуск
```bash
uvicorn main:app --reload --port 8000
```

## API Endpoints

| Метод  | URL              | Описание                    |
|--------|------------------|-----------------------------|
| POST   | /items/          | Создать новый элемент       |
| GET    | /items/          | Получить все элементы       |
| GET    | /items/{id}      | Получить элемент по ID      |
| PUT    | /items/{id}      | Обновить элемент            |
| DELETE | /items/{id}      | Удалить элемент             |

## Документация API

После запуска доступна по адресу: http://localhost:8000/docs