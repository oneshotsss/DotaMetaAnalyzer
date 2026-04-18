import sys
import os
import pytest
from fastapi.testclient import TestClient

# Додаємо корінь проєкту до sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from main import app

client = TestClient(app)

def test_create_hero():
    hero_data = {
        "name": "TestHero",
        "type": "Strength",
        "line": "Offlane",
    }
    response = client.post("/api/v1/heroes/", json=hero_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == hero_data["name"]
    assert data["type"] == hero_data["type"]
    assert data["line"] == hero_data["line"]

def test_get_all_heroes():
    response = client.get("/api/v1/heroes/")
    assert response.status_code == 200
    data = response.json()
    assert "heroes" in data
    assert isinstance(data["heroes"], list)

def test_get_hero_by_id():
    # Спочатку створимо героя
    hero_data = {
        "name": "TestHero2",
        "type": "Agility",
        "line": "Safe Lane",
    }
    create_resp = client.post("/api/v1/heroes/", json=hero_data)
    hero_id = create_resp.json()["id"]
    # Тепер отримаємо його за id
    response = client.get(f"/api/v1/heroes/{hero_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == hero_id
    assert data["name"] == hero_data["name"]

def test_update_hero():
    # Створимо героя
    hero_data = {
        "name": "TestHero3",
        "type": "Intelligence",
        "line": "Mid",
    }
    create_resp = client.post("/api/v1/heroes/", json=hero_data)
    hero_id = create_resp.json()["id"]
    # Оновимо героя
    updated_data = {
        "name": "UpdatedHero3",
        "type": "Intelligence",
        "line": "Mid",
    }
    response = client.put(f"/api/v1/heroes/{hero_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]

def test_delete_hero():
    # Створимо героя
    hero_data = {
        "name": "TestHero4",
        "type": "Strength",
        "line": "Offlane",
    }
    create_resp = client.post("/api/v1/heroes/", json=hero_data)
    hero_id = create_resp.json()["id"]
    # Видалимо героя
    response = client.delete(f"/api/v1/heroes/{hero_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Hero deleted"
    # Перевіримо, що героя більше немає
    get_resp = client.get(f"/api/v1/heroes/{hero_id}")
    assert get_resp.status_code == 404
