from fastapi import FastAPI
from app.models import Product
from app.event_bus import event_bus   # importe o event_bus que você criou
import random

app = FastAPI(title="Product Service")

products_db = [
    Product(id=1, name="Notebook", price=4500.00),
    Product(id=2, name="Mouse", price=150.00),
    Product(id=3, name="Smarttv", price=2700.00),
    Product(id=4, name="Desktop", price=3800.00),
    Product(id=5, name="IPHONE", price=6500.00)
]

@app.get("/produtos")
def list_products():
    return products_db

@app.post("/produtos")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Produto criado", "product": product}

@app.post("/comprar/{product_id}")
def buy_product(product_id: int, quantity: int = 1):
    order_id = random.randint(1000, 9999)
    event = {
        "event_type": "ORDER_CREATED",
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity
    }
    event_bus.publish(event)
    print(f"[PRODUCT] Evento publicado: {event}")
    return {"message": "Compra iniciada", "order_id": order_id}