using DesignPatterns.Examples.Behavioral.ChainOfResponsibility;
using Xunit;

namespace DesignPatterns.Tests;

public class ChainOfResponsibilityTests
{
    [Fact]
    public void Chain_Passes_When_AllRulesOk()
    {
        var chain = CreditAnalysisChainFactory.BuildDefaultChain();
        var app = new CreditApplication
        {
            Score = 700,
            RequestedAmount = 10_000m,
            FraudFlag = false,
            KycVerified = true,
        };
        chain.Process(app);
    }

    [Fact]
    public void Chain_Rejects_OnFraud()
    {
        var chain = CreditAnalysisChainFactory.BuildDefaultChain();
        var app = new CreditApplication
        {
            Score = 700,
            RequestedAmount = 1_000m,
            FraudFlag = true,
            KycVerified = true,
        };
        var ex = Assert.Throws<CreditRejectedException>(() => chain.Process(app));
        Assert.Contains("fraude", ex.Message);
    }

    [Fact]
    public void Chain_Rejects_OnScore()
    {
        var chain = CreditAnalysisChainFactory.BuildDefaultChain();
        var app = new CreditApplication
        {
            Score = 400,
            RequestedAmount = 1_000m,
            FraudFlag = false,
            KycVerified = true,
        };
        var ex = Assert.Throws<CreditRejectedException>(() => chain.Process(app));
        Assert.Contains("Score", ex.Message);
    }

    [Fact]
    public void FraudRunsBeforeScore_HighScoreRequirementStillFailsOnFraud()
    {
        var fraud = new FraudCheckHandler();
        var score = new ScoreCheckHandler(800);
        fraud.SetNext(score);

        var app = new CreditApplication
        {
            Score = 400,
            RequestedAmount = 1_000m,
            FraudFlag = true,
            KycVerified = true,
        };
        var ex = Assert.Throws<CreditRejectedException>(() => fraud.Process(app));
        Assert.Contains("fraude", ex.Message);
    }

    [Fact]
    public void Chain_Rejects_OnKyc()
    {
        var chain = CreditAnalysisChainFactory.BuildDefaultChain();
        var app = new CreditApplication
        {
            Score = 700,
            RequestedAmount = 5_000m,
            FraudFlag = false,
            KycVerified = false,
        };
        var ex = Assert.Throws<CreditRejectedException>(() => chain.Process(app));
        Assert.Contains("KYC", ex.Message);
    }

    [Fact]
    public void Chain_Rejects_OnInternalLimit()
    {
        var chain = CreditAnalysisChainFactory.BuildDefaultChain();
        var app = new CreditApplication
        {
            Score = 700,
            RequestedAmount = 100_000m,
            FraudFlag = false,
            KycVerified = true,
        };
        var ex = Assert.Throws<CreditRejectedException>(() => chain.Process(app));
        Assert.Contains("limite", ex.Message);
    }
}
