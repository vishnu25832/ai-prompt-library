# AI Prompt Library

A full-stack web application to manage AI image generation prompts with real-time view tracking using Redis.

---

## 🚀 Features

* Create AI prompts
* View all prompts
* View detailed prompt information
* Redis-based live view counter
* Clean REST API using Django (no DRF)

---

## 🛠 Tech Stack

**Frontend**

* Angular (Standalone Components)

**Backend**

* Django

**Database**

* SQLite (Development)

**Cache**

* Redis (source of truth for view count)

---

## 📦 Architecture

* Angular frontend consumes Django APIs
* Django handles CRUD operations
* Redis increments and stores view counts
* View count is NOT stored in database

---

## ⚙️ Setup Instructions

### 1. Clone repository

```bash
git clone <your-repo-url>
cd ai-prompt-library
```

---

### 2. Backend setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install django psycopg2-binary redis django-cors-headers
python manage.py migrate
python manage.py runserver
```

---

### 3. Frontend setup

```bash
cd frontend
npm install
ng serve
```

---

### 4. Run Redis

```bash
redis-server.exe
```

---

## 🌐 API Endpoints

### Get all prompts

```
GET /prompts/
```

### Create prompt

```
POST /prompts/
```

### Get prompt detail

```
GET /prompts/<id>/
```

---

## 🔥 Key Design Decisions

* Used Django without DRF to match assignment constraints
* Function-based views for simplicity and control
* Redis used as the single source of truth for view count
* Angular standalone components for minimal setup
* Focused on working system over over-engineering

---

## ⚠️ Limitations

* No authentication (bonus feature not implemented)
* SQLite used instead of PostgreSQL
* Basic UI styling

---

## 🐳 Docker Setup

This project includes a basic Docker configuration to run the full stack (Frontend, Backend, and Redis) using Docker Compose.

---

### Prerequisites

* Docker installed
* Docker Compose installed

---

### Run the application

From the project root:

```bash
docker-compose up --build
```

---

### Services

| Service  | URL / Port            | Description        |
| -------- | --------------------- | ------------------ |
| Frontend | http://localhost:4200 | Angular app        |
| Backend  | http://localhost:8000 | Django API         |
| Redis    | localhost:6379        | View counter store |

---

### Notes

* Backend runs Django development server inside container
* Redis is used as the source of truth for view counts
* SQLite is used for simplicity
* Volumes are mounted for live code changes

---

### Limitations (Docker)

* Not optimized for production
* No environment variable management
* Angular runs in dev mode

---

### Stop containers

```bash
docker-compose down
```

---

## 📌 Future Improvements

* JWT Authentication
* Tag-based filtering
* Pagination
* Deployment (Render / Railway)

---

## ✅ Status

Fully functional full-stack application with Redis integration.
