from pydantic import BaseModel
from models.user import User
from enum import Enum


class TaskStatus(Enum):
    Pending = "pending"
    Ongoing = "ongoing"
    Testing = "testing"
    Completed = "completed"


class Task(BaseModel):
    title: str
    task_id: int
    description: str
    task_status: TaskStatus | None = None
    deadline: str | None = None
    submitted_on: str | None = None
    assigned_by: str = "Team Lead"
    assigned_to: str = "Developer"
