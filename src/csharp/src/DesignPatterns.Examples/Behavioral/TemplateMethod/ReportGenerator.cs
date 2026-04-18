using System.Text;
using System.Text.Json;

namespace DesignPatterns.Examples.Behavioral.TemplateMethod;

public abstract class ReportGenerator
{
    public string Generate(IReadOnlyList<Dictionary<string, string>> records)
    {
        var header = Header();
        var body = FormatBody(records);
        var footer = Footer();
        return $"{header}\n{body}\n{footer}";
    }

    protected virtual string Header() => "--- Relatório ---";

    protected abstract string FormatBody(IReadOnlyList<Dictionary<string, string>> records);

    protected virtual string Footer() => "--- fim ---";
}

public sealed class CsvReport : ReportGenerator
{
    protected override string FormatBody(IReadOnlyList<Dictionary<string, string>> records)
    {
        if (records.Count == 0)
        {
            return string.Empty;
        }

        var keys = records[0].Keys.ToList();
        var sb = new StringBuilder();
        sb.AppendJoin(',', keys);
        sb.AppendLine();
        foreach (var row in records)
        {
            sb.AppendJoin(',', keys.Select(k => row[k]));
            sb.AppendLine();
        }

        return sb.ToString().TrimEnd();
    }
}

public sealed class JsonReport : ReportGenerator
{
    protected override string FormatBody(IReadOnlyList<Dictionary<string, string>> records)
    {
        return JsonSerializer.Serialize(records, new JsonSerializerOptions { WriteIndented = true });
    }
}
