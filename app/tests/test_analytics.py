import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from main import app

client = TestClient(app)

def test_top_heroes():
    response = client.get("/api/v1/analytics/top-heroes?limit=3")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 3
    for hero in data:
        assert "name" in hero
        assert "win_rate" in hero

def test_top_items():
    response = client.get("/api/v1/analytics/top-items?limit=3")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 3
    for item in data:
        assert "name" in item
        assert "win_rate" in item

