# Design Patterns

Repositório didático: **padrões GoF (Gang of Four)**, fundamentos de POO/SOLID, artigos no formato LinkedIn e **exemplos espelhados em Python e C#**.

[![CI](https://github.com/maicomoreira/design-patterns/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/maicomoreira/design-patterns/actions/workflows/ci.yml)

- **Licença:** [CC BY-SA 4.0](LICENSE)
- **Como contribuir:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Código de conduta:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) · **Segurança:** [SECURITY.md](SECURITY.md)

| Recurso | Caminho |
|---------|---------|
| Roadmap (currículo → pastas) | [docs/roadmap.md](docs/roadmap.md) |
| Guia de redação de artigos (online) | *URL pública a definir pelos mantenedores* |
| Template de artigo | [docs/templates/artigo-linkedin.md](docs/templates/artigo-linkedin.md) |
| Índice da documentação | [docs/README.md](docs/README.md) |
| Artigo — Introdução aos Design Patterns | [docs/foundation/01-introducao-design-patterns/artigo.md](docs/foundation/01-introducao-design-patterns/artigo.md) |
| Artigo — Revisão de POO | [docs/foundation/02-revisao-poo/artigo.md](docs/foundation/02-revisao-poo/artigo.md) |
| Exemplos Python | [src/python/README.md](src/python/README.md) |
| Exemplos C# | [src/csharp/README.md](src/csharp/README.md) |

## Padrões de Projeto
- Correção
- Robustez
- Flexibilidade
- Reusabilidade
- Eficiência
- Padrões de Interface
- Padrões de Responsabilidade
- Padrões de Construção
- Padrões de Operação
- Padrões de Extensão
- Padrões e Programação GUI
- Padrões Arquiteturais e Frameworks
- Componentes

## Competências
- **Conhecer, Analisar e Projetar Sistemas de Informação com Qualidade.**

## Habilidades
- Analisar, compreender, inferir e descrever sistemas a partir de seus elementos básicos, estudando suas partes.
- Criticar e avaliar documentos técnicos, softwares específicos e projetos, interpretando a situação real do caso específico.
- Sintetizar e expor a situação problema, relacionando elementos fundamentais.
- Dominar vocabulário específico, usando corretamente vocabulários, expressões e termos técnicos em projetos, sistemas e documentos.
- Planejar, programar e projetar a análise ou construção de um software ou projeto em informática.
- Modelar e compreender a análise e a modelagem de soluções para diversos tipos de problemas computacionais.

---

# Conteúdo e Objetivos de Design Patterns

Este conteúdo visa explorar conceitos de Programação Orientada a Objetos (POO), padrões de projeto GoF, princípios SOLID e exemplos práticos em **C#** e **Python**.

**Estrutura de pastas:** taxonomia GoF em [docs/patterns/](docs/patterns/) (`creational`, `structural`, `behavioral`); trilha introdutória em [docs/foundation/](docs/foundation/); anti-padrões em [docs/cross-cutting/antipatterns/](docs/cross-cutting/antipatterns/).

---

## 1. Introdução aos Design Patterns

### Conteúdo:
- Importância dos padrões de projeto para a qualidade de software: correção, robustez, flexibilidade e reusabilidade.
- Conceitos fundamentais de design patterns e como eles se integram na engenharia de software.

### Objetivo:
- Apresentar a relevância e o impacto dos design patterns no desenvolvimento de software de qualidade.

**Artigo (texto-base LinkedIn):** [docs/foundation/01-introducao-design-patterns/artigo.md](docs/foundation/01-introducao-design-patterns/artigo.md)

---

## 2. Revisão de Conceitos de Programação Orientada a Objetos (POO)

### Conteúdo:
- Conceitos de classe, objeto, atributos, propriedades.
- Tipos e relacionamentos em POO.
- Multiplicidade em POO.
- Principais erros e más práticas em POO.

### Prática:
- Ler e criticar modelos de classes e relacionamentos expressos em código (C# e Python).
- Desenvolver exemplos de código em C# e Python para demonstrar relacionamentos e multiplicidade.

### Objetivo:
- Relembrar conceitos fundamentais de POO.
- Diferenciar relacionamentos e analisar exemplos de código.
- Identificar e corrigir más práticas em POO.

**Artigo (texto-base LinkedIn):** [docs/foundation/02-revisao-poo/artigo.md](docs/foundation/02-revisao-poo/artigo.md)

---

## 3. Visão Geral sobre Padrões de Projeto

### Conteúdo:
- Introdução aos padrões GoF: criação, estruturais e comportamentais.
- Princípios SOLID (definição e explicação).
- Erros comuns e benefícios de cada princípio SOLID.

### Prática:
- Implementação de princípios SOLID em C# e Python.
- Exemplos de código utilizando padrões GoF.

### Objetivo:
- Definir e classificar padrões de projeto.
- Aplicar princípios SOLID para melhorar a qualidade do código.

---

## 4. Padrão GoF – Criação de Objetos: Singleton

### Conteúdo:
- Conceito e exemplo de implementação do padrão Singleton.
- Implementação de Singleton em Console, Form e Web.
- Variações do Singleton (Singleton thread-safe, Singleton com Lazy Initialization).

### Prática:
- Implementar o padrão Singleton em diferentes cenários (Console, Web, Form).
- Atividade prática: sobrescrita do método ToString() e uso de StringBuilder.

### Objetivo:
- Definir e demonstrar o padrão Singleton.
- Desenvolver projetos que utilizem o padrão Singleton em diferentes contextos.
- Compreender variações do Singleton e aplicabilidade.

**Material do repositório:** [docs/patterns/creational/singleton/](docs/patterns/creational/singleton/) · Python · C#

---

## 5. Padrão GoF – Comportamental – Template Method

### Conteúdo:
- Conceito do padrão Template Method.
- Contexto de uso e exemplos comuns do Template Method.

### Prática:
- Implementar o padrão Template Method em um projeto prático.

### Objetivo:
- Definir e demonstrar o padrão Template Method.
- Desenvolver um projeto utilizando Template Method.

**Material do repositório:** [docs/patterns/behavioral/template-method/](docs/patterns/behavioral/template-method/) · Python · C#

---

## 6. Padrão GoF – Comportamental – Strategy

### Conteúdo:
- Conceito do padrão Strategy.
- Contexto de uso e vantagens do Strategy em comparação com outras abordagens.

### Prática:
- Implementar o padrão Strategy em um projeto prático.

### Objetivo:
- Definir e demonstrar o padrão Strategy.
- Desenvolver um projeto utilizando o padrão Strategy.

**Material do repositório:** [docs/patterns/behavioral/strategy/](docs/patterns/behavioral/strategy/) · Python · C#

---

## 7. Anti-padrões Comuns em Design Patterns

### Conteúdo:
- Introdução aos anti-padrões: práticas que resolvem problemas de forma inadequada.
- Exemplos de anti-padrões comuns como God Object e Singleton excessivo.

### Objetivo:
- Reconhecer anti-padrões e entender por que são práticas a serem evitadas.
- Evitar armadilhas comuns ao implementar design patterns.

---

## Conclusão e Próximos Passos

Este plano de conteúdo visa fortalecer o entendimento de conceitos fundamentais de POO, padrões de projeto GoF e boas práticas de design, com uma abordagem focada em exemplos práticos e atividades em **C#** e **Python**.

### Próximos Passos:
- Incentivar a exploração de frameworks e bibliotecas que utilizam design patterns.
- Referências para frameworks modernos e padrões adicionais para estudo contínuo.
