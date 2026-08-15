import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.event_bus import event_bus

client = TestClient(app)

# Mock do event_bus para não propagar eventos reais
@pytest.fixture(autouse=True)
def mock_event_bus(monkeypatch):
    def mock_publish(event):
        print(f"[MOCK] Evento publicado: {event}")
    monkeypatch.setattr(event_bus, "publish", mock_publish)

def test_list_products():
    response = client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product():
    product = {"id": 3, "name": "Teclado", "price": 200.0}
    response = client.post("/produtos", json=product)
    assert response.status_code == 200
    assert response.json()["product"]["id"] == 3

def test_buy_product():
    # Compra não precisa de evento real, pois mockamos
    response = client.post("/comprar/1?quantity=2")
    assert response.status_code == 200
    assert "order_id" in response.json()