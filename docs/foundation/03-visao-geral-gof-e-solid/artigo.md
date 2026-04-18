# SOLID e GoF: o código que não envelhece

**Trilha:** foundation · **Slug:** `foundation/03-visao-geral-gof-e-solid`

---

## Introdução

A cena é comum: uma funcionalidade simples, que deveria levar dois dias para ser implementada, arrasta-se por duas semanas. O motivo? O código tornou-se um "castelo de cartas". Qualquer alteração em um ponto gera bugs inesperados em módulos teoricamente isolados.

Se você sente que sua equipe gasta mais tempo remediando dívida técnica do que entregando valor, o problema raramente é a linguagem ou o framework. O gargalo costuma estar na fundação: a falta de princípios de design robustos.

No ecossistema de TI atual, onde a agilidade é palavra de ordem, entender **SOLID** e os **Padrões GoF** não é um luxo acadêmico, mas uma competência crítica de sobrevivência para arquitetos e desenvolvedores que buscam escalabilidade e baixo custo de manutenção.

Se você acompanhou a trilha anterior, o nome de **Lucas** já apareceu no cenário da fintech — aqui aprofundamos o *que* muda quando princípios SOLID e padrões GoF entram no jogo para sair do emaranhado de condicionais.

---

## O dilema de Lucas: entre o "pra ontem" e o "bem feito"

Lucas é Tech Lead em uma fintech em rápido crescimento. A empresa precisa integrar novos meios de pagamento mensalmente. No início, Lucas e seu time usavam condicionais simples (`if/else`) para gerenciar as regras de cada operadora.

Os sintomas do problema surgiram rápido:

* **Rigidez:** alterar a lógica de um banco quebrava a integração de outro.
* **Fragilidade:** o arquivo de integração chegou a 5.000 linhas, tornando o code review um pesadelo.
* **Imobilidade:** ninguém tinha coragem de refatorar, temendo o efeito dominó no ambiente de produção.

O impacto para o negócio? O *time-to-market* da fintech despencou. O que era para ser uma vantagem competitiva virou um custo operacional proibitivo.

---

## SOLID: os mandamentos da manutenibilidade

Para resolver o caos de Lucas, precisamos voltar aos fundamentos do **SOLID**. Eles não são regras, são princípios que visam a **coesão** e o **desacoplamento**.

1. **S (Single Responsibility):** uma classe deve ter apenas uma razão para mudar. Se o serviço de pagamento também gera PDFs de recibo, ele está fazendo demais.
2. **O (Open/Closed):** o software deve estar aberto para extensão, mas fechado para modificação. Você deve conseguir adicionar um novo banco sem tocar no código dos bancos que já funcionam.
3. **L (Liskov Substitution):** subtipos devem ser substituíveis por seus tipos base. Se a "Conta Poupança" não permite "Saque", ela não deveria herdar de uma classe que obriga a implementação de saque.
4. **I (Interface Segregation):** não force um cliente a depender de métodos que ele não usa. Interfaces "gordas" criam dependências desnecessárias.
5. **D (Dependency Inversion):** dependa de abstrações, não de implementações. O seu código de alto nível não deve conhecer os detalhes do banco de dados ou da API externa.

---

## GoF: onde a teoria ganha nome e forma

Enquanto o SOLID nos dá a filosofia, o **GoF (Gang of Four)** nos entrega as plantas arquitetônicas. Os 23 padrões de projeto clássicos são soluções comprovadas para problemas recorrentes.

No caso do Lucas, dois padrões se destacam:

* **Strategy:** permite que ele defina uma família de algoritmos de pagamento, encapsule cada um e os torne intercambiáveis.
* **Factory Method:** centraliza a criação dos objetos de integração, escondendo a complexidade de qual classe instanciar.

### Na prática: refatorando o caos

Em vez de um `switch` infinito, a solução passa a utilizar uma interface comum e estratégias específicas:

```csharp
// Abstração (D do SOLID)
public interface IPagamentoStrategy {
    void Processar(decimal valor);
}

// Implementação específica (S do SOLID)
public class PagamentoPix : IPagamentoStrategy {
    public void Processar(decimal valor) { /* Lógica específica do Pix */ }
}

// Contexto que não muda ao adicionar novos métodos (O do SOLID)
public class ProcessadorPagamentos {
    public void Executar(IPagamentoStrategy strategy, decimal valor) {
        strategy.Processar(valor);
    }
}
```

---

## Síntese executiva: por que investir nisso agora?

Para gestores e executivos, a adoção desses padrões reflete em três indicadores financeiros:

1. **Redução do TCO (Total Cost of Ownership):** código limpo é mais barato de manter a longo prazo.
2. **Aumento da velocidade (*velocity*):** desenvolvedores entregam mais rápido quando o código é previsível e testável.
3. **Retenção de talentos:** bons profissionais sentem-se frustrados em ambientes de código legado mal estruturado.

---

## Conclusão: engenharia ou artesanato?

Design Patterns e SOLID não servem para tornar o sistema "bonito", mas para torná-lo **viável**. Um sistema sem esses princípios pode até funcionar hoje, mas ele nasce com uma data de validade curta e um custo de evolução crescente.

O desafio para o arquiteto moderno é saber o equilíbrio: aplicar o padrão certo no momento certo, evitando o *overengineering* (complicar o simples) e o *underengineering* (negligenciar a estrutura).

**Na sua organização, os padrões de projeto são vistos como aceleradores de entrega ou como uma barreira burocrática no desenvolvimento?**

---

## Onde está o código neste repositório

- **Este artigo (visão geral GoF e SOLID):** `docs/foundation/03-visao-geral-gof-e-solid/artigo.md`
- **Strategy (aprofundamento do padrão):** [docs/patterns/behavioral/strategy/artigo.md](../../patterns/behavioral/strategy/artigo.md) — a mesma ideia de **estratégias de pagamento intercambiáveis** via contrato + implementações.
- **Factory Method:** [docs/patterns/creational/factory-method/README.md](../../patterns/creational/factory-method/README.md) — pasta alinhada ao catálogo GoF; artigo e exemplos de código estão *a publicar* (placeholder no repositório).
- **Python:** `src/python/src/designpatterns_examples/behavioral/strategy/` — estratégias de preço/desconto (`pricing`) e processamento de pagamento com provedores plugáveis (`payment_processing`).
- **C#:** `src/csharp/src/DesignPatterns.Examples/Behavioral/Strategy/` — espelhado (preços + pagamentos).
