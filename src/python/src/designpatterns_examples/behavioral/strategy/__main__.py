"""Demonstração: Strategy — preços e, em seguida, gateways de pagamento."""

from designpatterns_examples.behavioral.strategy.payment_processing import (
    GatewayAlpha,
    GatewayBeta,
    PaymentCheckout,
)
from designpatterns_examples.behavioral.strategy.pricing import (
    FixedDiscount,
    Order,
    PercentageDiscount,
)


def main() -> None:
    print("--- Pricing (desconto) ---")
    order = Order(100.0, PercentageDiscount(10))
    print(order.total())
    order.set_strategy(FixedDiscount(15.0))
    print(order.total())

    print("--- Payment (gateway) ---")
    checkout = PaymentCheckout(GatewayAlpha())
    print(checkout.charge(42.0))
    checkout.set_gateway(GatewayBeta())
    print(checkout.charge(42.0))


if __name__ == "__main__":
    main()
