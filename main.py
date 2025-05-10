from fastapi import FastAPI
from models import User
from database import user_collection  # Make sure this is from motor
from bson import ObjectId

app = FastAPI()

# ✅ Root route to confirm deployment
@app.get("/")
def root():
    return {"message": "🚀 FastAPI app deployed and running!"}

# ✅ Create user
@app.post("/users/")
async def create_user(user: User):
    try:
        user_dict = user.dict()
        result = await user_collection.insert_one(user_dict)
        return {"message": "User created", "id": str(result.inserted_id)}
    except Exception as e:
        return {"error": str(e)}

# ✅ Get all users
@app.get("/users/")
async def get_users():
    users = []
    async for user in user_collection.find():
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        users.append(user)
    return users
