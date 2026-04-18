from app.db.models import Hero

def get_all_heroes(db):
    return db.query(Hero).all()

def get_hero_by_id(db, hero_id):
    return db.query(Hero).filter(Hero.id == hero_id).first()

def create_hero(db, hero_data: dict):
    new_hero = Hero(**hero_data)
    db.add(new_hero)
    db.commit()
    db.refresh(new_hero)
    return new_hero

def delete_hero(db, hero_id: int):
    hero = db.query(Hero).filter(Hero.id == hero_id).first()
    if hero:
        db.delete(hero)
        db.commit()
        return True
    return False

def update_hero(db, hero_id: int, hero_data):
    hero = db.query(Hero).filter(Hero.id == hero_id).first()
    if not hero:
        return None
    hero.name = hero_data.name
    hero.type = hero_data.type
    hero.line = hero_data.line
    # Якщо є додаткові поля, додати тут
    db.commit()
    db.refresh(hero)
    return hero
