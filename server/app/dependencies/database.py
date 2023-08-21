from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorClient
from db.postgres.database import engine
from db.mongodb.database import mongodb_db

def get_postgres_db():
    client = Session(bind=engine)
    try:
        yield client
    finally:
        client.close()

def get_mongodb_db():
    client = mongodb_db
    try:
        yield client.db
    finally:
        client.close()
