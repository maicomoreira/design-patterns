# Exemplos em Python

Pacote **`designpatterns_examples`**: padrões GoF organizados por família (`creational`, `structural`, `behavioral`), um subpacote por padrão.

## Convenções

- Introdução geral aos Design Patterns (artigo foundation): [artigo.md](../../docs/foundation/01-introducao-design-patterns/artigo.md).
- Código demonstrativo e testes automatizados (`pytest`) por padrão.
- Executar um exemplo: `python -m designpatterns_examples.behavioral.strategy` (ajuste o caminho do módulo).
- Gestão de dependências: [uv](https://github.com/astral-sh/uv) — ver `pyproject.toml`.

## Mapa rápido

| Padrão | Módulo | Artigo |
|--------|--------|--------|
| Singleton | `designpatterns_examples.creational.singleton` | [artigo.md](../../docs/patterns/creational/singleton/artigo.md) |
| Template Method | `designpatterns_examples.behavioral.template_method` | [artigo.md](../../docs/patterns/behavioral/template-method/artigo.md) |
| Strategy | `designpatterns_examples.behavioral.strategy` | [artigo.md](../../docs/patterns/behavioral/strategy/artigo.md) |
| Chain of Responsibility | `designpatterns_examples.behavioral.chain_of_responsibility` | [artigo.md](../../docs/patterns/behavioral/chain-of-responsibility/artigo.md) |

Índice geral: [docs/patterns](../../docs/patterns/).

### Comandos úteis

Use um **ambiente virtual** (recomendado) para evitar erro de permissão no Python do sistema. Se o `pip` for muito antigo (antes da 21.3), atualize antes do editable: `python -m pip install -U "pip>=21.3" setuptools wheel`.

```bash
cd src/python
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install -U pip setuptools wheel
pip install -e ".[dev]"
pytest -q
python -m designpatterns_examples.creational.singleton
python -m designpatterns_examples.behavioral.template_method
python -m designpatterns_examples.behavioral.strategy
python -m designpatterns_examples.behavioral.chain_of_responsibility
```
