# Prueba Técnica: CRUD con FastAPI, SQLAlchemy y JWT

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

Una API RESTful completa desarrollada con **FastAPI**, **Pydantic v2**, **SQLAlchemy 2.0 (async)**, **Alembic**, **JWT**, **soft-delete**, **mixins**, **routers**, **middleware personalizado** y **Docker**.

---

## Objetivo

Desarrollar un **CRUD completo** con relaciones complejas, autenticación segura, migraciones, soft-delete y buenas prácticas de arquitectura.

---

## Requisitos Cumplidos

| Requisito | Estado |
|---------|--------|
| Modelos con relaciones 1:N y N:N | Done |
| Migraciones con Alembic (incluye evolución de modelo) | Done |
| Operaciones asíncronas con SQLAlchemy | Done |
| Soft-delete con mixin y filtro personalizado | Done |
| Timestamps automáticos (`created_at`, `updated_at`) | Done |
| Autenticación JWT (registro, login, protección) | Done |
| Routers por entidad (`users.py`, `posts.py`, etc.) | Done |
| Middleware de tiempo de respuesta | Done |
| Paginación en listados | Done |
| Validaciones Pydantic v2 (email, longitud, etc.) | Done |
| Docker + Docker Compose | Done |
| Solo el autor puede editar/eliminar su post | Done |

---

## Tecnologías

- **FastAPI** (API + OpenAPI)
- **Pydantic v2** (validación)
- **SQLAlchemy 2.0 (async)** + **PostgreSQL**
- **Alembic** (migraciones)
- **PyJWT** + **passlib** (autenticación)
- **Docker** & **Docker Compose**
- **Python 3.11**

---

## Estructura del Proyecto

.
├── Prueba-Tecnica-Fastapi/
│   ├── application/   # Se definen los servicios que consumen directamente de los repositorios
│   ├── domain/         # Pydantic schemas, mixins y definicion de los schema filters (todos los filtros posibles) usando Pydantic
│   ├── infrastructure/ # En orm la definicion de las tablas , en filters los filtros y en repositories los repositorios
│   ├── utils/          # Helpers (JWT, password) , permisos
    ├── presentation    # Routers y serializadores (mappers)
    └── main.py         # App FastAPI
    ├── alembic/         # Alembic
    ├── docker-compose.yml
    ├── Dockerfile
    ├── alembic.ini
    ├── config.py      # Env vars
    ├── database.py    # Métodos de inicio de la DB
    ├── requirements.txt
    └── README.md

## Inicio Rápido (Docker)

docker compose up --build
