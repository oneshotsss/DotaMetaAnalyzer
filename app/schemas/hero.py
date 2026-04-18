from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# БАЗОВА СХЕМА - те що може бути у героя
class HeroBase(BaseModel):
    name: str  # Ім'я героя (обов'язково)
    type: Optional[str] = None  # Тип: Melee або Ranged (можна не писати)
    line: Optional[str] = None  # Лінія: Carry, Mid, Support (можна не писати)
    win_rate: Optional[float] = 0.0  # Win rate у відсотках
    pick_rate: Optional[float] = 0.0  # Як часто пікають
    ban_rate: Optional[float] = 0.0  # Як часто банять


# СХЕМА ДЛЯ СТВОРЕННЯ - що ми отримуємо від користувача
class HeroCreate(HeroBase):
    pass  # Те саме що HeroBase


# СХЕМА ДЛЯ ВІДПОВІДІ - що ми відправляємо назад
class HeroResponse(HeroBase):
    id: int  # ID героя з БД
    created_at: datetime  # Коли створили
    updated_at: datetime  # Коли оновили

    class Config:
        from_attributes = True  # Магія для SQLAlchemy

