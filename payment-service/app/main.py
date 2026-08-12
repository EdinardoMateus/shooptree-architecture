from fastapi import FastAPI
from app.payment_strategy import PaymentContext, CreditCardPayment, PixPayment
from app.event_bus import event_bus

app = FastAPI(title="Payment Service")

def payment_consumer(event):
    if event.get("event_type") == "ORDER_CREATED":
        order_id = event["order_id"]
        amount = 100.0 * event["quantity"]
        strategy = CreditCardPayment()  # pode ser escolhido dinamicamente
        context = PaymentContext(strategy)
        result = context.execute_payment(amount, order_id)
        print(f"[PAYMENT] Pagamento processado: {result}")

# Inscreve o consumidor
event_bus.subscribe(payment_consumer)

@app.get("/pagamentos")
def list_payments():
    return {"payments": []}  # mock

@app.post("/pagamentos")
def process_payment(amount: float, method: str = "credit"):
    if method == "credit":
        strategy = CreditCardPayment()
    elif method == "pix":
        strategy = PixPayment()
    else:
        return {"error": "Método não suportado"}
    context = PaymentContext(strategy)
    result = context.execute_payment(amount, 999)
    return result