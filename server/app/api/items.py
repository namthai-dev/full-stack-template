from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.item import Item, ItemCreate
from app.models.auth import User
from db.postgres import crud as postgres
from app.dependencies.auth import get_current_user
from app.dependencies.database import get_postgres_db

router = APIRouter()

@router.post("/items/", response_model=Item)
async def create_item(item: ItemCreate, user: User = Depends(get_current_user), db: Session = Depends(get_postgres_db)):
    print(user)
    return postgres.create_item(db, item)

@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, db: Session = Depends(get_postgres_db)):
    item = postgres.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_data: ItemCreate, db: Session = Depends(get_postgres_db)):
    item = postgres.update_item(db, item_id, updated_data)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int, db: Session = Depends(get_postgres_db)):
    item = postgres.delete_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
