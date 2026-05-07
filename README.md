# Tenant CRM API

Multi-tenant CRM система для централізації обліку замовлень малого бізнесу.

## 🚀 Швидкий старт

### Вимоги
- Docker & Docker Compose
- Python 3.11+ (для локального розробки)
- PostgreSQL 15+

### Установка та запуск

1. Клонуйте репозиторій:
```bash
git clone <repository-url>
cd tenant_crm
```

2. Створіть `.env` файл:
```bash
cp .env.example .env
```

3. Запустіть приложення з Docker Compose:
```bash
docker-compose up -d
```

4. Перевірте здоров'я API:
```bash
curl http://localhost:8000/health
```

5. Відкрийте документацію:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Локальний розробка

1. Створіть вірт. оточення:
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
```

2. Установіть залежності:
```bash
pip install -r requirements.txt
```

3. Запустіть PostgreSQL локально або через Docker:
```bash
docker run --name tenant_crm_db -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:15
```

4. Запустіть сервер розробки:
```bash
uvicorn app.main:app --reload
```

## 📁 Структура проекту

```
tenant_crm/
├── app/
│   ├── models/          # SQLAlchemy моделі
│   ├── schemas/         # Pydantic валідаційні схемы
│   ├── crud/            # Логіка доступу до БД
│   ├── routes/          # API ендпоінти
│   ├── main.py          # FastAPI додаток
│   ├── config.py        # Конфігурація
│   └── database.py      # БД з'єднання
├── tests/               # Юніт-тести
├── docs/                # Документація
├── docker/              # Docker файли
├── docker-compose.yml   # Docker Compose конфіг
└── requirements.txt     # Python залежності
```

## 📚 Документація

- [Архітектура рішення](docs/ARCHITECTURE.md)
- [API Design](docs/API_DESIGN.md)
- [Схема БД](docs/DATABASE_SCHEMA.md)
- [Декомпозиція задач](docs/TASKS.md)
- [Стратегія AI](docs/AI_STRATEGY.md)

## 🧪 Тестування

Запустіть тести:
```bash
pytest
```

З покриттям:
```bash
pytest --cov=app tests/
```

## 🐳 Docker команды

Запуск:
```bash
docker-compose up
```

Зупинка:
```bash
docker-compose down
```

Перебудова образів:
```bash
docker-compose up --build
```

Логи:
```bash
docker-compose logs -f api
```

## 🔌 API endpoints

### Tenants
- `GET /tenants` - Список всіх tenants
- `GET /tenants/{id}` - Отримати tenant з замовленнями
- `POST /tenants` - Створити tenant
- `PUT /tenants/{id}` - Оновити tenant
- `DELETE /tenants/{id}` - Видалити tenant

### Orders
- `GET /orders` - Список всіх замовлень
- `GET /orders/{id}` - Отримати замовлення
- `GET /orders/tenant/{tenant_id}` - Замовлення tenant'а
- `POST /orders` - Створити замовлення
- `PUT /orders/{id}` - Оновити замовлення
- `DELETE /orders/{id}` - Видалити замовлення

## 📝 Приклади запитів

### Створити tenant:
```bash
curl -X POST http://localhost:8000/tenants \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "company_name": "Acme Corp"
  }'
```

### Створити замовлення:
```bash
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": 1,
    "order_number": "ORD-001",
    "description": "Web development",
    "amount": 5000.00,
    "status": "pending"
  }'
```

## 🛠 Технологічний стек

- **FastAPI** - Web фреймворк
- **SQLAlchemy** - ORM
- **PostgreSQL** - База даних
- **Pydantic** - Валідація даних
- **Pytest** - Тестування
- **Docker** - Контейнеризація

## 📄 Ліцензія

MIT

## ✋ Contributing

Сприятливі до pull requests!

# Архітектура рішення

## 📐 Загальна архітектура

Система побудована на основі багатошарової архітектури (Layered Architecture) з розділенням відповідальності:

```
┌─────────────────────────────────────┐
│       Presentation Layer (Routes)   │  API Endpoints
├─────────────────────────────────────┤
│       Business Logic Layer (CRUD)   │  Операції над даними
├─────────────────────────────────────┤
│       Data Access Layer (Models)    │  SQLAlchemy ORM
├─────────────────────────────────────┤
│       Database Layer                 │  PostgreSQL
└─────────────────────────────────────┘
```

## 🏗 Компоненти

### 1. **Routes Layer** (`app/routes/`)
- Обробка HTTP запитів
- Валідація вхідних даних (Pydantic schemas)
- Повернення результатів
- HTTP статус коди

### 2. **CRUD Layer** (`app/crud/`)
- Логіка створення, читання, оновлення, видалення
- Взаємодія з БД через SQLAlchemy
- Бізнес-правила (перевірка наявності)

### 3. **Models Layer** (`app/models/`)
- SQLAlchemy ORM моделі
- Визначення таблиць та зв'язків
- Індекси та обмеження

### 4. **Schemas Layer** (`app/schemas/`)
- Pydantic моделі для валідації
- Serialization/Deserialization
- Документація у Swagger

### 5. **Database Layer** (`app/database.py`)
- SQLAlchemy engine та session
- Управління підключеннями

## 🔗 Взаємозв'язки

```
Tenant (1) ──→ (Many) Order
  - id (PK)         - id (PK)
  - name            - tenant_id (FK)
  - email           - order_number
  - company_name    - amount
  - is_active       - status
```

## 🔄 Flow запиту

```
HTTP Request
    ↓
Routes (GET /tenants/{id})
    ↓
Path параметри + Query параметри
    ↓
CRUD (get_tenant)
    ↓
SQLAlchemy Query
    ↓
PostgreSQL
    ↓
Результат
    ↓
Pydantic schema (serialization)
    ↓
HTTP Response (JSON)
```

## 🎯 Обґрунтування архітектури

### Переваги обраного підходу:

1. **Розділення відповідальності**
   - Кожній компоненту своя роль
   - Легко тестірати окремі шари

2. **Масштабованість**
   - Просто добавити нові сутності
   - Легко розширити функціонал

3. **Простота розуміння**
   - Новим розробникам легше орієнтуватися
   - Чітка структура файлів

4. **Переиспользование коду**
   - CRUD функції можуть використовуватися в різних маршрутах
   - Бізнес-логіка відокремлена від HTTP

5. **Тестованість**
   - Легко мокувати БД
   - Може тестірати окремі шари

## 🚀 Розширення

### Для додання нової сутності:

1. Створити модель у `models/entity.py`
2. Створити схему у `schemas/entity.py`
3. Створити CRUD у `crud/entity.py`
4. Створити маршути у `routes/entity.py`
5. Додати маршути до `main.py`

## 🔐 Безпека (майбутня розробка)

- Аутентифікація (JWT)
- Авторизація (RBAC)
- Rate limiting
- Input validation
- CORS