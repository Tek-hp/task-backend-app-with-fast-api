from pydantic import BaseModel
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
    assigned_to: str
    assigned_by: str
    task_status: TaskStatus | None = None
    deadline: str | None = None
    submitted_on: str | None = None

    model_config = {
        "json_schema_extra":{
            "examples": [
                {
                "title": "Dummy Title",
                "task_id": 123,
                "description": "This is a dummy description just for test.This is a dummy description just for test.This is a dummy description just for test.This is a dummy description just for test.This is a dummy description just for test.",
                "assigned_to": "Someone",
                "assigned_by": "Tek",
                "task_status": "pending",
                "deadline": "2023-12-10",
                "submitted_on":"2023-10-12",
            }
            ]
        }
    }
