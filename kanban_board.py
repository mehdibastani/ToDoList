# kanban_board.py
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional, List
from fastapi import HTTPException

# Task Model for SQLModel
class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    status: str  # Example statuses: "to-do", "in-progress", "done"


# Kanban Board Class to handle database interactions
class KanbanBoard:
    def __init__(self, db_url: str = "sqlite:///./kanban.db"):
        # SQLite database URL
        self.engine = create_engine(db_url)
        # Create tables in the database
        SQLModel.metadata.create_all(self.engine)

    # Get all tasks
    def get_tasks(self) -> List[Task]:
        with Session(self.engine) as session:
            tasks = session.exec(select(Task)).all()
        return tasks

    # Get a specific task by ID
    def get_task_by_id(self, task_id: int) -> Task:
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
        return task

    # Add a new task
    def create_task(self, task: Task) -> Task:
        with Session(self.engine) as session:
            session.add(task)
            session.commit()
            session.refresh(task)
        return task

    # Edit an existing task
    def update_task(self, task_id: int, updated_task: Task) -> Task:
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            task.title = updated_task.title
            task.description = updated_task.description
            task.status = updated_task.status
            session.add(task)
            session.commit()
            session.refresh(task)
        return task

    # Delete a task by ID
    def delete_task(self, task_id: int) -> dict:
        with Session(self.engine) as session:
            task = session.get(Task, task_id)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            session.delete(task)
            session.commit()
        return {"detail": "Task deleted successfully"}
