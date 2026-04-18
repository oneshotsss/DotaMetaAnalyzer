from fastapi import FastAPI
from app.db.session import engine
from app.db.models import Base
from app.api.routes import heroes, items, analytics

# Створювати таблиці при запуску
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dota Meta Analyzer", version="1.0.0")

# Реєструємо routes
app.include_router(heroes.router)
app.include_router(items.router)
app.include_router(analytics.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
