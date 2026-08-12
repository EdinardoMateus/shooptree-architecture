from fastapi import FastAPI
from app.event_bus import event_bus

app = FastAPI(title="Notification Service")

def notification_consumer(event):
    if event.get("event_type") == "ORDER_CREATED":
        print(f"[NOTIFICATION] Enviando e-mail: Pedido {event['order_id']} foi criado!")
        print(f"[NOTIFICATION] E-mail enviado para cliente sobre o produto {event['product_id']}")

event_bus.subscribe(notification_consumer)

@app.get("/")
def root():
    return {"message": "Notification service running"}