using DesignPatterns.Examples.Behavioral.ChainOfResponsibility;
using DesignPatterns.Examples.Behavioral.Strategy;
using DesignPatterns.Examples.Behavioral.TemplateMethod;
using DesignPatterns.Examples.Creational.Singleton;

namespace DesignPatterns.Demo;

internal static class Program
{
    private static void Main()
    {
        RunSingletonDemo();
        Console.WriteLine();
        RunTemplateMethodDemo();
        Console.WriteLine();
        RunStrategyDemo();
        Console.WriteLine();
        RunChainOfResponsibilityDemo();
    }

    private static void RunSingletonDemo()
    {
        Console.WriteLine("=== Singleton ===");
        var a = AppSettings.Instance;
        var b = AppSettings.Instance;
        a.Set("theme", "escuro");
        Console.WriteLine($"Mesma instância: {ReferenceEquals(a, b)}");
        Console.WriteLine($"theme = {b.Get("theme")}");
    }

    private static void RunTemplateMethodDemo()
    {
        Console.WriteLine("=== Template Method ===");
        var rows = new Dictionary<string, string>[]
        {
            new() { ["id"] = "1", ["nome"] = "Ana" },
            new() { ["id"] = "2", ["nome"] = "Bruno" },
        };
        Console.WriteLine(new CsvReport().Generate(rows));
        Console.WriteLine(new JsonReport().Generate(rows));
    }

    private static void RunStrategyDemo()
    {
        Console.WriteLine("=== Strategy (pricing) ===");
        var order = new Order(100m, new PercentageDiscount(10m));
        Console.WriteLine($"10% off: {order.Total()}");
        order.SetStrategy(new FixedDiscount(15m));
        Console.WriteLine($"R$15 off: {order.Total()}");

        Console.WriteLine("=== Strategy (payment gateway) ===");
        var checkout = new PaymentCheckout(new GatewayAlpha());
        Console.WriteLine(checkout.Charge(42m));
        checkout.SetGateway(new GatewayBeta());
        Console.WriteLine(checkout.Charge(42m));
    }

    private static void RunChainOfResponsibilityDemo()
    {
        Console.WriteLine("=== Chain of Responsibility (crédito) ===");
        var chain = CreditAnalysisChainFactory.BuildDefaultChain();

        var ok = new CreditApplication
        {
            Score = 720,
            RequestedAmount = 10_000m,
            FraudFlag = false,
            KycVerified = true,
        };
        Console.WriteLine("Caso aprovado na cadeia:");
        chain.Process(ok);
        Console.WriteLine("  Passou por todas as etapas.");

        var badFraud = new CreditApplication
        {
            Score = 720,
            RequestedAmount = 5_000m,
            FraudFlag = true,
            KycVerified = true,
        };
        Console.WriteLine("Rejeição na fraude:");
        try
        {
            chain.Process(badFraud);
        }
        catch (CreditRejectedException ex)
        {
            Console.WriteLine($"  {ex.Message}");
        }
    }
}
