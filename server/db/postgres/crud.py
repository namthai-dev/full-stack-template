from sqlalchemy.orm import Session
from app.models.item import ItemCreate
from .models import Item as DBItem

def create_item(db: Session, item: ItemCreate):
    db_item = DBItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(DBItem).filter(DBItem.id == item_id).first()

def update_item(db: Session, item_id: int, updated_data: ItemCreate):
    item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if item:
        for key, value in updated_data.model_dump().items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
    return item

def delete_item(db: Session, item_id: int):
    item = db.query(DBItem).filter(DBItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None
