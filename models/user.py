from pydantic import BaseModel, EmailStr
from models.task import Task


class UserWithID(BaseModel):
    id: str
    name: str
    email: EmailStr
    user_name: str
    dob: str | None = None

class UserWithoutId(BaseModel):
    name: str
    email: EmailStr
    user_name: str
    dob: str | None = None
