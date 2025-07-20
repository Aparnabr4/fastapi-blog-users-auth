# fastapi-blog-users-auth
A FastAPI-based RESTful API for a blogging platform with user registration, login via OAuth2, and secure blog CRUD operations. Built using SQLAlchemy, Pydantic, and JWT authentication

# FastAPI Blog App with User Authentication 📝🔐

This is a backend blog application built using **FastAPI**. It includes features for **user registration, login with JWT tokens**, and CRUD operations on blog posts.

## 🚀 Features

- ✅ User registration & login
- 🔐 JWT Authentication
- 📝 Create, Read, Update, Delete blogs
- 🗄️ SQLite Database with SQLAlchemy
- 📜 Pydantic for schema validation
- 🌐 FastAPI with automatic Swagger UI docs
- 🐳 Dockerized setup (if applicable)
- 🔄 Async endpoints (optional)

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Passlib (for password hashing)
- Python-Jose (for JWT tokens)

🗃️ Database Setup
-This project uses SQLite as the database.
-The database file (.blog.db) is automatically created when you run the project.
-You do not need to manually create or insert any tables.
-SQLAlchemy takes care of creating tables based on the models defined in models.py.

✅ How it works
When the app starts, the following line (in main.py or equivalent) creates all tables:
models.Base.metadata.create_all(bind=engine)


👩‍💻 Author
Aparna B R
GitHub

