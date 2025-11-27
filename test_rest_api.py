import requests
import pytest

# RESTful API 接口测试
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

def test_create_user_success():
    r = requests.post(f"{BASE_URL}/users", json={"name": "Charlie", "email": "charlie@example.com"})
    assert r.status_code == 201
    assert r.json()["name"] == "Charlie"

def test_delete_user():
    # 先创建一个用户
    r = requests.post(f"{BASE_URL}/users", json={"name": "Temp"})
    user_id = r.json()["id"]
    # 删除该用户
    r = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert r.status_code == 200
    # 再次访问应返回 404
    r = requests.get(f"{BASE_URL}/users/{user_id}")
    assert r.status_code == 404
