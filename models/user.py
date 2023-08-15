from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id:int
    name: str
    email: EmailStr
    user_name: str
    dob: str | None = None
    tasks_completed: list | None = None

    class Config:
        scheme_extra = {
            "example":{
                "id": 12,
                "name" : "Tek Raj Ojha",
                "email" : "tekrajojha6@gmail.com",
                "user_name" : "tek0_0",
                "dob": "1997-04-19",
                "tasks_completed": []
            }
        }
