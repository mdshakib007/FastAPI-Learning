# FastAPI Learning Journey

Welcome to my **FastAPI Learning Repository**!  
This repository documents my hands-on journey with **FastAPI**, one of the fastest and most modern frameworks for building APIs with Python.

> **Goal:** Learn by building real-world examples, mastering core concepts, and preparing for production-grade backend development.

---

## What You'll Find Here

- **Basic FastAPI Setup** — Installation, project structure, and "few" examples  
- **Request Handling** — Query parameters, request bodies, validation with Pydantic  
- **Authentication & Authorization** — OAuth2, JWT Tokens  
- **Database Integration** — SQLite, SQLAlchemy, async database access  
- **Asynchronous Programming** — Writing truly async FastAPI apps  
- **Testing** — Pytest with FastAPI  
- **Project Organization** — Building scalable and maintainable APIs  
- **Deployment Basics** — Uvicorn, Docker, simple cloud deployments (coming soon...)

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Type Defination:** Pydantic
- **Database:** SQLite (initially), PostgreSQL (later)
- **ORM:** SQLAlchemy & RAW SQL Code
- **Authentication:** OAuth2, JWT
- **Testing:** Pytest
- **Containerization:** Docker (Planned)

---

## 📂 Project Structure (Evolving)

```bash
fastapi-learning/
│
├── app/
│   ├── main.py         # Entry point
│   ├── models.py       # Database models
│   ├── schemas.py      # Pydantic models
│   ├── crud.py         # Database operations
│   ├── routes/         # API routes
│   └── core/           # Configuration, utilities
│
├── tests/              # Test cases
├── requirements.txt    # Python dependencies
├── Dockerfile          # (Coming soon)
└── README.md           # info file
```

---

## 🙤 Learning Roadmap

I am progressing through the following stages:

1. **Foundation:**  
   - FastAPI Basics  
   - Request and Response handling

2. **Core Features:**  
   - Path Operations, Dependency Injection, Security

3. **Database & Async:**  
   - Building CRUD APIs with async support

4. **Advanced Topics:**  
   - Background tasks, WebSocket, Middleware

5. **Deployment & Best Practices:**  
   - Dockerizing FastAPI, CI/CD basics

---

## Why FastAPI?

- **Blazingly fast** (thanks to Starlette and Pydantic)  
- **Async-ready** for modern applications  
- **Automatic Interactive API Docs** (Swagger & Redoc)  
- **Pythonic and type-hinted**  

I believe mastering FastAPI will strengthen both my **backend** and **full-stack** engineering skills significantly.

---

# 🚀 Let's build APIs — the FastAPI way! test