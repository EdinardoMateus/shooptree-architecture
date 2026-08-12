from kafka import KafkaConsumer
import json
import os

KAFKA_BROKER = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

def start_consumer():
    consumer = KafkaConsumer(
        "ecommerce_events",
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    print("[NOTIFICATION] Aguardando eventos...")
    
    for message in consumer:
        event = message.value
        if event.get("event_type") == "ORDER_CREATED":
            print(f"[NOTIFICATION] Enviando e-mail: Pedido {event['order_id']} foi criado!")
            print(f"[NOTIFICATION] E-mail enviado para cliente sobre o produto {event['product_id']}")