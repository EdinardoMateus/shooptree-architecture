from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_payment():
    response = client.post("/pagamentos", params={"amount": 100, "method": "credit"})
    assert response.status_code == 200
    assert response.json()["method"] == "credit_card"

def test_process_payment_invalid():
    response = client.post("/pagamentos", params={"amount": 100, "method": "invalid"})
    assert response.status_code == 200
    assert "error" in response.json()