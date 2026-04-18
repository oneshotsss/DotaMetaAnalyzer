from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.services import item_service
from app.schemas.item import ItemCreate

router = APIRouter(prefix="/api/v1/items", tags=["items"])


@router.get("/")
def get_all_items(db: Session = Depends(get_db)):
    """Get all items."""
    items = item_service.get_all_items(db)
    return {"total": len(items), "items": items}


@router.get("/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    """Get item by ID."""
    item = item_service.get_item_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """Create a new item."""
    item_data = {
        "name": item.name,
        "cost": item.cost,
        "description": item.description or "",
        "popularity": item.popularity,
        "win_rate": item.win_rate,
    }
    new_item = item_service.create_item(db, item_data)
    return new_item


@router.put("/{item_id}")
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    """Update item by ID."""
    updated_item = item_service.update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete item by ID."""
    deleted = item_service.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
