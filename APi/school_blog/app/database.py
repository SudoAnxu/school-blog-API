from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"  # Update with your MongoDB connection string

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.school_blog
