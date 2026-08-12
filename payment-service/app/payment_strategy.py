from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float, order_id: int) -> dict:
        pass

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount: float, order_id: int) -> dict:
        return {"status": "approved", "method": "credit_card", "amount": amount, "order_id": order_id}

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount: float, order_id: int) -> dict:
        return {"status": "approved", "method": "paypal", "amount": amount, "order_id": order_id}

class PixPayment(PaymentStrategy):
    def process_payment(self, amount: float, order_id: int) -> dict:
        return {"status": "approved", "method": "pix", "amount": amount, "order_id": order_id}

# Contexto que usa a estratégia
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount: float, order_id: int):
        return self._strategy.process_payment(amount, order_id)