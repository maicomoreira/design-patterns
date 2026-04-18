"""Checkout com gateway de pagamento plugável (Strategy)."""

from __future__ import annotations

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Processa o valor e devolve um identificador de resultado determinístico para testes."""


class GatewayAlpha(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f"ALPHA:{amount:.2f}"


class GatewayBeta(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f"BETA:{amount:.2f}"


class PaymentCheckout:
    def __init__(self, gateway: PaymentGateway) -> None:
        self._gateway = gateway

    def set_gateway(self, gateway: PaymentGateway) -> None:
        self._gateway = gateway

    def charge(self, amount: float) -> str:
        return self._gateway.process_payment(amount)
