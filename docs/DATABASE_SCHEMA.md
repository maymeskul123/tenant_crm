# Схема бази даних

## 📊 ER Diagram

```
┌─────────────────────────────────┐
│         TENANTS                 │
├─────────────────────────────────┤
│ id (PK)                         │
│ name (VARCHAR, UNIQUE)          │
│ email (VARCHAR, UNIQUE)         │
│ company_name (VARCHAR)          │
│ is_active (BOOLEAN)             │
│ created_at (TIMESTAMP)          │
│ updated_at (TIMESTAMP)          │
└──────────────┬──────────────────┘
               │ (1:N)
               │
┌──────────────▼──────────────────┐
│         ORDERS                  │
├─────────────────────────────────┤
│ id (PK)                         │
│ tenant_id (FK) ─────────────────┤
│ order_number (VARCHAR, UNIQUE)  │
│ description (TEXT)              │
│ amount (FLOAT)                  │
│ status (VARCHAR)                │
│ created_at (TIMESTAMP)          │
│ updated_at (TIMESTAMP)          │
└─────────────────────────────────┘
```

## 🗄 Таблиця TENANTS

```sql
CREATE TABLE tenants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    company_name VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tenants_email ON tenants(email);
CREATE INDEX idx_tenants_name ON tenants(name);
```

### Поля

| Поле | Тип | Обмеження | Опис |
|------|-----|----------|------|
| id | SERIAL | PRIMARY KEY | Унікальний ідентифікатор |
| name | VARCHAR(255) | NOT NULL, UNIQUE | Ім'я tenant |
| email | VARCHAR(255) | NOT NULL, UNIQUE | Email tenant |
| company_name | VARCHAR(255) | NOT NULL | Назва компанії |
| is_active | BOOLEAN | DEFAULT TRUE | Статус активності |
| created_at | TIMESTAMP | DEFAULT NOW() | Дата створення |
| updated_at | TIMESTAMP | DEFAULT NOW() | Дата оновлення |

## 🗄 Таблиця ORDERS

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
    order_number VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    amount FLOAT NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_orders_tenant_id ON orders(tenant_id);
CREATE INDEX idx_orders_order_number ON orders(order_number);
CREATE INDEX idx_orders_status ON orders(status);
```

### Поля

| Поле | Тип | Обмеження | Опис |
|------|-----|----------|------|
| id | SERIAL | PRIMARY KEY | Унікальний ідентифікатор |
| tenant_id | INTEGER | NOT NULL, FK | Посилання на tenant |
| order_number | VARCHAR(50) | NOT NULL, UNIQUE | Номер замовлення |
| description | TEXT | - | Опис замовлення |
| amount | FLOAT | NOT NULL | Сума замовлення |
| status | VARCHAR(50) | DEFAULT 'pending' | Статус замовлення |
| created_at | TIMESTAMP | DEFAULT NOW() | Дата створення |
| updated_at | TIMESTAMP | DEFAULT NOW() | Дата оновлення |

### Статуси замовлень

- `pending` - Очікує обробки
- `in_progress` - У розробці
- `completed` - Завершено
- `cancelled` - Скасовано

## 🔑 索引

### TENANTS
- `idx_tenants_email` - Пошук по email
- `idx_tenants_name` - Пошук по імені

### ORDERS
- `idx_orders_tenant_id` - Пошук замовлень tenant
- `idx_orders_order_number` - Пошук по номеру
- `idx_orders_status` - Фільтрація по статусу

## 🔗 Зв'язки

### Foreign Key
```
orders.tenant_id → tenants.id
ON DELETE CASCADE
```

**Каскадне видалення:** При видаленні tenant видаляються всі його замовлення.

## 📈 Приклади запитів

### Отримати всі замовлення tenant

```sql
SELECT * FROM orders 
WHERE tenant_id = 1 
ORDER BY created_at DESC;
```

### Отримати статистику по tenant

```sql
SELECT 
    t.id,
    t.name,
    COUNT(o.id) as total_orders,
    SUM(o.amount) as total_amount,
    AVG(o.amount) as avg_amount
FROM tenants t
LEFT JOIN orders o ON t.id = o.tenant_id
GROUP BY t.id, t.name;
```

### Отримати замовлення за період

```sql
SELECT * FROM orders 
WHERE tenant_id = 1 
AND created_at BETWEEN '2026-01-01' AND '2026-12-31'
ORDER BY created_at DESC;
```

### Отримати активні tenant без замовлень

```sql
SELECT t.* FROM tenants t
LEFT JOIN orders o ON t.id = o.tenant_id
WHERE t.is_active = TRUE
AND o.id IS NULL;
```