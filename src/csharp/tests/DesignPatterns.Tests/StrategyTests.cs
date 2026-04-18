using DesignPatterns.Examples.Behavioral.Strategy;
using Xunit;

namespace DesignPatterns.Tests;

public class StrategyTests
{
    [Fact]
    public void PercentageDiscount_AppliesCorrectly()
    {
        var order = new Order(100m, new PercentageDiscount(10m));
        Assert.Equal(90m, order.Total());
    }

    [Fact]
    public void SwitchStrategy_UpdatesTotal()
    {
        var order = new Order(100m, new NoDiscount());
        Assert.Equal(100m, order.Total());
        order.SetStrategy(new FixedDiscount(30m));
        Assert.Equal(70m, order.Total());
    }

    [Fact]
    public void PaymentCheckout_UsesGateway()
    {
        var checkout = new PaymentCheckout(new GatewayAlpha());
        Assert.Equal("ALPHA:10.00", checkout.Charge(10m));
    }

    [Fact]
    public void PaymentCheckout_SwitchGateway_UpdatesBehavior()
    {
        var checkout = new PaymentCheckout(new GatewayAlpha());
        Assert.Equal("ALPHA:5.00", checkout.Charge(5m));
        checkout.SetGateway(new GatewayBeta());
        Assert.Equal("BETA:5.00", checkout.Charge(5m));
    }
}
