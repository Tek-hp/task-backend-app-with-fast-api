from fastapi import FastAPI
from models.user import User
from models.task import Task, TaskStatus


app = FastAPI()

user_list: list[User] = []
task_list: list[Task] = []


@app.get("/")
def root():
    return {"content": "task-application"}


@app.post("/users")
async def users(data: User):
    try:
        if len(user_list) != 0:
            for an_user in user_list:
                if an_user.email == data.email:
                    raise Exception("Email has already been used")

                if an_user.user_name == data.user_name:
                    raise Exception("User name has already been used")

        new_user = User(
            name=data.name,
            user_name=data.user_name,
            email=data.email,
        )

        if data.dob is not None:
            new_user.dob = data.dob
        if data.tasks_completed is not None:
            new_user.tasks_completed = data.tasks_completed

        user_list.append(new_user)

        return base_response(
            success=True,
            message="User created successfully",
            data=new_user,
        )
    except Exception as e:
        return base_response(
            success=False,
            message=f"{e}",
        )


@app.get("/users")
async def users():
    return base_response(
        success=True,
        message="Successfully fetched user list",
        data=user_list,
    )


@app.get("/tasks")
def tasks():
    return base_response(
        success=True,
        message="Successfully got the task list",
        data=task_list,
    )


@app.post("/tasks")
async def tasks(data: Task):
    try:
        new_task = Task(
            task_id=len(task_list),
            title=data.title,
            description=data.description,
            assigned_by=data.assigned_by,
            assigned_to=data.assigned_to,
            task_status=data.task_status,
        )

        if data.deadline is not None:
            new_task.deadline = data.deadline
        if data.submitted_on is not None:
            new_task.submitted_on = data.submitted_on

        task_list.append(new_task)

        return base_response(
            success=True,
            message="Task created successfully",
            data=new_task,
        )
    except Exception as e:
        return base_response(
            success=False,
            message=f"{e}",
        )


def base_response(
    success: bool,
    message: str,
    data: any = None,
) -> dict[str, any]:
    response = {
        "success": success,
        "message": message,
    }

    if data is not None:
        response["data"] = data

    return response
