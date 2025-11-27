import requests
import pytest
#微服务组件集成测试
USER_SERVICE = "http://localhost:5001"
ORDER_SERVICE = "http://localhost:5002"
PAYMENT_SERVICE = "http://localhost:5003"

def test_user_order_flow():
    r = requests.get(f"{USER_SERVICE}/users/1/orders")
    assert r.status_code == 200
    orders = r.json()
    assert isinstance(orders, list)

def test_order_payment_flow():
    r = requests.get(f"{ORDER_SERVICE}/orders/123/payment")
    assert r.status_code == 200
    payment = r.json()
    assert "status" in payment

def test_payment_service_unavailable(monkeypatch):
    def fake_get(*args, **kwargs):
        class FakeResponse:
            status_code = 503
            def json(self): return {"error":"Service Unavailable"}
        return FakeResponse()
    monkeypatch.setattr(requests, "get", fake_get)
    r = requests.get(f"{PAYMENT_SERVICE}/pay/123")
    assert r.status_code == 503
