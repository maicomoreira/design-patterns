namespace DesignPatterns.Examples.Creational.Singleton;

/// <summary>
/// Singleton thread-safe via <see cref="Lazy{T}"/> (equivalente didático ao exemplo em Python).
/// </summary>
public sealed class AppSettings
{
    private static readonly Lazy<AppSettings> LazyInstance = new(() => new AppSettings());

    public static AppSettings Instance => LazyInstance.Value;

    private AppSettings()
    {
    }

    private readonly Dictionary<string, object?> _values = new();

    public void Set(string key, object? value) => _values[key] = value;

    public object? Get(string key) => _values.TryGetValue(key, out var v) ? v : null;
}
