# Exemplos em C#

Solução **DesignPatterns**: biblioteca `DesignPatterns.Examples` com namespaces por família/padrão, projeto de demonstração console e testes **xUnit**.

## Convenções

- Introdução geral aos Design Patterns (artigo foundation): [artigo.md](../../docs/foundation/01-introducao-design-patterns/artigo.md).
- Padrões em `src/DesignPatterns.Examples/` (`Creational`, `Structural`, `Behavioral`).
- Executar demo: `dotnet run --project src/DesignPatterns.Demo`
- Testes: `dotnet test`

## Mapa rápido

| Padrão | Namespace principal | Artigo |
|--------|---------------------|--------|
| Singleton | `DesignPatterns.Examples.Creational.Singleton` | [artigo.md](../../docs/patterns/creational/singleton/artigo.md) |
| Template Method | `DesignPatterns.Examples.Behavioral.TemplateMethod` | [artigo.md](../../docs/patterns/behavioral/template-method/artigo.md) |
| Strategy | `DesignPatterns.Examples.Behavioral.Strategy` | [artigo.md](../../docs/patterns/behavioral/strategy/artigo.md) |
| Chain of Responsibility | `DesignPatterns.Examples.Behavioral.ChainOfResponsibility` | [artigo.md](../../docs/patterns/behavioral/chain-of-responsibility/artigo.md) |

Requer **.NET 8 SDK** ([download](https://dotnet.microsoft.com/download)). Índice geral: [docs/patterns](../../docs/patterns/).

### Comandos úteis

```bash
cd src/csharp
dotnet build DesignPatterns.sln
dotnet test DesignPatterns.sln
dotnet run --project src/DesignPatterns.Demo
```
