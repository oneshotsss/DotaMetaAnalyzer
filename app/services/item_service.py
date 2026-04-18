from app.db.models import Item

def get_all_items(db):
    return db.query(Item).all()

def get_item_by_id(db, item_id):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db, item_data: dict):
    new_item = Item(**item_data)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def delete_item(db, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False

def update_item(db, item_id: int, item_data):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return None
    item.name = item_data.name
    item.cost = item_data.cost
    item.description = item_data.description
    item.popularity = item_data.popularity
    item.win_rate = item_data.win_rate
    db.commit()
    db.refresh(item)
    return item
