"""Strategy: família de algoritmos intercambiáveis."""

from designpatterns_examples.behavioral.strategy.payment_processing import (
    GatewayAlpha,
    GatewayBeta,
    PaymentCheckout,
    PaymentGateway,
)
from designpatterns_examples.behavioral.strategy.pricing import (
    FixedDiscount,
    NoDiscount,
    Order,
    PercentageDiscount,
    PricingStrategy,
)

__all__ = [
    "Order",
    "PricingStrategy",
    "NoDiscount",
    "PercentageDiscount",
    "FixedDiscount",
    "PaymentGateway",
    "GatewayAlpha",
    "GatewayBeta",
    "PaymentCheckout",
]
