from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional, Annotated
from models import Task as TaskModel
from database import get_db
from repository import TaskRepository
from schemas import TaskCreate, Task


router = APIRouter(
    tags=["задачи"],
)


@router.get("/")
def read_root():
    return {"message": "Добро пожаловать!"}

@router.get("/tasks/", response_model=List[Task])
def get_tasks(db: Annotated[Session, Depends(get_db)]):
    repo = TaskRepository(db)
    return repo.get_tasks()

@router.post("/tasks/", response_model=Task)
def create_task(task_data: TaskCreate, db: Annotated[Session, Depends(get_db)]):
    repo = TaskRepository(db)
    return repo.create_task(task_data)

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    repo = TaskRepository(db)
    task = repo.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена!")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task_data: TaskCreate, db: Annotated[Session, Depends(get_db)]):
    repo = TaskRepository(db)
    task = repo.update_task(task_id, updated_task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена!")
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    repo = TaskRepository(db)
    try:
        if not repo.delete_task(task_id):
            raise HTTPException(status_code=404, detail="Задача не найдена")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"message": "Задача успешно удалена"}

@router.get("/tasks/{task_id}/parent", response_model=Optional[Task])
def get_parent_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    repo = TaskRepository(db)
    parent_task = repo.get_parent_task(task_id)
    
    if parent_task is None:
        raise HTTPException(status_code=404, detail="Родительская задача не найдена")
    
    return parent_task
