# Documentação do repositório

## Fonte canônica

Os **artigos didáticos** e o **currículo** vivem neste repositório, em Markdown, sob **`docs/`**. Eles são revisados por PR junto com o código e o CI. A [GitHub Wiki](https://github.com/maicomoreira/design-patterns/wiki) do projeto é apenas um **atalho de navegação** (e pode guardar páginas legadas); **não** substitui nem duplica o papel de `docs/` como referência principal.

- **[Roadmap didático](roadmap.md)** — mapeamento do [README principal](../README.md) para pastas de artigos e código.
- **[Template de artigo](templates/artigo-linkedin.md)** — esqueleto com placeholders para novos textos.
- **Guia de estilo / redação:** use o template acima e, se existir, um guia público opcional indicado no [README raiz](../README.md). Um documento de apoio local opcional pode ser ignorado pelo Git (ver `.gitignore`).

### Onde criar um artigo novo

| Tipo de conteúdo | Pasta |
|------------------|--------|
| Trilha introdutória (POO, intro, visão GoF/SOLID) | [`foundation/`](foundation/) — tipicamente `artigo.md` na pasta numerada |
| Padrão GoF | [`patterns/`](patterns/) (`creational`, `structural`, `behavioral`) — `artigo.md` + `README.md` conforme o padrão já existente |
| Temas transversais | [`cross-cutting/`](cross-cutting/) |
| Diagramas Mermaid ou imagens de apoio | [`diagrams/`](diagrams/) |

Sempre alinhe ao **[roadmap](roadmap.md)** quando o artigo fizer parte do currículo; atualize o roadmap se incluir um padrão ou seção nova na trilha.

### Nota sobre a wiki (auditoria)

A wiki continha uma **Home** espelhando o roteiro do README e **subpáginas** com rascunhos (HTML/imagens) que podem diferir dos `artigo.md` em `docs/`. A política adotada é: **`docs/` é a verdade para texto didático versionado**; páginas antigas na wiki ficam como legado até eventual migração ou podem ser apenas links na Home da wiki.

---

## Índice rápido

- **`foundation/`** — trilha introdutória (POO, SOLID, visão geral GoF). Artigos: [foundation/01-introducao-design-patterns/artigo.md](foundation/01-introducao-design-patterns/artigo.md) · [foundation/02-revisao-poo/artigo.md](foundation/02-revisao-poo/artigo.md) · [foundation/03-visao-geral-gof-e-solid/artigo.md](foundation/03-visao-geral-gof-e-solid/artigo.md)
- **`patterns/`** — padrões GoF por família (criação, estrutura, comportamento).
- **`cross-cutting/`** — temas transversais (anti-padrões).
- **`diagrams/`** — diagramas Mermaid.
