# Contribuindo

Obrigado por considerar contribuir com este repositório didático sobre **padrões de projeto GoF**, fundamentos de POO/SOLID e exemplos em **Python** e **C#**.

## Objetivo e tom

- Mantenha o foco educativo: clareza, consistência com o [roadmap](docs/roadmap.md) e com a [estrutura de artigos](docs/estrutura-de-artigos.md).
- Novos padrões devem ser **espelhados** em Python e C# quando fizer sentido (mesmo exemplo conceitual, duas implementações).

## Como propor uma mudança

1. Abra uma **issue** (ou discuta na PR) com o padrão/tópico e o que pretende entregar (docs, código, testes).
2. Siga a taxonomia em `docs/patterns/` (`creational`, `structural`, `behavioral`) e a trilha em `docs/foundation/` quando aplicável.
3. Para artigos novos, use o [template](docs/templates/artigo-linkedin.md) e as diretrizes em [estrutura-de-artigos.md](docs/estrutura-de-artigos.md).
4. Atualize o [README](README.md) ou [docs/README.md](docs/README.md) se adicionar entradas ao índice.

## Verificação local

**Python** (a partir de `src/python/`):

```bash
pip install -e ".[dev]"
pytest
ruff check src tests
```

**C#** (a partir de `src/csharp/`):

```bash
dotnet restore DesignPatterns.sln
dotnet build DesignPatterns.sln --no-restore
dotnet test DesignPatterns.sln --no-build
```

## Commits

Preferimos [Conventional Commits](https://www.conventionalcommits.org/), por exemplo:

- `docs: descreve o padrão X`
- `feat(python): exemplo do padrão Y`
- `feat(csharp): exemplo do padrão Y`
- `test: cobre cenário Z`
- `chore: ajusta CI ou documentação`

## Código de conduta

Participação sujeita ao [Código de Conduta](CODE_OF_CONDUCT.md).

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas nos termos da [LICENSE](LICENSE) (CC BY-SA 4.0), salvo acordo explícito em contrário.
