using DesignPatterns.Examples.Creational.Singleton;
using Xunit;

namespace DesignPatterns.Tests;

public class SingletonTests
{
    [Fact]
    public void Instance_IsSameReference()
    {
        var a = AppSettings.Instance;
        var b = AppSettings.Instance;
        Assert.Same(a, b);
    }

    [Fact]
    public void Instance_SharesState()
    {
        var key = $"k_{Guid.NewGuid():N}";
        AppSettings.Instance.Set(key, 1);
        Assert.Equal(1, AppSettings.Instance.Get(key));
    }
}
