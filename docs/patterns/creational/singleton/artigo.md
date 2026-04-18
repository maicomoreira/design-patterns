# Uma instância para governar todas? Singleton sem virar gargalo

**Categoria GoF:** criação. **Slug:** `creational/singleton`

---

## Introdução

Em quase todo sistema existe alguma “verdade única”: configuração global, pool de conexão, cliente de log. Sem disciplina, cada módulo cria a sua — e você ganha inconsistência, desperdício e bugs difíceis de reproduzir.

O padrão **Singleton** promete exatamente isso: **uma única instância** de um tipo, com um ponto de acesso global. Parece simples. Na prática, é um dos padrões mais citados — e mais mal aplicados.

Este texto é para quem precisa decidir **quando** o Singleton ajuda na arquitetura e **quando** ele vira dependência oculta, teste frágil e acoplamento forte. A ideia não é demonizar o padrão, mas usá-lo com o mesmo rigor que você espera de uma decisão de API pública.

Por que importa agora? Porque em microsserviços, injeção de dependência e testes automatizados, “global” tem custo. Entender Singleton é treinar o músculo de **estado compartilhado** — competência de arquiteto, não só de sintaxe.

---

## Contexto e problema

**Cenário:** um time entrega features rápido; cada serviço lê variáveis de ambiente no startup e guarda cópias locais. Um dia, alguém altera um flag em tempo de execução em um módulo — e outro módulo continua com o valor antigo.

**Personagens:** o tech lead que quer previsibilidade, o desenvolvedor que só precisa “de um lugar” para buscar config, e a plataforma que exige observabilidade e testes confiáveis.

- **Onde aparece:** acesso a configuração, caches de leitura, clientes HTTP “caros” de criar, loggers.
- **Sintomas:** estado divergente entre partes do sistema; testes que interferem uns nos outros; ordem de inicialização frágil.
- **Impactos:** incidentes intermitentes, retrabalho em QA, medo de refatorar o “objeto global”.

---

## Conceito técnico central

**Definição:** o Singleton **restringe** uma classe a **uma instância** e oferece um **acesso global** a ela (GoF).

- **O que é:** controle explícito de ciclo de vida para algo que **de fato** deve ser único no processo (ou no escopo delimitado).
- **O que não é:** atalho para “variável global porque é mais fácil”; nem todo “único” precisa ser Singleton clássico — muitas vezes **injeção de dependência** com escopo singleton no container resolve melhor.

**Vantagens:** ponto único de verdade; economia de recursos quando a instância é cara; coordenação centralizada (com cuidado).

**Limitações:** estado global dificulta testes e paralelismo; acoplamento ao tipo concreto; em cenários distribuídos, “único” **no processo** não implica “único no sistema”.

**Analogia:** um **registro civil** — há um lugar oficial para consultar “quem é essa entidade”. Útil quando a regra de negócio exige unicidade. Se cada esquina mantivesse uma cópia divergente dos dados, o caos seria inevitável.

**Anti-padrões relacionados:** Singleton **excessivo**; “Deus” que centraliza tudo; uso de Singleton para mascarar falta de desenho de módulos.

---

## Implicações práticas e aplicação

**Arquitetura:** prefira **interfaces** e composição; se usar Singleton clássico, documente o **escopo** (processo, AppDomain, thread). Em .NET, `Lazy<T>` ou inicialização lazy thread-safe são comuns; em Python, `__new__` com trava ou metaclasse — sempre com atenção a testes.

**Processo:** code review deve perguntar: “Isso precisa ser global?” e “Como testamos com e sem esse estado?”.

**Ferramentas:** DI containers (singleton lifetime), factories explícitas, ou encapsulamento atrás de interface para facilitar mocks.

**Código (ideia):** uma instância lazy thread-safe em C#:

```csharp
public sealed class AppSettings
{
    private static readonly Lazy<AppSettings> Lazy = new(() => new AppSettings());
    public static AppSettings Instance => Lazy.Value;
    private AppSettings() { }
    // ...
}
```

**Diagrama conceitual:** um único objeto `Singleton` referenciado por vários clientes; evite setas de dependência de volta para “todo o resto”.

---

## Síntese executiva

1. Singleton resolve **unicidade de instância**, não todo problema de configuração.
2. Estado global exige **estratégia de teste** (reset, fakes, ou não usar Singleton nos testes).
3. Em sistemas modernos, muitas vezes o “singleton” certo é um **serviço com escopo singleton** na injeção de dependência.
4. O maior risco não é o padrão — é **acoplamento oculto** e **concorrência** mal modelada.

---

## Conclusão e apelo à ação

Singleton é ferramenta de **arquitetura**, não atalho de teclado. Se no seu contexto a unicidade é real e o escopo é claro, use com orgulho — e documente. Se você está usando só porque “sempre foi assim”, pause e redesenhe fronteiras.

**Onde está o código neste repositório**

- Artigo: `docs/patterns/creational/singleton/artigo.md`
- Python: `src/python/src/designpatterns_examples/creational/singleton/`
- C#: `src/csharp/src/DesignPatterns.Examples/Creational/Singleton/`

---

## Pergunta para o LinkedIn

Onde você traça a linha entre “singleton de verdade” e “global que atrapalha testes e evolução” no seu time — e que sinal no código costuma denunciar que essa linha foi cruzada?
