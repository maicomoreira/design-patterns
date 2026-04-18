namespace DesignPatterns.Examples.Behavioral.Strategy;

public interface IPaymentGateway
{
    string ProcessPayment(decimal amount);
}

public sealed class GatewayAlpha : IPaymentGateway
{
    public string ProcessPayment(decimal amount) =>
        FormattableString.Invariant($"ALPHA:{amount:F2}");
}

public sealed class GatewayBeta : IPaymentGateway
{
    public string ProcessPayment(decimal amount) =>
        FormattableString.Invariant($"BETA:{amount:F2}");
}

public sealed class PaymentCheckout
{
    private IPaymentGateway _gateway;

    public PaymentCheckout(IPaymentGateway gateway) => _gateway = gateway;

    public void SetGateway(IPaymentGateway gateway) => _gateway = gateway;

    public string Charge(decimal amount) => _gateway.ProcessPayment(amount);
}
