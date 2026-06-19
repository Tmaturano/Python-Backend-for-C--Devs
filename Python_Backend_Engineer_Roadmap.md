# Python Backend Engineer Roadmap (for a .NET/C# Developer)

## Goal

Build production-grade APIs with:

- Python 3.13+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Redis
- RabbitMQ
- Docker
- Pytest
- Clean Architecture
- REST APIs
- Idempotency
- Observability

---

## Module 1 — Python Fundamentals

### Topics
- Variables and types
- Functions
- Classes
- Exceptions
- Modules and packages
- Type hints
- Python conventions

### Outcome
Read and write basic Python code comfortably.

---

## Module 2 — Pythonic Programming

### Topics
- List comprehensions
- Generators
- Decorators
- Context managers
- Type hints in depth

### Outcome
Write idiomatic Python instead of "C# written in Python".

---

## Module 3 — Data Structures

### Topics
- Lists
- Tuples
- Sets
- Dictionaries
- Dataclasses

### Mapping from C#
| C# | Python |
|------|------|
| List<T> | list |
| Dictionary<TKey,TValue> | dict |
| HashSet<T> | set |
| Record | dataclass |

---

## Module 4 — Async Programming

### Topics
- async / await
- Event loop
- Concurrency
- Async I/O

### Mapping from C#
- Task
- async/await
- Asynchronous APIs

---

## Module 5 — PostgreSQL

### Topics
- Dockerized PostgreSQL
- SQL fundamentals
- Connections with psycopg
- Transactions
- Parameterized queries

### Outcome
Understand database access before introducing an ORM.

---

## Module 6 — SQLAlchemy ORM

### Topics
- Entities
- Relationships
- Sessions
- Queries
- Unit of Work concepts

### Mapping from C#
- EF Core
- DbContext
- LINQ-like querying

---

## Module 7 — Database Migrations

### Tool
- Alembic

### Topics
- Creating migrations
- Applying migrations
- Schema evolution

---

## Module 8 — FastAPI

### Topics
- Routing
- Request/response models
- Dependency injection
- Validation
- Middleware

### Outcome
Build modern REST APIs similar to ASP.NET Core.

---

## Module 9 — Dependency Injection

### Topics
- Constructor injection
- Service lifetimes
- Dependency Injector

### Outcome
Create maintainable and testable services.

---

## Module 10 — Clean Architecture

### Suggested Structure

```text
src/
├── api/
├── application/
├── domain/
├── infrastructure/
└── tests/
```

### Topics
- Domain layer
- Application layer
- Infrastructure layer
- Dependency inversion

---

## Module 11 — Unit Testing

### Tool
- Pytest

### Topics
- Test organization
- Assertions
- Mocking
- Fixtures

### Outcome
Write reliable automated tests.

---

## Module 12 — Integration Testing

### Topics
- Testcontainers
- PostgreSQL integration tests
- Redis integration tests
- API integration tests

---

## Module 13 — Redis

### Topics
- Caching
- Distributed locks
- Rate limiting
- Idempotency keys

---

## Module 14 — RabbitMQ

### Topics
- Producers
- Consumers
- Dead-letter queues
- Retries
- Event-driven architecture
- Outbox pattern

---

## Module 15 — API Design

### Topics
- REST principles
- Resource design
- Pagination
- Filtering
- Validation
- Error handling

### Advanced Topics
- Idempotency
- Correlation IDs
- Versioning

---

## Module 16 — Observability

### Topics
- Structured logging
- OpenTelemetry
- Metrics
- Tracing
- Grafana
- Prometheus

---

## Module 17 — Docker

### Topics
- Dockerfiles
- Docker Compose
- Multi-container environments

### Services
- API
- PostgreSQL
- Redis
- RabbitMQ

---

## Final Capstone Project

### Football Statistics API

### Features
- Teams
- Players
- Matches
- Statistics
- Redis caching
- RabbitMQ integration
- PostgreSQL persistence
- REST endpoints
- Unit tests
- Integration tests
- Dockerized deployment

### Architecture

```text
FastAPI
├── REST API
├── PostgreSQL
├── SQLAlchemy
├── Redis
├── RabbitMQ
├── Docker
├── Alembic
├── Pytest
├── OpenTelemetry
└── Clean Architecture
```

---

## Estimated Timeline

- 8–12 weeks
- 5–7 hours per week
- Designed for an experienced .NET/C# backend engineer
