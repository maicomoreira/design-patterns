# Template Method: o esqueleto que salva o time de refazer o mesmo fluxo

**Categoria GoF:** comportamental. **Slug:** `behavioral/template-method`

---

## Introdução

Você já viu três relatórios diferentes que “são quase iguais”: buscar dados, montar cabeçalho, formatar corpo, rodapé — mas cada formato (CSV, PDF, JSON) copiou e colou o fluxo inteiro e só mudou um pedaço? Quando a regra do meio muda, alguém atualiza dois lugares e esquece o terceiro.

**Template Method** resolve exatamente essa classe de problema: **fixar o algoritmo** num lugar e deixar **variar só os passos** que realmente mudam.

É um padrão comportamental: não fala tanto de “estrutura de objetos” quanto de **ordem de operações** e **reuso de fluxo**. Para quem se posiciona como arquiteto, dominar isso é mostrar que você pensa em **processos estáveis** e **variações seguras**.

---

## Contexto e problema

**Cenário:** uma pipeline de exportação cresceu: novos formatos chegam todo sprint. O time duplicou métodos `ExportCsv`, `ExportJson`, `ExportXml` — cada um com seu `try/catch`, validação e logging levemente diferente.

**Personagens:** o desenvolvedor que precisa entregar rápido, o revisor que enxerga duplicação, e o negócio que quer consistência (sempre o mesmo cabeçalho de auditoria, sempre o mesmo rodapé legal).

- **Onde aparece:** pipelines ETL, geração de documentos, fluxos de aprovação com etapas fixas e subpassos customizáveis.
- **Sintomas:** bugs só em um formato; regras transversais implementadas de forma inconsistente.
- **Impactos:** custo de manutenção, risco regulatório (relatórios com rodapés diferentes), lentidão para evoluir.

---

## Conceito técnico central

**Definição:** defina o **esqueleto** de um algoritmo na classe base (método template), e deixe **subclasses** implementarem passos específicos **sem alterar a estrutura** do algoritmo (GoF).

- **O que é:** inversão parcial de controle — o fluxo “de cima” chama ganchos (`abstract`/`virtual`) implementados “de baixo”.
- **O que não é:** Strategy (família inteira de algoritmos intercambiáveis); Template Method costuma usar **herança**, Strategy frequentemente **composição**.

**Vantagens:** reuso máximo do fluxo; um só lugar para invariantes (validação, logging, transação).

**Limitações:** herança pode acoplar; hierarquias profundas ficam rígidas se mal desenhadas.

**Analogia:** um **checklist de cozinha**: a ordem “preparar → cozinhar → servir” é fixa; o molho muda conforme o prato.

**Anti-padrões:** template gigante com dezenas de ganchos opcionais confusos; base class que conhece demais os detalhes das subclasses.

---

## Implicações práticas e aplicação

**Arquitetura:** coloque invariantes no template (transação, telemetria, políticas). Ganchos devem ser **pequenos e nomeados**.

**Processo:** ao adicionar um novo formato, o time implementa só os passos novos — code review foca em **paridade** entre formatos.

**Código (ideia):** fluxo fixo `Generate`, corpo variável `_format_body` (como nos exemplos deste repositório em Python e C#).

**Diagrama:** caixa “Template Method” no centro com setas para operações primitivas opcionais/obrigatórias nas subclasses.

---

## Síntese executiva

1. Template Method protege o **fluxo** e liberta as **variações**.
2. Funciona melhor quando há **passos claros** e pouca necessidade de combinar algoritmos em runtime.
3. Se a variação explode em muitos tipos ortogonais, avalie **Strategy** ou composição.
4. Bons templates são **curtos** e com nomes que o negócio entende.

---

## Conclusão e apelo à ação

Antes de copiar mais um export, desenhe o fluxo único. Seja o profissional que reduz **surpresas** entre formatos — isso é maturidade de engenharia.

**Onde está o código neste repositório**

- Artigo: `docs/patterns/behavioral/template-method/artigo.md`
- Python: `src/python/src/designpatterns_examples/behavioral/template_method/`
- C#: `src/csharp/src/DesignPatterns.Examples/Behavioral/TemplateMethod/`

---

## Pergunta para o LinkedIn

Qual foi a última vez que você unificou um fluxo duplicado com Template Method (ou decidiu não usar herança) — o que pesou mais na decisão: time-to-market ou flexibilidade futura?
