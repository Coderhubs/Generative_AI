# **Task Tracker API (FastAPI)**

_A simple RESTful API built with **FastAPI** to manage users and their tasks. Ideal for beginners to understand how APIs, models, and validations work._

---

## **🚀 Features**

- **🧑 Create and view users**
- **📝 Create, view, and update tasks**
- **🔄 Update task status**
- **📋 View all tasks for a specific user**
- **🛡️ Input validation using Pydantic**

---

## **📦 Project Overview – Task 06**

This API project demonstrates how to implement:

- **_Pydantic models with validation_**
- **_Input constraints_**
- **_Custom validators (like checking due date)_**
- **_API routing and request handling using FastAPI_**

---

## **🧱 API Endpoints and Logic**

### 👤 **Users**

- **POST /users/** – _Create a user. Returns the user data (id, username, email)._
- **GET /users/{user_id}** – _Fetch a specific user by ID._

### ✅ **Tasks**

- **POST /tasks/** – _Create a new task. Validates that the due date is today or in the future._
- **GET /tasks/{task_id}** – _Retrieve a task by its ID._
- **PUT /tasks/{task_id}** – _Update the status of a task (must be one of: "pending", "in_progress", "done")._
- **GET /users/{user_id}/tasks** – _List all tasks that belong to a specific user._

---

## **📘 Validation Rules**

- **Username** must be between _3–20 characters_
- **Email** must be valid using `EmailStr`
- **Due date** must be _today or a future date_ (checked using `@validator`)

---

## **▶️ How to Use in Browser**

Once the server is running, you can use the API via:

- **Swagger UI:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
- **ReDoc UI:** [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)

---

