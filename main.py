# app.py
from fastapi import FastAPI
from kanban_board import KanbanBoard, Task
from typing import List

app = FastAPI()

# Instantiate KanbanBoard (connect to the SQLite database)
kanban_board = KanbanBoard()

# Routes

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return kanban_board.get_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: int):
    return kanban_board.get_task_by_id(task_id)

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    return kanban_board.create_task(task)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    return kanban_board.update_task(task_id, updated_task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return kanban_board.delete_task(task_id)

# Example route for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Kanban Board API!"}
