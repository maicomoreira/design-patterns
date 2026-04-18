# Strategy: trocar regras sem reescrever o mundo

**Categoria GoF:** comportamental. **Slug:** `behavioral/strategy`

---

## Introdução

Regras de negócio mudam — promoções, impostos, políticas de frete. Se o código central está cheio de `if/else` ou `switch` gigante, cada mudança vira **risco** e **conflito** em merge. O padrão **Strategy** encapsula **famílias de algoritmos**, torna-os **intercambiáveis** e deixa o contexto (`Context`) desacoplado dos detalhes.

Para arquitetos e tech leads, Strategy é peça-chave de **extensibilidade**: novas regras entram como **novas classes**, não como mais um ramo no meio de um método de quinhentas linhas.

---

## Contexto e problema

**Cenário:** um módulo de pedidos calcula total com desconto. Começa com um tipo; depois vêm cupom percentual, valor fixo, desconto progressivo. O método `CalculateTotal` vira um espaguete.

**Personagens:** product owner pedindo novas promoções toda semana; desenvolvedores com medo de tocar no “cálculo central”; QA testando combinações impossíveis porque o código permite estados estranhos.

- **Onde aparece:** preços, roteamento, validação plugável, compressão, serialização.
- **Sintomas:** crescimento de condicionais; duplicação de pré/pós-processamento em cada ramo.
- **Impactos:** bugs de regra de negócio; lentidão para experimentar (A/B, campanhas).

---

## Conceito técnico central

**Definição:** **Strategy** define uma família de algoritmos, os encapsula e os torna intercambiáveis (GoF). O contexto delega a um **objeto estratégia** com interface comum.

- **O que é:** composição sobre condicionais — “comportamento plugável”.
- **O que não é:** Template Method (fluxo fixo com herança); Strategy troca **algoritmo inteiro** em tempo de execução via interface comum.

**Vantagens:** aberto/fechado (estender sem modificar o núcleo); testes unitários por estratégia.

**Limitações:** mais classes; pode ser excesso se há **uma** regra estável para sempre.

**Analogia:** **formas de pagamento** no checkout — o carrinho não precisa saber se o PIX cobra igual ao cartão; ele só chama “pagar”.

**Anti-padrões:** estratégias anêmicas que só encapsulam constantes; contexto que ainda conhece implementações concretas demais (falta de interface ou DI).

---

## Implicações práticas e aplicação

**Arquitetura:** exponha uma **interface** de estratégia no domínio; injete implementações na borda (API, jobs). Evite service locator escondido.

**Processo:** novas campanhas viram **novas classes** + testes isolados; feature flags podem selecionar estratégia.

**Código (ideia):** `Order` mantém `subtotal` e referência a `IPricingStrategy`; `set_strategy` ou construtor definem comportamento (como nos exemplos deste repositório).

**Diagrama:** `Context` → interface `Strategy` ← `ConcreteStrategyA/B`.

---

## Síntese executiva

1. Strategy remove **condicionais de domínio** do núcleo do fluxo.
2. Combina bem com **injeção de dependência** e testes focados.
3. Avalie se precisa de **Factory** ou registro para criar estratégias por nome/código.
4. Nomeie estratégias com **linguagem de negócio**.

---

## Conclusão e apelo à ação

O melhor sinal de Strategy bem aplicado é quando o product percebe **velocidade** nas mudanças de regra — sem aumentar o medo da equipe de tocar no arquivo errado.

**Onde está o código neste repositório**

- Artigo: `docs/patterns/behavioral/strategy/artigo.md`
- Python: `src/python/src/designpatterns_examples/behavioral/strategy/` — `pricing.py` (desconto) e `payment_processing.py` (gateways plugáveis).
- C#: `src/csharp/src/DesignPatterns.Examples/Behavioral/Strategy/` — `PricingStrategy.cs` e `PaymentProcessing.cs`.

---

## Pergunta para o LinkedIn

Em qual parte do seu sistema as regras mudam com mais frequência — e hoje isso está modelado como Strategy (ou outro plug-in), ou ainda preso a `if` e `switch`?
