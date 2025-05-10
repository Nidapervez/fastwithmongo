from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Get MongoDB URI from environment variable
MONGO_URL = os.getenv("MONGO_URL")

# ✅ Fail early if env var is missing
if not MONGO_URL:
    raise ValueError("⚠️ MONGO_URL environment variable not set!")

# ✅ Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URL)
db = client["fastapi_db"]  # Use your desired DB name
user_collection = db["users"]  # Your collection

print("✅ MongoDB connected successfully")


