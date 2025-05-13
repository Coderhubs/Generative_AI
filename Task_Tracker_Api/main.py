from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date
from typing import List



app = FastAPI()

# Temporary in-memory "databases"
users_db = {}
tasks_db = {}

# Auto-increment counters for IDs
next_user_id = 1
next_task_id = 1

# -------------------------------
# User Models
# -------------------------------

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr

class UserRead(BaseModel):
    id: int
    
    username: str
    email: EmailStr

# -------------------------------
# Task Models
# -------------------------------

class TaskCreate(BaseModel):
    user_id: int
    title: str
    description: str
    status: str
    due_date: date

    # This validator is INSIDE the model class
    @validator("due_date")
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date must be today or in the future")
        return v

class Task(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    status: str
    due_date: date  # ← You had this line incomplete

class TaskStatusUpdate(BaseModel):
    status: str

# -------------------------------
# User Endpoints
# -------------------------------

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global next_user_id

    new_user = {
        "id": next_user_id,
        "username": user.username,
        "email": user.email
    }

    users_db[next_user_id] = new_user
    next_user_id += 1
    return new_user

@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# -------------------------------
# Task Endpoints
# -------------------------------

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global next_task_id

    if task.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    new_task = task.dict()
    new_task["id"] = next_task_id
    tasks_db[next_task_id] = new_task
    next_task_id += 1
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status_update: TaskStatusUpdate):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if status_update.status not in ["pending", "in_progress", "done"]:
        raise HTTPException(status_code=400, detail="Invalid status")

    task["status"] = status_update.status
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_tasks_for_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    user_tasks = [task for task in tasks_db.values() if task["user_id"] == user_id]
    return user_tasks
