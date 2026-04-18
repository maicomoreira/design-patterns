using DesignPatterns.Examples.Behavioral.TemplateMethod;
using Xunit;

namespace DesignPatterns.Tests;

public class TemplateMethodTests
{
    private static readonly Dictionary<string, string>[] Rows =
    {
        new() { ["a"] = "1", ["b"] = "2" },
    };

    [Fact]
    public void CsvReport_ContainsHeaderAndColumns()
    {
        var report = new CsvReport();
        var outText = report.Generate(Rows);
        Assert.Contains("Relatório", outText);
        Assert.Contains("a", outText);
    }

    [Fact]
    public void JsonReport_ContainsKeys()
    {
        var report = new JsonReport();
        var outText = report.Generate(Rows);
        Assert.Contains("\"a\"", outText);
    }
}
