# AI Prompt Library

A full-stack web application to manage AI image generation prompts with real-time view tracking using Redis.

---

## 🚀 Features

* Create AI prompts
* View all prompts
* View prompt details
* Redis-based live view counter
* Clean REST API (Django without DRF)

---

## 🛠 Tech Stack

**Frontend**

* Angular (Standalone Components)

**Backend**

* Django

**Database**

* SQLite (Development)

**Cache**

* Redis (used as source of truth for view count)

---

## 📦 Architecture

* Angular frontend consumes Django APIs
* Django handles CRUD operations
* Redis tracks and increments prompt views
* View count is NOT stored in DB (Redis only)

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
* Function-based views for simplicity
* Redis used as the single source of truth for view count
* Angular standalone components for minimal setup
* Focused on working system over over-engineering

---

## ⚠️ Limitations

* No authentication (bonus feature not implemented)
* SQLite used instead of PostgreSQL
* Basic UI (no heavy styling)

---

## 📹 Demo

(Add your screen recording link here)

---

## 📌 Future Improvements

* JWT Authentication
* Tag-based filtering
* Pagination
* Deployment (Render / Railway)

---

## ✅ Status

Fully functional full-stack application with Redis integration.
