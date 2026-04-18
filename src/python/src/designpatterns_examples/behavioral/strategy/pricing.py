"""Preço de pedido com estratégias de desconto plugáveis."""

from __future__ import annotations

from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def discount(self, subtotal: float) -> float:
        """Retorna o valor do desconto (não o total)."""


class NoDiscount(PricingStrategy):
    def discount(self, subtotal: float) -> float:
        return 0.0


class PercentageDiscount(PricingStrategy):
    def __init__(self, percent: float) -> None:
        self._percent = percent

    def discount(self, subtotal: float) -> float:
        return subtotal * (self._percent / 100.0)


class FixedDiscount(PricingStrategy):
    def __init__(self, amount: float) -> None:
        self._amount = amount

    def discount(self, subtotal: float) -> float:
        return min(self._amount, subtotal)


class Order:
    def __init__(self, subtotal: float, strategy: PricingStrategy) -> None:
        self._subtotal = subtotal
        self._strategy = strategy

    def set_strategy(self, strategy: PricingStrategy) -> None:
        self._strategy = strategy

    def total(self) -> float:
        return max(0.0, self._subtotal - self._strategy.discount(self._subtotal))
