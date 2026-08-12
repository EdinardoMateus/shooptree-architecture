from kafka import KafkaConsumer
import json
import os
from app.payment_strategy import PaymentContext, CreditCardPayment

KAFKA_BROKER = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

def start_consumer():
    consumer = KafkaConsumer(
        "ecommerce_events",
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    print("[PAYMENT] Aguardando eventos...")
    
    for message in consumer:
        event = message.value
        if event.get("event_type") == "ORDER_CREATED":
            order_id = event["order_id"]
            # Simula cálculo de valor (fixo apenas para exemplo)
            amount = 100.0 * event["quantity"]
            # Aplica Strategy Pattern
            strategy = CreditCardPayment()  # poderia ser escolhido dinamicamente
            context = PaymentContext(strategy)
            result = context.execute_payment(amount, order_id)
            print(f"[PAYMENT] Pagamento processado: {result}")