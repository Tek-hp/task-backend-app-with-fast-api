from fastapi import FastAPI
from models.user import UserWithoutId, UserWithID
import database

app = FastAPI()


@app.post('/create-user')
def create_user(user: UserWithoutId):
    result = database.create_user(user=user)
    return result

@app.get('/user/{user_id}')
def  get_user_by_id(user_id:str):
    result = database.get_user(user_id=user_id)
    return result

@app.get('/users')
def get_all_users():
    result = database.get_users()
    return result

@app.patch('/update_user/{user_id}')
def update_a_user(user_id:str,user_data:UserWithoutId):
    user :UserWithID = UserWithID(**user_data, _id = user_id)
    result = database.updateUser(user)
    return result

@app.get('/delete-user/{user_id}')
def delete_a_user(user_id:str):
    result = database.deleteUser(user_id=user_id)
    return result

