from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    user_name: str
    dob: str | None = None
    tasks_completed: list | None = None
