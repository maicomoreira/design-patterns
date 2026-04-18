namespace DesignPatterns.Examples.Behavioral.ChainOfResponsibility;

public sealed class CreditApplication
{
    public required int Score { get; init; }
    public required decimal RequestedAmount { get; init; }
    public required bool FraudFlag { get; init; }
    public required bool KycVerified { get; init; }
}

public sealed class CreditRejectedException : Exception
{
    public CreditRejectedException(string message) : base(message) { }
}

public abstract class CreditAnalysisHandler
{
    private CreditAnalysisHandler? _next;

    public void SetNext(CreditAnalysisHandler next) => _next = next;

    public abstract void Process(CreditApplication application);

    protected void Forward(CreditApplication application) => _next?.Process(application);
}

public sealed class FraudCheckHandler : CreditAnalysisHandler
{
    public override void Process(CreditApplication application)
    {
        if (application.FraudFlag)
            throw new CreditRejectedException("Reprovado por suspeita de fraude.");
        Forward(application);
    }
}

public sealed class ScoreCheckHandler : CreditAnalysisHandler
{
    private readonly int _minimumScore;

    public ScoreCheckHandler(int minimumScore = 600) => _minimumScore = minimumScore;

    public override void Process(CreditApplication application)
    {
        if (application.Score < _minimumScore)
            throw new CreditRejectedException("Score insuficiente.");
        Forward(application);
    }
}

public sealed class KycCheckHandler : CreditAnalysisHandler
{
    public override void Process(CreditApplication application)
    {
        if (!application.KycVerified)
            throw new CreditRejectedException("KYC não verificado.");
        Forward(application);
    }
}

public sealed class InternalLimitHandler : CreditAnalysisHandler
{
    private readonly decimal _maxAmount;

    public InternalLimitHandler(decimal maxAmount = 50_000m) => _maxAmount = maxAmount;

    public override void Process(CreditApplication application)
    {
        if (application.RequestedAmount > _maxAmount)
            throw new CreditRejectedException("Valor acima do limite interno.");
        Forward(application);
    }
}

public static class CreditAnalysisChainFactory
{
    public static CreditAnalysisHandler BuildDefaultChain()
    {
        var fraud = new FraudCheckHandler();
        var score = new ScoreCheckHandler();
        var kyc = new KycCheckHandler();
        var limit = new InternalLimitHandler();
        fraud.SetNext(score);
        score.SetNext(kyc);
        kyc.SetNext(limit);
        return fraud;
    }
}
