from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.services import hero_service
from app.schemas import HeroCreate, HeroResponse
router = APIRouter(prefix="/api/v1/heroes", tags=["heroes"])


@router.get("/")
def get_all_heroes(db: Session = Depends(get_db)):
    """Get all heroes."""
    heroes = hero_service.get_all_heroes(db)
    return {"total": len(heroes), "heroes": heroes}


@router.get("/{hero_id}")
def get_hero(hero_id: int, db: Session = Depends(get_db)):
    """Get hero by ID."""
    hero = hero_service.get_hero_by_id(db, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.post("/")
def create_hero(hero: HeroCreate, db: Session = Depends(get_db)):
    hero_data = {
        "name": hero.name,
        "type": hero.type,
        "line": hero.line,
        "win_rate": 0.0,
        "pick_rate": 0.0,
        "ban_rate": 0.0,
    }
    new_hero = hero_service.create_hero(db, hero_data)
    return new_hero


@router.put("/{hero_id}")
def update_hero(hero_id: int, hero: HeroCreate, db: Session = Depends(get_db)):
    """Update hero by ID."""
    updated_hero = hero_service.update_hero(db, hero_id, hero)
    if not updated_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return updated_hero


@router.delete("/{hero_id}")
def delete_hero(hero_id: int, db: Session = Depends(get_db)):
    """Delete hero by ID."""
    deleted = hero_service.delete_hero(db, hero_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Hero not found")
    return {"detail": "Hero deleted"}
