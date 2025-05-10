# main.py
from fastapi import FastAPI
from models import User
from database import user_collection
from bson import ObjectId

app = FastAPI()

# Create user
@app.post("/users/")
async def create_user(user: User):
    try:
        user_dict = user.dict()
        result = await user_collection.insert_one(user_dict)
        return {"message": "User created", "id": str(result.inserted_id)}
    except Exception as e:
        return {"error": str(e)}


# Get all users
@app.get("/users/")
async def get_users():
    users = []
    async for user in user_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users
