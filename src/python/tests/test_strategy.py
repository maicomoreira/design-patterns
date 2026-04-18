from designpatterns_examples.behavioral.strategy.payment_processing import (
    GatewayAlpha,
    GatewayBeta,
    PaymentCheckout,
)
from designpatterns_examples.behavioral.strategy.pricing import (
    FixedDiscount,
    NoDiscount,
    Order,
    PercentageDiscount,
)


def test_percentage_discount() -> None:
    o = Order(100.0, PercentageDiscount(10))
    assert o.total() == 90.0


def test_switch_strategy() -> None:
    o = Order(100.0, NoDiscount())
    assert o.total() == 100.0
    o.set_strategy(FixedDiscount(30))
    assert o.total() == 70.0


def test_payment_checkout_uses_gateway() -> None:
    checkout = PaymentCheckout(GatewayAlpha())
    assert checkout.charge(10.0) == "ALPHA:10.00"


def test_payment_checkout_switch_gateway() -> None:
    checkout = PaymentCheckout(GatewayAlpha())
    assert checkout.charge(5.0) == "ALPHA:5.00"
    checkout.set_gateway(GatewayBeta())
    assert checkout.charge(5.0) == "BETA:5.00"
