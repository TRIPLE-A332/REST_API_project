# REST API Project 

A comparative backend development project demonstrating **CRUD operations** using three different frameworks:
- **Flask (Python)**
- **FastAPI (Python)**
- **Spring Boot (Java)**

This repository was created to benchmark, understand, and demonstrate the implementation of RESTful APIs using different languages and frameworks. Each implementation interacts with a simple user database and performs standard operations: Create, Read, Update, Delete (CRUD).

---

##  Project Structure

│

├── flask_app/ # Python Flask app with SQLite and SQLAlchemy

│

├── fastapi_app/ # Python FastAPI app with SQLite and SQLAlchemy

│

├── springboot_app/ # Java Spring Boot app with JPA and H2 DB


---

##  Key Features

| Feature               | Flask             | FastAPI           | Spring Boot      |
|----------------------|------------------|-------------------|------------------|
| Language             | Python            | Python            | Java             |
| DB Used              | SQLite            | SQLite            | MySQL            |
| ORM/Database Layer   | SQLAlchemy        | SQLAlchemy        | Spring Data JPA  |
| Performance          | Lightweight       | Fast, modern      | Production-grade |

---

##  CRUD Functionality Implemented

All three apps support:

-  Create new user (POST `/users`)
-  Get all users (GET `/users`)
-  Get user by ID (GET `/users/{id}`)
-  Update user (PUT `/users/{id}`)
-  Delete user (DELETE `/users/{id}`)

---

## Purpose
This project serves as:

A technical comparison of REST API implementations

Practice ground for backend development in both Python and Java

A boilerplate reference for small-to-medium scale web services
