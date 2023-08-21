from app.models.item import ItemCreate
from models import Item

async def create_item(item: ItemCreate):
    db_item = Item(**item.model_dump())
    await db_item.insert_one(db_item)
    return db_item

async def get_item(item_id: int):
    item = await Item.find_one({"id": item_id})
    return item

async def update_item(item_id: int, updated_data: ItemCreate):
    item = await Item.find_one({"id": item_id})
    if item:
        for key, value in updated_data.model_dump().items():
            setattr(item, key, value)
        await item.commit()
    return item

async def delete_item(item_id: int):
    item = await Item.find_one({"id": item_id})
    if item:
        await item.delete()
        return item
    return None
