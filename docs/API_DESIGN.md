# API Design

## 📋 API Conventions

### Базовий URL
```
http://localhost:8000/api/v1
```

### HTTP методи
- `GET` - Отримати ресурс
- `POST` - Створити ресурс (201)
- `PUT` - Оновити весь ресурс
- `PATCH` - Оновити частину ресурсу
- `DELETE` - Видалити ресурс (204)

### Status коди
- `200` - OK
- `201` - Created
- `204` - No Content
- `400` - Bad Request
- `404` - Not Found
- `500` - Server Error

## 👥 Tenants API

### List Tenants
```
GET /tenants?skip=0&limit=100
```

**Response (200):**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "company_name": "Acme Corp",
    "is_active": true,
    "created_at": "2026-05-07T10:00:00",
    "updated_at": "2026-05-07T10:00:00"
  }
]
```

### Get Tenant
```
GET /tenants/{id}
```

**Response (200):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "company_name": "Acme Corp",
  "is_active": true,
  "created_at": "2026-05-07T10:00:00",
  "updated_at": "2026-05-07T10:00:00",
  "orders": [
    {
      "id": 1,
      "tenant_id": 1,
      "order_number": "ORD-001",
      "description": "Web development",
      "amount": 5000.0,
      "status": "pending",
      "created_at": "2026-05-07T10:00:00",
      "updated_at": "2026-05-07T10:00:00"
    }
  ]
}
```

### Create Tenant
```
POST /tenants
Content-Type: application/json

{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "company_name": "Tech Solutions",
  "is_active": true
}
```

**Response (201):**
```json
{
  "id": 2,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "company_name": "Tech Solutions",
  "is_active": true,
  "created_at": "2026-05-07T10:00:00",
  "updated_at": "2026-05-07T10:00:00"
}
```

### Update Tenant
```
PUT /tenants/{id}
Content-Type: application/json

{
  "company_name": "New Company Name"
}
```

**Response (200):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "company_name": "New Company Name",
  "is_active": true,
  "created_at": "2026-05-07T10:00:00",
  "updated_at": "2026-05-07T10:15:00"
}
```

### Delete Tenant
```
DELETE /tenants/{id}
```

**Response (204):** No Content

## 📦 Orders API

### List Orders
```
GET /orders?skip=0&limit=100
```

### Get Order by Tenant
```
GET /orders/tenant/{tenant_id}?skip=0&limit=100
```

### Get Order
```
GET /orders/{id}
```

### Create Order
```
POST /orders
Content-Type: application/json

{
  "tenant_id": 1,
  "order_number": "ORD-002",
  "description": "Mobile app development",
  "amount": 8000.0,
  "status": "pending"
}
```

**Response (201):**
```json
{
  "id": 2,
  "tenant_id": 1,
  "order_number": "ORD-002",
  "description": "Mobile app development",
  "amount": 8000.0,
  "status": "pending",
  "created_at": "2026-05-07T10:00:00",
  "updated_at": "2026-05-07T10:00:00"
}
```

### Update Order
```
PUT /orders/{id}
Content-Type: application/json

{
  "status": "completed"
}
```

### Delete Order
```
DELETE /orders/{id}
```

**Response (204):** No Content

## ❌ Error Responses

```json
{
  "detail": "Tenant not found"
}
```

```json
{
  "detail": "Email already registered"
}
```