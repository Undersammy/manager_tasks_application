from sqlalchemy.orm import Session
from typing import List, Optional
from .models import Task as TaskModel
from .schemas import TaskCreate

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_task(self, task_id: int) -> Optional[TaskModel]:
        return self.db.query(TaskModel).filter(TaskModel.id == task_id).first()

    def get_tasks(self) -> List[TaskModel]:
        return self.db.query(TaskModel).all()

    def create_task(self, task_data: TaskCreate) -> TaskModel:
        task = TaskModel(**task_data.dict())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: int, updated_task: TaskCreate) -> Optional[TaskModel]:
        task = self.get_task(task_id)
        if task:
            for key, value in updated_task.dict().items():
                setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            subtasks = self.db.query(TaskModel).filter(TaskModel.parent_id == task_id).all()
            if subtasks:
                raise ValueError("Сначала удалите подзадачи")
            self.db.delete(task)
            self.db.commit()
            return True
        return False

    def get_parent_task(self, task_id: int) -> Optional[TaskModel]:
        task = self.get_task(task_id)
        if task and task.parent_id is not None:
            return self.get_task(task.parent_id)
        return None
