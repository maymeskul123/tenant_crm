# Tenant CRM

Система управления арендаторами и заказами с REST API.

## Стек технологий

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Containerization**: Docker & Docker Compose
- **Python**: 3.11+

## Установка и запуск

### Требования
- Docker
- Docker Compose

### Быстрый старт

```bash
# Клонируйте репозиторий
git clone https://github.com/maymeskul123/tenant_crm.git
cd tenant_crm

# Запустите контейнеры
docker-compose up --build

# API доступен на http://localhost:8000
```

## API Endpoints

### Здоровье приложения
```bash
GET /health
```

### Арендаторы (Tenants)

**Создать арендатора**
```bash
POST /tenants/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "company_name": "Acme Corp",
  "is_active": true
}
```

**Получить всех арендаторов**
```bash
GET /tenants/
```

**Получить арендатора по ID**
```bash
GET /tenants/{tenant_id}
```

**Обновить арендатора**
```bash
PUT /tenants/{tenant_id}
Content-Type: application/json

{
  "name": "Jane Doe",
  "is_active": false
}
```

**Удалить арендатора**
```bash
DELETE /tenants/{tenant_id}
```

### Заказы (Orders)

Coming soon...

## Структура проекта

```
tenant_crm/
├── app/
│   ├── models/           # SQLAlchemy моделей
│   ├── schemas/          # Pydantic схемы
│   ├── routes/           # API маршруты
│   ├── crud/             # Операции с БД
│   ├── database.py       # Конфигурация БД
│   └── main.py           # FastAPI приложение
├── docker-compose.yml    # Docker конфиг
├── Dockerfile            # Docker образ
├── requirements.txt      # Python зависимости
└── README.md
```

## Разработка

### Запуск в режиме разработки

```bash
docker-compose up
docker-compose logs -f api
```

### Документация API

Интерактивная документация доступна на:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Лицензия

MIT

## Автор

[маймескул123](https://github.com/maymeskul123)