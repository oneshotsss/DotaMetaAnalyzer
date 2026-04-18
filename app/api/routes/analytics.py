from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.services import analytics_service

router = APIRouter(prefix="/api/v1/analytics", tags=["analytics"])

@router.get("/top-heroes")
def get_top_heroes(limit: int = 5, db: Session = Depends(get_db)):
    """Get top heroes by winrate."""
    return analytics_service.get_top_heroes_by_winrate(db, limit)

@router.get("/top-items")
def get_top_items(limit: int = 5, db: Session = Depends(get_db)):
    """Get top items by winrate."""
    return analytics_service.get_top_items_by_winrate(db, limit)

