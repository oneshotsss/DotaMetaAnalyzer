import sys
import os
import pytest
from fastapi.testclient import TestClient

# Додаємо корінь проєкту до sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from main import app

client = TestClient(app)

def test_create_item():
    item_data = {
        "name": "TestItem",
        "cost": 1000,
        "description": "Test item description",
        "popularity": 0.5,
        "win_rate": 0.6
    }
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["cost"] == item_data["cost"]
    assert data["description"] == item_data["description"]
    assert data["popularity"] == item_data["popularity"]
    assert data["win_rate"] == item_data["win_rate"]

def test_get_all_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert isinstance(data["items"], list)

def test_get_item_by_id():
    # Спочатку створимо предмет
    item_data = {
        "name": "TestItem2",
        "cost": 2000,
        "description": "Another item",
        "popularity": 0.7,
        "win_rate": 0.8
    }
    create_resp = client.post("/api/v1/items/", json=item_data)
    item_id = create_resp.json()["id"]
    # Тепер отримаємо його за id
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == item_data["name"]

def test_update_item():
    # Створимо предмет
    item_data = {
        "name": "TestItem3",
        "cost": 3000,
        "description": "Update item",
        "popularity": 0.2,
        "win_rate": 0.3
    }
    create_resp = client.post("/api/v1/items/", json=item_data)
    item_id = create_resp.json()["id"]
    # Оновимо предмет
    updated_data = {
        "name": "UpdatedItem3",
        "cost": 3500,
        "description": "Updated description",
        "popularity": 0.4,
        "win_rate": 0.5
    }
    response = client.put(f"/api/v1/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]
    assert data["cost"] == updated_data["cost"]

def test_delete_item():
    # Створимо предмет
    item_data = {
        "name": "TestItem4",
        "cost": 4000,
        "description": "Delete item",
        "popularity": 0.1,
        "win_rate": 0.2
    }
    create_resp = client.post("/api/v1/items/", json=item_data)
    item_id = create_resp.json()["id"]
    # Видалимо предмет
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Item deleted"
    # Перевіримо, що предмета більше немає
    get_resp = client.get(f"/api/v1/items/{item_id}")
    assert get_resp.status_code == 404

