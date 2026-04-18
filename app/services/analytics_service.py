from app.db.models import Hero, Item

def get_top_heroes_by_winrate(db, limit=5):
    heroes = db.query(Hero).order_by(Hero.win_rate.desc()).limit(limit).all()
    return [{
        "id": h.id,
        "name": h.name,
        "win_rate": h.win_rate
    } for h in heroes]

def get_top_items_by_winrate(db, limit=5):
    items = db.query(Item).order_by(Item.win_rate.desc()).limit(limit).all()
    return [{
        "id": i.id,
        "name": i.name,
        "win_rate": i.win_rate
    } for i in items]

