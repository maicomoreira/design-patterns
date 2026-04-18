# Contribuindo

Obrigado por considerar contribuir com este repositório didático sobre **padrões de projeto GoF**, fundamentos de POO/SOLID e exemplos em **Python** e **C#**.

## Objetivo e tom

- Mantenha o foco educativo: clareza e consistência com o [roadmap](docs/roadmap.md).
- **Artigos (texto-base LinkedIn):** commitados em **`docs/`** (pastas `foundation/`, `patterns/...`, etc.), usando o [template](docs/templates/artigo-linkedin.md). Um guia de estilo **adicional** fora do repositório é opcional — *URL no [README](README.md)*, se existir.
- Novos padrões devem ser **espelhados** em Python e C# quando fizer sentido (mesmo exemplo conceitual, duas implementações).

## Onde commitar documentação

- **Fonte canônica:** todo artigo do currículo e material didático principal deve existir em **`docs/**/*.md`** (em geral `artigo.md` na pasta do tópico, mais `README.md` do padrão quando aplicável). Revise via **PR** neste repositório.
- **GitHub Wiki** (`design-patterns.wiki`): use só como **índice** com links para arquivos em `main`, ou para notas legadas explicitamente marcadas. **Não** use a wiki como único destino de artigos novos do currículo — isso quebra revisão, CI e ligação com `src/`.
- Ao incluir um padrão ou nova seção na trilha: pasta sob `docs/patterns/...` ou `docs/foundation/...`, atualize [docs/roadmap.md](docs/roadmap.md) e os índices em [README.md](README.md) / [docs/README.md](docs/README.md) quando fizer sentido.

## Como propor uma mudança

1. Abra uma **issue** (ou discuta na PR) com o padrão/tópico e o que pretende entregar (docs, código, testes).
2. Siga a taxonomia em `docs/patterns/` (`creational`, `structural`, `behavioral`) e a trilha em `docs/foundation/` quando aplicável.
3. Para artigos novos, use o [template](docs/templates/artigo-linkedin.md); o commit fica em `docs/`, não apenas na wiki.
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
