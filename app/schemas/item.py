from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# БАЗОВА СХЕМА ДЛЯ АЙТЕМУ
class ItemBase(BaseModel):
    name: str  # Ім'я айтему (обов'язково)
    cost: int = 0  # Вартість айтему
    description: Optional[str] = None  # Опис
    popularity: Optional[float] = 0.0  # Популярність
    win_rate: Optional[float] = 0.0  # Win rate


# СХЕМА ДЛЯ СТВОРЕННЯ
class ItemCreate(ItemBase):
    pass


# СХЕМА ДЛЯ ВІДПОВІДІ
class ItemResponse(ItemBase):
    id: int  # ID з БД
    created_at: datetime  # Коли створили
    updated_at: datetime  # Коли оновили

    class Config:
        from_attributes = True

