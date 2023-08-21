import os

class Settings:
    PROJECT_NAME = "Your FastAPI Project"
    DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")
    MONGODB_URL = os.environ.get("MONGODB_URL")

    
settings = Settings()
