import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorClient

from app.main import app
from app.dependencies.database import get_postgres_db, get_mongodb_db
from config.database_config import SessionLocal, mongodb_db

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture(scope="module")
async def test_mongodb():
    yield mongodb_db

@pytest.fixture(scope="module")
def test_app():
    # Override app dependencies for testing
    app.dependency_overrides[get_postgres_db] = lambda: SessionLocal()
    app.dependency_overrides[get_mongodb_db] = lambda: mongodb_db
    yield app

# tests/test_main.py

def test_main(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

# tests/test_api.py

def test_create_item(test_client, test_db):
    item_data = {"name": "Test Item", "description": "This is a test item"}
    response = test_client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_read_item(test_client, test_db):
    response = test_client.get("/items/1")
    assert response.status_code == 404  # Assuming item with ID 1 doesn't exist in this test scenario

# tests/test_crud.py

def test_postgres_create_item(test_db):
    from app.crud.postgres import create_item
    from app.models.item import ItemCreate

    item_data = {"name": "Test Item", "description": "This is a test item"}
    item_create = ItemCreate(**item_data)
    item = create_item(test_db, item_create)
    assert item.name == item_create.name
    assert item.description == item_create.description

# tests/test_crud_mongodb.py

@pytest.mark.asyncio
async def test_mongodb_create_item(test_mongodb):
    from app.crud.mongodb import create_item
    from app.models.item import ItemCreate

    item_data = {"name": "Test Item", "description": "This is a test item"}
    item_create = ItemCreate(**item_data)
    item = await create_item(item_create)
    assert item.name == item_create.name
    assert item.description == item_create.description