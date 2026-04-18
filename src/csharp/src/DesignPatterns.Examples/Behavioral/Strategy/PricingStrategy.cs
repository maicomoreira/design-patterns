namespace DesignPatterns.Examples.Behavioral.Strategy;

public interface IPricingStrategy
{
    decimal Discount(decimal subtotal);
}

public sealed class NoDiscount : IPricingStrategy
{
    public decimal Discount(decimal subtotal) => 0m;
}

public sealed class PercentageDiscount : IPricingStrategy
{
    private readonly decimal _percent;

    public PercentageDiscount(decimal percent) => _percent = percent;

    public decimal Discount(decimal subtotal) => subtotal * (_percent / 100m);
}

public sealed class FixedDiscount : IPricingStrategy
{
    private readonly decimal _amount;

    public FixedDiscount(decimal amount) => _amount = amount;

    public decimal Discount(decimal subtotal) => subtotal < _amount ? subtotal : _amount;
}

public sealed class Order
{
    private decimal _subtotal;
    private IPricingStrategy _strategy;

    public Order(decimal subtotal, IPricingStrategy strategy)
    {
        _subtotal = subtotal;
        _strategy = strategy;
    }

    public void SetStrategy(IPricingStrategy strategy) => _strategy = strategy;

    public decimal Total()
    {
        var d = _strategy.Discount(_subtotal);
        var t = _subtotal - d;
        return t < 0 ? 0 : t;
    }
}
