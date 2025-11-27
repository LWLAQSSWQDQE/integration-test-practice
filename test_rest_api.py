import requests
import pytest
#RESTful API接口测试
BASE_URL = "http://localhost:8000"

def test_get_user():
    r = requests.get(f"{BASE_URL}/users/1")
    assert r.status_code == 200
    assert "id" in r.json()

def test_create_user_missing_field():
    r = requests.post(f"{BASE_URL}/users", json={"name": ""})
    assert r.status_code == 400

def test_update_user():
    r = requests.put(f"{BASE_URL}/users/1", json={"email": "new@example.com"})
    assert r.status_code == 200
    assert r.json()["email"] == "new@example.com"

def test_delete_user():
    r = requests.delete(f"{BASE_URL}/users/1")
    assert r.status_code in (200, 204)
