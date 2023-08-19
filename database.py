from pymongo import MongoClient

import settings
import os
from dotenv import load_dotenv
from models.user import UserWithoutId, UserWithID
from enum import Enum
from utils.show_message import showMessage
from bson import ObjectId

class CollectionType(Enum):
    User= 'users'
    Task= 'tasks'


load_dotenv()


__mongo_client__ = MongoClient(settings.mongodb_uri)

__database__ = __mongo_client__.get_database(os.getenv("CLUSTERNAME"))

def __get_my_collection__(collection_type:CollectionType):
    if collection_type.value in __database__.list_collection_names():
        return __database__.get_collection(collection_type.value)
    else:
        showMessage(f"Missing {collection_type.value}. Creating a new Collection : {collection_type.value}")
        collection = __database__.create_collection(collection_type.value)
        return collection

def create_user(user:UserWithoutId):
    user_check_filter = {"email": user.email}

    collection = __get_my_collection__(CollectionType.User)

    try:
        
        if collection.find_one(user_check_filter) is None:
            result = collection.insert_one(user.model_dump())
            showMessage(result.inserted_id)

            user_data : UserWithID = UserWithID(id = str(result.inserted_id), **user.model_dump()) # assings respective value of fields
            return base_response(message="Created User Successfully", data= user_data)
        
        return base_response(message=f"User Already exists for the email {user.email}. Please try again with another email")
    except Exception as e:
        showMessage(message=e, success=False)
        return base_response(message=f"{e}", success=False)


def get_users():
    collection = __get_my_collection__(CollectionType.User)
    try: 
        result = collection.find()
        if result is not None:
            users = []

            for value in result:
                new_user = UserWithID(**value, id=str(value['_id']))
                users.append(new_user)
            
            if len(users) == 0:
                return base_response(message="No users found. Create users to fetch the List")

            return base_response(message="Fetched all users", data= users)


        return base_response(message="Failed to fetch all users", success=False)
    except Exception as e:
        return base_response(message=f"{e}", success=False)
    
def get_user(user_id:str):
    user_check_filter = {"_id":ObjectId(user_id)}

    showMessage(f'User ID :: {user_id}')

    collection = __get_my_collection__(CollectionType.User)
    try:
        result  = collection.find_one(user_check_filter)

        showMessage(f'Result :: {result}')

        if result is not None:
            user_data_from_database =  UserWithID(**result, id=str(result['_id']))
            return base_response(message=f"Fetched user data successfully", data= user_data_from_database)
        
        return base_response(message=f"Could not find user with id {user_id}", success=False)
    except Exception as e:
        return base_response(message=f"{e}", success= False)
    
def updateUser(user:UserWithID):
    user_check_filter = {"_id":ObjectId(user.id)}
    collection = __get_my_collection__(CollectionType.User)

    try:
        result = collection.find_one_and_update(filter=user_check_filter,update= user.model_dump())

        if result is not None:
            return base_response(message="Updated User", data= result)
        
        return base_response(message="Could not update user", success= False)
    except Exception as e:
        return base_response(message=f"{e}")
    
def deleteUser(user_id:str):
    user_check_filter = {"_id":ObjectId(user_id)}

    collection = __get_my_collection__(CollectionType.User)

    try:
        result = collection.find_one_and_delete(user_check_filter)

        if result is not None:
            print(result)
            return base_response(message='Deleted successfully')
        
        return base_response(message="Could not find user with the given id.")
    except Exception as e:
        return base_response(message=f'{e}')

def base_response(
    message: str,
    success: bool = True,
    data: any = None,
) -> dict[str, any]:
    response = {
        "success": success,
        "message": message,
    }

    if data is not None:
        response["data"] = data

    return response
