from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient()
db = client.your_database

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
