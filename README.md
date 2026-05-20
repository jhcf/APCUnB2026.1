# APCUnB2026.1

Repositório público da turma 07 da disciplina Algoritmos e Programação de Computadores da UnB no semestre 2026.1, sob responsabilidade do Prof. Jorge Henrique Cabral Fernandes

# Disciplina: Algoritmos e Programação de Computadores

**Curso:** Computação - Licenciatura — Turma de Repetentes
**Carga horária:** 90 horas-aula (45 min cada)
**Período:** 16/03/2026 a 18/07/2026 (15 semanas letivas+Folga para ajustes)
**Formato:**
- Segunda-feira, 19h–20h30 — Aula teórica (2 horas-aula) - Sala 
- Quarta-feira, 19h–22h — Laboratório prático (4 horas-aula)

**Perfil da turma:** estudantes repetentes com experiência prévia em Python; futuros professores de computação para a educação básica.

---

# 1. Objetivos da turma

A turma tem como objetivo introduzir os estudantes aos **fundamentos da computação e da programação**, desenvolvendo competências em:

- construção de algoritmos
- resolução sistemática de problemas
- implementação de programas em Python
- documentação, versionamento e compartilhamento de código

Por se tratar de um curso voltado a estudantes de **licenciatura em computação**, a turma também busca desenvolver a capacidade de **ensinar conceitos de computação na educação básica**, utilizando ferramentas didáticas como:

- simuladores visuais (OctoStudio / Scratch)
- plataformas de pensamento computacional (Code.org)
- robótica educacional virtual (Tinkercad / Arduino)
- atividades de programação desplugada

Essa abordagem também é útil para a aprendizagem de estudantes de graduação de qualquer curso.
 
---

# 2. Ementa

Princípios fundamentais de construção de programas.
Construção de algoritmos e sua representação em pseudocódigo e linguagens de alto nível.
Noções de abstração.
Especificação de variáveis e funções.
Testes e depuração.
Padrões de soluções em programação.
Noções de programação estruturada.
Identificadores e tipos.
Operadores e expressões.
Estruturas de controle: condicional e repetição.
Entrada e saída de dados.
Estruturas de dados estáticas: agregados homogêneos e heterogêneos.
Iteração e recursão.
Noções de análise de custo e complexidade.
Desenvolvimento sistemático e implementação de programas.
Estruturação, depuração, testes e documentação de programas.
Resolução de problemas.
Aplicações em casos reais e questões ambientais.

---

# 3. Metodologia

A turma adota uma abordagem **construtivista e baseada em projetos**, centrada na construção progressiva de **simuladores computacionais**.

Os conceitos de programação são introduzidos por meio de três ambientes principais:

- **OctoStudio / Scratch** — programação visual no smartphone; construção de simuladores; porta de entrada imediata na primeira aula
- **Code.org** — exercícios estruturados de pensamento computacional; atividades autoguiadas durante o período de ausência do professor
- **Python + VS Code** — linguagem textual de alto nível; ambiente profissional de desenvolvimento

A sequência pedagógica segue o princípio:

> construir antes de definir — compreender conceitos de computação por meio da experiência antes da formalização sintática.

Assim, os estudantes iniciam construindo simuladores no smartphone no primeiro dia de aula, e progressivamente migram para Python, sempre com o conceito visual como âncora.

O **GitHub** funciona como portfólio de aprendizagem ao longo de todo o semestre — cada entrega é um commit, e a página pessoal publicada via GitHub Pages ao final do semestre documenta toda a trajetória.

---

# 4. Ferramentas utilizadas

## Programação visual — OctoStudio / Scratch

Utilizado do início ao fim do semestre para construir simuladores como:

- robô executor de algoritmos (semana 1)
- simulador de CPU e memória (semana 2)
- calculadora interativa (semana 3)
- semáforo inteligente (semana 5)
- contador automático (semana 6)
- banco de dados de escolas / agenda de contatos (semanas 11–12)

Os projetos OctoStudio são compartilhados no **grupo WhatsApp da turma**, criado na primeira aula, que funciona como espaço de circulação de código e feedback entre pares.

## Plataforma de desafios — Code.org

Utilizada nas semanas em que o professor estará em viagem (semanas 4, 5 e 6 — quartas-feiras com monitor), garantindo continuidade com atividades autoguiadas, estruturadas e avaliáveis.

## Linguagem de programação — Python 3 + VS Code

Introduzida na semana 9 como reimplementação textual dos simuladores já construídos visualmente. A transição é suave porque os conceitos já foram vivenciados no OctoStudio.

## Simulador de arquitetura — Little Man Computer (LMC)

Utilizado na semana 2 para visualizar o ciclo fetch-decode-execute, registradores e memória — conectando o simulador Scratch de CPU com o que ocorre fisicamente dentro de um computador.

## Visualização de execução — Python Tutor

Utilizado a partir da semana 9 para tornar visível o que o Python faz internamente: criação de variáveis na memória, pilha de chamadas de funções, percurso de listas.

## Robótica educacional virtual — Tinkercad Circuits

Introduzido na semana 6 com circuitos Arduino simulados. Loops, sensores e estruturas de dados ganham expressão física e visual sem necessidade de hardware.

## Visualizador de algoritmos — VisuAlgo.net

Utilizado na semana 14 para animações de algoritmos de ordenação e busca em português.

## Versionamento — Git + GitHub + GitHub Pages

Introduzido na semana 2 e expandido progressivamente ao longo do semestre. Cada estudante mantém um repositório público como portfólio de aprendizagem, publicando sua página pessoal de programador(a) na semana 15.

---

# 5. Portfólio GitHub

Cada estudante criará e manterá o repositório público `APC-2026-1` com a seguinte estrutura:

```
APC-2026-1/
├── README.md                  ← apresentação pessoal + lista de projetos + reflexões
├── semana02/
│   ├── robo_algoritmos.md     ← descrição do simulador OctoStudio
│   └── fluxograma.png
├── semana03/
│   └── simulador_cpu.md
├── ...
├── semana09/
│   └── calculadora.py         ← primeira reimplementação em Python
├── ...
├── projeto_final/
│   ├── README.md
│   ├── proposta_pedagogica.md
│   └── src/
└── index.html                 ← GitHub Pages (ativado na semana 15)
```

Cada projeto/entrega deve incluir:

- código ou arquivo do simulador (OctoStudio, Python, Tinkercad)
- imagens ou capturas de tela
- documentação descrevendo o algoritmo
- reflexão breve sobre o que foi aprendido

**Critérios de avaliação do portfólio:**

- commits regulares (mínimo 1 por semana) com mensagens descritivas
- README atualizado a cada duas semanas com reflexão sobre o progresso
- código comentado; funções Python com docstrings
- nenhum arquivo `.py` com erro de sintaxe no branch `main`

**Progressão do Git ao longo do semestre:**

| Semana | Habilidade Git introduzida |
|---|---|
| 2 | `init`, `add`, `commit`, `push`, `status`, `log` |
| 4 | `diff`, mensagens semânticas (`feat:`, `fix:`, `docs:`) |
| 9 | `branch`, `checkout` |
| 14 | `pull request`, revisão entre colegas, `merge` |
| 15 | GitHub Pages (`/docs` ou branch `gh-pages`) |

---

# 6. Simuladores desenvolvidos na turma

Durante o semestre os estudantes constroem simuladores progressivamente mais complexos, cobrindo toda a ementa:

| # | Simulador | Semana | Ambiente | Conceito principal |
|---|---|---|---|---|
| 1 | Robô executor de algoritmos | 1 | OctoStudio | algoritmo, sequência, entrada/saída |
| 2 | Simulador de CPU e memória | 2 | OctoStudio + LMC | arquitetura, fetch-decode-execute |
| 3 | Calculadora interativa | 3 | OctoStudio | variáveis, operadores, tipos |
| 4 | Semáforo inteligente | 5 | OctoStudio | condicional, estado |
| 5 | Contador automático | 6 | OctoStudio + Tinkercad | repetição, loop |
| 6 | Simulador de circuito Arduino | 6–8 | Tinkercad | loops, sensores, saída física |
| 7 | Calculadora em Python | 9 | Python | reimplementação textual |
| 8 | Banco de dados simples | 11 | Python | listas, busca |
| 9 | Agenda de contatos | 12 | Python | dicionários, JSON |
| 10 | Analisador de desempenho escolar (SAEB) | 14–15 | Python | recursão, complexidade, dados reais |

---

# 7. Avaliação

A avaliação é contínua e baseada em atividades práticas e reflexivas.

| Atividade | Peso |
|---|---|
| Portfólio GitHub (commits semanais + README) | 30% |
| Desafios Code.org (semanas 4, 5 e 6) | 20% |
| Exercícios e simuladores semanais | 20% |
| Projeto final | 20% |
| Participação e atividades em laboratório | 10% |

## Rubrica dos desafios Code.org

Cada semana de desafios vale 10 pontos:

| Critério | Pontos |
|---|---|
| Conclusão dos desafios propostos | 4 |
| Explicação do algoritmo em linguagem natural | 3 |
| Identificação e correção de erros | 2 |
| Reflexão sobre a própria aprendizagem | 1 |

---

# 8. Projeto final

Os estudantes desenvolvem, individualmente ou em duplas, um **recurso educacional computacional** que poderá ser:

- simulador educacional (OctoStudio ou Python)
- jogo didático para a educação básica
- aplicação em Python com microdados reais (SAEB/INEP)
- analisador de desempenho escolar com visualização de resultados
- robô virtual com Arduino simulado no Tinkercad

O projeto deve incluir obrigatoriamente:

- descrição do problema e do algoritmo
- implementação funcional com código comentado
- documentação no README
- **proposta pedagógica:** como usar este recurso em uma aula da educação básica, para qual faixa etária, quais competências da BNCC-Computação desenvolve

---

# 9. Cronograma de aulas

> **Legenda:**
> ⚠️ Professor em viagem (08–26/abr) — quartas com monitor; segundas com estudo dirigido ou Code.org
> 🎯 Destaque pedagógico da semana
> 📱 Atividade no smartphone (OctoStudio)
> 💻 Laboratório com computadores desktop
> 🤖 Robótica virtual (Tinkercad)

---

## Semana 1 — 16/mar (Seg) e 18/mar (Qua)

**Tema:** Introdução à computação, algoritmos e primeira experiência com programação

🎯 *A aula começa pelo fazer. Cada estudante sai hoje com um programa funcionando, compartilhado com a turma. Conceitos formais são ancorados nessa experiência.*

### Segunda-feira — Aula teórica/prática

**Parte 1 — Contrato pedagógico (30 min)**
- Apresentação da turma, ementa e avaliação
- O que muda para quem já reprovou: autonomia, portfólio, protagonismo
- Criação do **grupo WhatsApp da turma** — canal permanente de compartilhamento de projetos

**Parte 2 — 📱 OctoStudio: programar antes de definir (60 min)**
- Instalar OctoStudio no smartphone (iOS/Android, gratuito, MIT Media Lab)
- 10 minutos de exploração livre: "mexa e veja o que acontece"
- Demonstração guiada: sprite, bloco `perguntar`, variável `resposta`, `se... então... senão`
- **Desafio — programa de apresentação pessoal:**
  - pergunta o nome de quem usa
  - usa pelo menos uma condicional
  - apresenta algo diferente conforme a resposta (saudação personalizada, diagnóstico criativo, "tipo de programador", qualquer coisa que represente o(a) autor(a))
- Compartilhar no grupo WhatsApp — cada estudante roda o programa de 2 colegas
- Fechamento: "o que você fez tem nome — é um **algoritmo com entrada de dados e estrutura condicional**"

### Quarta-feira — 💻 Laboratório

1. Roda de apresentações: cada estudante demonstra seu programa OctoStudio (2–3 min, grupos de 5)
2. **O que é um computador?** — CPU, memória, E/S, modelo de Von Neumann
3. Simulador LMC (Little Man Computer): ciclo fetch-decode-execute, registradores, memória
4. Da abstração Scratch para o texto: reescrever o programa OctoStudio em **pseudocódigo** coletivamente no quadro
5. Comparação lado a lado: bloco Scratch ↔ pseudocódigo ↔ código Python
6. Python + VS Code: instalar, configurar, executar `print("Olá, mundo!")`
7. **Para a semana 2:** trazer ideia de simulador de CPU em OctoStudio

**Recursos:** OctoStudio, WhatsApp, [LMC online](https://peterhigginson.co.uk/LMC/), Python 3, VS Code

---

## Semana 2 — 23/mar (Seg) e 25/mar (Qua)

**Tema:** Arquitetura de computadores e algoritmos

### Segunda-feira — Aula teórica

- O que é um algoritmo? Propriedades: finitude, determinismo, entrada/saída
- Formalizar a semana 1: o programa OctoStudio *era* um algoritmo
- Representações: linguagem natural → pseudocódigo → fluxograma → código
- Abstração: o que o OctoStudio esconde que o Python vai expor?
- **Git:** motivação — o problema do `trabalho_v3_final_definitivo2.py`; o que é versionamento

### Quarta-feira — 💻 Laboratório

1. 📱 OctoStudio: **simulador de CPU** — sprite representa a CPU, variáveis representam registradores, blocos executam instruções; compartilhar no WhatsApp
2. LMC: executar um programa simples e acompanhar registradores e memória passo a passo
3. Criar conta no GitHub; configurar perfil público
4. `git init`, `git add`, `git commit`, `git push` — repositório `algoritmos-lc-2026`
5. Criar `README.md` com apresentação pessoal e link/print do simulador OctoStudio da semana 1
6. **Commit 1:** pasta `semana02/` com documentação do simulador de CPU

**Recursos:** OctoStudio, LMC, GitHub, Git

---

## Semana 3 — 30/mar (Seg) e 01/abr (Qua)

**Tema:** Variáveis, tipos de dados e operadores

### Segunda-feira — Aula teórica

- Variáveis: conceito, declaração, atribuição, tipagem dinâmica em Python
- Tipos primitivos: `int`, `float`, `str`, `bool` — representação e limites
- Operadores aritméticos, relacionais, lógicos e de atribuição composta
- Precedência de operadores e expressões compostas
- Conversão de tipos: `int()`, `float()`, `str()`, `bool()`

### Quarta-feira — 💻 Laboratório

1. 📱 OctoStudio: **simulador de calculadora interativa** — operações com variáveis visíveis na tela; compartilhar no WhatsApp
2. Python Tutor: observar variáveis na memória passo a passo
3. Python: calculadora com `input()`, operações, `print()` com f-strings
4. Depuração dirigida: encontrar e corrigir `TypeError`, `NameError`, `ValueError`
5. **Commit 2:** pasta `semana03/` com simulador OctoStudio documentado + versão Python

**Recursos:** OctoStudio, [Python Tutor](https://pythontutor.com), Python 3

---

## Semana 4 — 06/abr (Seg) e 08/abr (Qua)

**Tema:** Algoritmos e decomposição de problemas

> ⚠️ **Quarta 08/abr:** professor em viagem a partir desta data. **Monitor no laboratório.**

### Segunda-feira — Aula teórica

- Entrada e saída de dados: `input()`, `print()`, f-strings, formatação numérica
- Expressões booleanas compostas; curto-circuito com `and`, `or`, `not`
- Boas práticas: nomes descritivos, comentários, código legível
- Git para o dia a dia: `git diff`, `git log`, `git status`, mensagens semânticas (`feat:`, `fix:`, `docs:`)
- Apresentação do Code.org: como usar, onde entregar, o que é esperado

### Quarta-feira — 💻 Laboratório com monitor

1. **Code.org:** módulo "Algoritmos e Sequências" — desafios estruturados de decomposição
2. Exercícios Python de E/S: IMC, conversão de temperatura, cálculo de troco
3. 📱 OctoStudio: "quiz de 3 perguntas com placar" — variáveis acumuladoras e condicionais; compartilhar no WhatsApp
4. Rubrica dos desafios: monitor orienta preenchimento do relatório reflexivo
5. **Commit 3:** pasta `semana04/` + relatório Code.org em Markdown

**Recursos:** [Code.org](https://code.org), OctoStudio, Python 3, WhatsApp

---

## Semana 5 — 13/abr (Seg) e 15/abr (Qua)

**Tema:** Estrutura condicional

> ⚠️ **Professor em viagem. Segunda: estudo dirigido. Quarta: monitor no laboratório.**

### Segunda-feira — Estudo Dirigido

*Entregue pelo professor via repositório ou impresso:*

1. Trace manual: qual a saída para cada entrada? (3 variações com `if/elif/else`)
2. Escreva em pseudocódigo um algoritmo para classificar triângulos (equilátero, isósceles, escaleno, inválido)
3. Traduza para Python, teste no Python Tutor, cole o link gerado na entrega
4. Encontre os 3 bugs em `classifica_nota.py` (fornecido junto com o estudo)
5. Reflexão docente: como você ensinaria condicionais para alunos do 6º ano sem computador? Descreva uma atividade de 10 minutos

*Entrega:* pull request no repositório até quinta 16/abr, pasta `semana05/estudo_dirigido/`

### Quarta-feira — 💻 Laboratório com monitor

1. **Code.org:** módulo "Condicionais e Decisões" — desafios com estruturas de seleção
2. Monitor discute dúvidas do estudo dirigido em grupo
3. 📱 OctoStudio: **semáforo inteligente** — botão alterna estados com condicional; compartilhar no WhatsApp
4. Python Tutor: traçar execução de condicionais aninhadas
5. **Commit 4:** pull request com estudo dirigido + relatório Code.org

**Recursos:** Code.org, estudo dirigido (PDF), Python Tutor, OctoStudio

---

## Semana 6 — 20/abr (Seg) e 22/abr (Qua)

**Tema:** Repetição e padrões algorítmicos

> ⚠️ **Professor em viagem. Segunda: estudo dirigido. Quarta: monitor no laboratório.**

### Segunda-feira — Estudo Dirigido

*Entregue pelo professor:*

1. Analise os pseudocódigos fornecidos: qual usa `while`? Qual usa `for`? Justifique
2. Trace manual de um `while` com acumulador: o que o programa imprime? (3 variações)
3. Escreva em Python a tabuada do 7 com `for` e `range()`
4. Corrija o loop infinito em `soma_notas.py` (fornecido)
5. Pesquisa (1 página): o que é "pensamento computacional"? Como laços de repetição aparecem no cotidiano?

*Entrega:* pull request no repositório até quinta 23/abr, pasta `semana06/estudo_dirigido/`

### Quarta-feira — 💻🤖 Laboratório com monitor

1. **Code.org:** módulo "Loops e Otimização" — desafios com repetição e padrões
2. Monitor introduz `while` e `for` com exemplos simples no projetor
3. 📱 OctoStudio: **contador automático animado** — bloco `repita` com visualização; compartilhar no WhatsApp
4. 🤖 **Tinkercad Circuits:** LED piscando com `while True` — robótica virtual como analogia corporal a loops
5. **Commit 5:** pull request com estudo dirigido + relatório Code.org + print do circuito Tinkercad

**Recursos:** Code.org, estudo dirigido (PDF), OctoStudio, [Tinkercad](https://tinkercad.com)

---

## Semana 7 — 27/abr (Seg) e 29/abr (Qua)

**Tema:** Abstração e modularização

### Segunda-feira — Aula teórica

- Retomada: correção coletiva dos estudos dirigidos e desafios Code.org
- `while`, `for`, `range()`, `break`, `continue`, `else` em laços
- Padrões de solução: contagem, acumulação, busca, validação de entrada
- Abstração: o que modularizar significa — do bloco Scratch ao módulo Python
- Discussão pedagógica: como os estudantes planejam ensinar loops? Troca de ideias

### Quarta-feira — 💻 Laboratório

1. Refatoração: pegar simuladores Scratch das semanas anteriores e reorganizá-los em **blocos reutilizáveis**
2. Comparação: bloco customizado OctoStudio ↔ função Python
3. Problemas clássicos com loops: fatorial, números primos, Fibonacci
4. 🤖 Tinkercad: varredura de LEDs com array e loop
5. **Commit 6:** pasta `semana07/` com simuladores refatorados documentados + reflexão sobre abstração

**Recursos:** OctoStudio, Python 3, Tinkercad

---

## Semana 8 — 04/mai (Seg) e 06/mai (Qua)

**Tema:** Funções e biblioteca de blocos reutilizáveis

### Segunda-feira — Aula teórica

- Funções: motivação — DRY (*Don't Repeat Yourself*)
- `def`, parâmetros posicionais e nomeados, `return`
- Escopo: variáveis locais e globais
- Docstrings: documentar funções como padrão profissional
- A ponte já construída: bloco customizado com parâmetro em Scratch = `def f(x):` em Python

### Quarta-feira — 💻 Laboratório

1. Python Tutor: pilha de chamadas (`call stack`) — quadros de função na memória
2. 📱 OctoStudio: **biblioteca de blocos** — criar conjunto de blocos reutilizáveis para os simuladores anteriores; compartilhar no WhatsApp
3. Python: construir `lib_matematica.py` com funções de média, mdc, mmc, primalidade — todas com docstrings
4. 🤖 Tinkercad: encapsular leitura de sensor em função `medir()` reutilizável
5. **Commit 7:** pasta `semana08/` com `lib_matematica.py` documentada + projeto OctoStudio

**Recursos:** Python Tutor, OctoStudio, Python 3, Tinkercad

---

## Semana 9 — 11/mai (Seg) e 13/mai (Qua)

**Tema:** Introdução ao Python — reimplementando os simuladores

🎯 *Transição suave: os conceitos já foram vivenciados no OctoStudio. Agora os estudantes os reescrevem em Python.*

### Segunda-feira — Aula teórica

- Sintaxe Python em comparação com Scratch: o mesmo algoritmo em dois idiomas
- Tipos de dados, operadores, estruturas de controle — revisão com a notação Python
- Depuração com `pdb` e breakpoints no VS Code
- Desenvolvimento sistemático: análise → projeto → codificação → teste → refatoração

### Quarta-feira — 💻 Laboratório

1. **Reimplementação:** calculadora interativa (semana 3) em Python — com funções, `input()`, `while` para repetição
2. Python Tutor: comparar execução Python com o que o OctoStudio fazia visualmente
3. Doctest: escrever testes para cada função da calculadora
4. Pair programming: uma pessoa escreve o teste, a outra escreve a função
5. **Commit 8:** pasta `semana09/` com `calculadora.py` — primeira reimplementação textual completa, com testes

**Recursos:** Python Tutor, Python 3 (`doctest`), VS Code

---

## Semana 10 — 18/mai (Seg) e 20/mai (Qua)

**Tema:** Programação estruturada — condicionais e loops em Python

### Segunda-feira — Aula teórica

- Revisão das estruturas de controle em Python: `if/elif/else`, `while`, `for`, `range()`
- Laços aninhados: matrizes, padrões, tabuada completa
- Padrões de solução revisitados com código Python
- Análise de custo intuitiva: contar operações, comparar soluções

### Quarta-feira — 💻 Laboratório

1. Python Tutor: visualizar laço aninhado — dois contadores simultâneos na memória
2. Exercícios: tabuada completa, triângulo de asteriscos, matriz identidade
3. **Reimplementação:** semáforo inteligente (semana 5) e contador automático (semana 6) em Python
4. 🤖 Tinkercad: matriz 3×3 de LEDs controlada por laços aninhados
5. **Commit 9:** pasta `semana10/` com reimplementações dos simuladores + análise comparativa Scratch vs Python

**Recursos:** Python Tutor, Python 3, Tinkercad

---

## Semana 11 — 25/mai (Seg) e 27/mai (Qua)

**Tema:** Estruturas de dados — listas e banco de dados simples

### Segunda-feira — Aula teórica

- Listas em Python: criação, indexação, fatiamento, mutabilidade
- Operações: `append`, `insert`, `remove`, `sort`, `len`, `in`
- Percurso: `for`, `enumerate`, `zip`
- Algoritmos de busca: linear O(n) e binária O(log n)
- Aplicação com dados reais: microdados do SAEB (INEP) — proficiência em Matemática e Língua Portuguesa por escola e UF

### Quarta-feira — 💻 Laboratório

1. Python Tutor: visualizar lista na memória — objeto, referência, mutabilidade
2. Estatísticas de notas: média, maior, menor, desvio padrão — sem bibliotecas externas
3. **Simulador 8 — banco de dados simples:** lista de registros com busca e filtragem
4. Aplicação com dados reais: carregar CSV de microdados do SAEB, filtrar por UF, calcular média de proficiência por escola e comparar com listas
5. **Commit 10:** pasta `semana11/` com simulador de banco de dados + análise de desempenho escolar com dados reais

**Recursos:** Python Tutor, Python 3, matplotlib, [Microdados SAEB — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb)

---

## Semana 12 — 01/jun (Seg) e 03/jun (Qua)

**Tema:** Estruturas de dados heterogêneas — agenda de contatos

### Segunda-feira — Aula teórica

- Dicionários Python: chave-valor, hashing intuitivo, operações CRUD
- Tuplas: imutabilidade e uso como registros/structs
- JSON: leitura e escrita — dados como ponte entre programas
- Comparação com estruturas de dados de outras linguagens

### Quarta-feira — 💻 Laboratório

1. 📱 OctoStudio: banco de personagens como analogia visual a dicionários; compartilhar no WhatsApp
2. **Simulador 9 — agenda de contatos:** dicionários aninhados, busca por nome, exportação em JSON
3. Microdados SAEB em formato JSON: ler e consultar registros de escolas por município com Python
4. Aplicação com dados reais: construir dicionário de escolas do DF com atributos de rede, localização e proficiência média — consultável por código INEP
5. **Commit 11:** pasta `semana12/` com agenda de contatos + catálogo de escolas do DF documentado

**Recursos:** Python (`json`), [Microdados SAEB — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb), OctoStudio, Python 3

---

## Semana 13 — 08/jun (Seg) e 10/jun (Qua)

**Tema:** Testes, depuração e desenvolvimento sistemático

### Segunda-feira — **Prova teórica**

- Conteúdo: pseudocódigo, análise de algoritmos, estruturas de controle, funções, estruturas de dados
- Formato: trace manual, escrita de algoritmos em pseudocódigo e Python, análise de custo intuitiva
- Sem consulta a código; rascunho em papel permitido

### Quarta-feira — 💻 Laboratório

1. Ciclo completo de desenvolvimento: análise → projeto → codificação → teste → refatoração
2. Prática de depuração: encontrar e corrigir bugs em 5 programas problemáticos fornecidos
3. Escrever doctests para as funções da `lib_matematica.py` (semana 8)
4. 🤖 Tinkercad: sensor ultrassônico + Arduino — função `medir()` com teste automatizado
5. **Commit 12:** `lib_matematica.py` com doctests completos + relatório de erros encontrados

**Recursos:** Python (`doctest`, `pdb`), VS Code debugger, Tinkercad

---

## Semana 14 — 15/jun (Seg) e 17/jun (Qua)

**Tema:** Recursão, complexidade e análise de desempenho escolar com dados do SAEB

### Segunda-feira — Aula teórica

- Recursão: caso base, caso recursivo — a estrutura essencial
- Iteração vs recursão: legibilidade, memória, risco de estouro de pilha
- Análise de complexidade: O(n), O(n²), O(log n) — com gráficos
- Algoritmos de ordenação: Bubble Sort, Selection Sort — passo a passo
- Como ensinar recursão e ordenação? Cartas de baralho, dança, VisuAlgo

### Quarta-feira — 💻 Laboratório

1. Python Tutor: rastrear fatorial recursivo — pilha crescendo e desempilhando
2. [VisuAlgo.net](https://visualgo.net/pt): animações de Bubble Sort, Selection Sort, busca binária
3. Implementar Bubble Sort; medir tempo para N = 100, 1000, 10000 com `time`
4. Gerar gráfico comparativo com `matplotlib`: implementação própria vs `list.sort()`
5. **Simulador 10 — analisador de desempenho escolar (SAEB):** carregar microdados reais, ordenar escolas por proficiência, calcular rankings por município e rede; usar recursão para sumarização hierárquica
6. **Commit 13:** pasta `semana14/` com analisador SAEB + gráfico de complexidade

**Recursos:** Python Tutor, VisuAlgo.net, matplotlib, Python 3, [Microdados SAEB — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb)

---

## Semana 15 — 22/jun (Seg) e 24/jun (Qua)

**Tema:** Projeto final, robótica educacional e GitHub Pages

### Segunda-feira — Apresentações dos projetos finais

- Cada dupla/individual apresenta seu recurso educacional (10 min + 5 de perguntas)
- Formato: demonstração ao vivo + repositório GitHub aberto + proposta pedagógica
- Avaliação por pares com rubrica fornecida

### Quarta-feira — 💻🤖 Laboratório — GitHub Pages + Robótica

1. 🤖 **Tinkercad:** projeto integrador de robótica — simulador ambiental com múltiplos sensores, lógica de alerta e log de dados
2. Configurar GitHub Pages no repositório de cada estudante
3. Criar `index.html` com página pessoal de programador(a): apresentação, projetos OctoStudio, projetos Python, reflexão sobre o semestre
4. Peer review: cada estudante abre uma *issue* no repositório de um colega com elogio e sugestão
5. **Commit final:** GitHub Pages publicado — URL registrada no formulário da turma

**Recursos:** Tinkercad, GitHub Pages, HTML/Jekyll

---

> **Semanas 16–18 (29/jun–18/jul):** período de exames — prova final, recuperação e lançamento de menções, conforme calendário acadêmico da UnB.

---

# 10. Resultados esperados

Ao final da turma os estudantes deverão ser capazes de:

- construir algoritmos e representá-los em pseudocódigo, fluxograma e Python
- implementar programas com variáveis, funções, estruturas de controle e estruturas de dados
- depurar e testar código de forma sistemática
- versionar código com Git e manter portfólio público no GitHub
- desenvolver simuladores educacionais em OctoStudio e Python
- propor e executar atividades de ensino de computação para a educação básica

---

# 11. Observações pedagógicas

A turma é estruturada em torno de dois eixos simultâneos:

**Eixo técnico:** progressão de OctoStudio → Python, do algoritmo visual ao textual, do simulador simples ao projeto complexo com dados reais de desempenho escolar (microdados SAEB/INEP).

**Eixo pedagógico:** a cada simulador construído, os estudantes são convidados a pensar como o usariam em uma sala de aula da educação básica — qual faixa etária, qual conceito, qual atividade. O projeto final sintetiza os dois eixos na forma de um recurso educacional completo.

A abordagem prioriza:

- **aprendizagem ativa** — construir antes de receber explicação
- **resolução de problemas** — todo conceito é introduzido via problema real
- **reflexão sobre o ensinar** — competência técnica e competência pedagógica desenvolvidas em paralelo
- **portfólio como evidência** — o GitHub documenta a trajetória completa, não apenas o produto final

O grupo WhatsApp da turma, criado na primeira aula, funciona como espaço de circulação imediata dos projetos OctoStudio — criando uma cultura de compartilhamento de código que antecipa o espírito do GitHub.

---

# 12. Referências

## Livros e artigos

- **Downey, Allen B.** — *Pense em Python* — [penseallen.com.br](https://penseallen.com.br) (tradução livre gratuita)
- **Cormen et al.** — *Introdução a Algoritmos* — Caps. 1–3 (análise de complexidade)
- **Wing, Jeannette** — "Computational Thinking", CACM, 2006 — leitura obrigatória para a formação docente
- **BNCC — Computação** (CBIE/SBC, 2019) — referência curricular nacional

## Ferramentas e plataformas

- [OctoStudio](https://octostudio.org) — Scratch no smartphone (MIT Media Lab)
- [Code.org](https://code.org) — pensamento computacional estruturado
- [Python Tutor](https://pythontutor.com) — visualização de execução de código
- [VisuAlgo](https://visualgo.net/pt) — algoritmos animados em português
- [CS Unplugged](https://csunplugged.org/pt) — computação sem computador para a escola
- [Tinkercad Circuits](https://tinkercad.com) — simulador Arduino gratuito
- [Little Man Computer](https://peterhigginson.co.uk/LMC/) — simulador de arquitetura
- [Microdados SAEB — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/saeb) — proficiência escolar por escola, município e UF

---

*Plano elaborado para o semestre 2026/1 | Última atualização: 16/03/2026*
*Sujeito a ajustes pedagógicos conforme andamento da turma.*
