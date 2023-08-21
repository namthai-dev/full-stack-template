from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import settings

MONGODB_URL = settings.MONGODB_URL

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(MONGODB_URL)
        self.db = self.client.your_database  # Replace with your actual database name

    async def close(self):
        if self.client:
            self.client.close()

mongodb_db = MongoDB()
