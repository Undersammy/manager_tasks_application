from pydantic import BaseModel
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False
    parent_id: Optional[int] = None


class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True
