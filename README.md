# APCUnB2026.1

Repositório público da turma 07 da disciplina Algoritmos e Programação de Computadores da UnB no semestre 2026.1, sob responsabilidade do Prof. Jorge Henrique Cabral Fernandes (jhcf@unb.br).

---

# Disciplina: Algoritmos e Programação de Computadores

**Curso:** Computação — Licenciatura — Turma de Repetentes
**Carga horária:** 90 horas-aula (45 min cada)
**Período:** 16/03/2026 a 18/07/2026 (15 semanas letivas + período de exames)
**Formato:**
- Segunda-feira, 19h–20h30 — Aula teórica (2 horas-aula)
- Quarta-feira, 19h–22h — Laboratório prático (4 horas-aula)

**Perfil da turma:** estudantes repetentes com experiência prévia em Python; futuros professores de computação para a educação básica.

**Apoio:** os estudantes podem obter apoio de monitorias ao longo do semestre — consulte o Moodle da disciplina para horários e canais de atendimento.

---

# 1. Objetivos

A disciplina tem como objetivo introduzir os estudantes aos **fundamentos da computação e da programação**, desenvolvendo competências em:

- construção de algoritmos e sua representação em múltiplas linguagens
- resolução sistemática de problemas computacionais
- implementação de programas com interface gráfica
- documentação, versionamento e compartilhamento de código

Por se tratar de um curso de **licenciatura em computação**, a disciplina também busca desenvolver a capacidade de **ensinar conceitos de computação na educação básica**, utilizando ferramentas didáticas como simuladores, programação visual e atividades de pensamento computacional.

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

# 3. Linguagens utilizadas no semestre

A disciplina trabalha com **quatro linguagens**, em progressão pedagógica — cada uma ilumina um aspecto diferente da computação:

| Ordem | Linguagem | Ferramenta | Papel pedagógico |
|---|---|---|---|
| 1 | **Linguagem de máquina** | Little Man Computer (LMC) | Compreender o que o computador faz por baixo: registradores, memória, ciclo fetch-decode-execute |
| 2 | **JavaScript** | Code.org Game Lab | Programação estruturada em linguagem textual real, dentro de um ambiente visual motivador (jogos) |
| 3 | **C** | VS Code + gcc | Aprofundar tipos, operadores binários, organização de memória e ponteiros — o que Python esconde |
| 4 | **Python** | VS Code + tkinter + pandas | Linguagem principal do trabalho final; interface gráfica, análise de dados reais (PDAD 2024) |

> **Nota sobre robótica e Arduino:** Tinkercad e Arduino não foram utilizados neste semestre. A progressão de linguagens acima é o que efetivamente foi trabalhado em sala.

> **Nota sobre OctoStudio:** utilizado nas primeiras semanas como porta de entrada à programação visual, mas não como ferramenta central ao longo de todo o semestre.

---

# 4. Metodologia

A disciplina adota uma abordagem **construtivista e baseada em projetos**, com a seguinte sequência pedagógica:

> compreender conceitos de computação antes da sintaxe — e aprender cada linguagem como uma nova lente sobre os mesmos conceitos fundamentais.

Os estudantes partem do nível de máquina (LMC), sobem para JavaScript (Code.org), aprofundam com C os detalhes que linguagens de alto nível escondem, e chegam ao Python com uma compreensão sólida do que acontece por baixo dos panos.

O **GitHub** funciona como portfólio de aprendizagem ao longo de todo o semestre. O **Moodle** apoia a avaliação, comunicação e entrega de atividades. O grupo **WhatsApp da turma** serve como canal informal de compartilhamento de projetos e dúvidas rápidas.

---

# 5. Repositório individual — GitHub

## Compartilhamento obrigatório na primeira semana

**Na primeira semana de aula, cada estudante deve criar seu repositório e compartilhar a URL com o professor via Moodle.** O professor e os monitores acompanharão a evolução semanal dos repositórios como parte da avaliação contínua.

## O que o repositório deve conter

O repositório não é apenas um portfólio de READMEs — ele deve conter os **códigos completos de todos os exercícios realizados em laboratório**. Um repositório com apenas arquivos de documentação sem código-fonte não será considerado para avaliação.

### Estrutura esperada

```
APC-2026-1/
├── README.md                        ← apresentação pessoal + reflexão de progresso
├── semana01/
│   └── programa_apresentacao/       ← projeto OctoStudio documentado + print/link
├── semana02/
│   ├── lmc_contagem.txt             ← programa LMC com comentários
│   └── README.md
├── semana03/
│   └── calculadora_octostudio/      ← projeto OctoStudio
├── semana04/                        ← Code.org lições 1–5
│   ├── progresso.png                ← print da plataforma
│   └── README.md                    ← link do projeto Game Lab
├── semana05/                        ← Code.org lições 6–12
│   ├── progresso.png
│   └── README.md
├── semana06/                        ← Code.org lições 13–18
│   ├── progresso.png
│   └── README.md                    ← link do jogo finalizado
├── semana07/
│   └── jogo_para_python.py          ← lógica do jogo reimplementada em Python
├── semana08/
│   ├── exercicios_c/
│   │   ├── ex1_printf.c
│   │   ├── ex2_sizeof.c
│   │   ├── ex3_variaveis.c
│   │   └── ...                      ← todos os .c dos exercícios de laboratório
│   └── README.md
├── semana09/
│   ├── exercicios_c/
│   │   └── ...                      ← continuação dos exercícios C
│   └── README.md
├── semana10/
│   ├── exercicios_python/
│   │   └── ...                      ← exercícios com pandas e PDAD
│   └── README.md
├── semana11/
│   └── analise_pdad/
│       └── ...                      ← scripts de análise com dados reais
├── semana12/
│   └── ...
├── projeto_final/
│   ├── README.md                    ← descrição, como executar, dependências
│   ├── requirements.txt             ← pandas matplotlib openpyxl
│   └── src/
│       └── sistema.py               ← aplicação tkinter principal
└── index.html                       ← GitHub Pages (opcional)
```

## Critérios de avaliação do portfólio

- **Commits regulares:** mínimo 1 commit por semana com mensagem descritiva
- **Código completo:** todos os exercícios de laboratório devem estar no repositório como arquivos executáveis (`.py`, `.c`, `.txt`), não apenas descritos no README
- **README atualizado:** reflexão breve sobre o progresso a cada duas semanas
- **Código comentado:** funções Python com docstrings; exercícios C com comentários explicativos
- **Nenhum arquivo com erro de sintaxe** no branch `main`

## Acompanhamento semanal

O professor e os monitores analisarão os repositórios semanalmente. Estudantes sem commits na semana serão contatados. A evolução do repositório é evidência de aprendizagem — commits de última hora concentrados no final do semestre não substituem o processo contínuo.

---

# 6. Ferramentas utilizadas

## Little Man Computer (LMC)

Simulador de computador de linguagem de máquina com acumulador, contador de programa, memória de dados e instruções. Usado para visualizar concretamente o que acontece dentro do processador antes de qualquer linguagem de alto nível.

- [LMC online](https://peterhigginson.co.uk/LMC/)

## Code.org Game Lab

Módulo "Introdução ao Laboratório de Jogos" — 18 lições de programação em **JavaScript** dentro de um ambiente de criação de jogos. Usado nas semanas 4–6 no ritmo de cada estudante, com acompanhamento de monitor.

- [Code.org](https://code.org)

## Linguagem C

Utilizada para aprofundar conceitos que linguagens de alto nível escondem: tipos primitivos e seus tamanhos em memória, operadores aritméticos e binários, ponteiros, structs, alocação dinâmica. Não é a linguagem final do semestre — é uma linguagem de transição que torna o Python mais compreensível.

- Compilador: `gcc` (Linux) ou equivalente
- Editor: VS Code

## Python 3

Linguagem principal do trabalho final. Usada com:

- `tkinter` — interface gráfica (janelas, widgets, eventos, gráficos embutidos)
- `pandas` — leitura e análise de microdados reais
- `matplotlib` — visualização de dados dentro das janelas tkinter

## Python Tutor

Ferramenta de visualização de execução de código — mostra variáveis na memória, pilha de chamadas e percurso de listas passo a passo.

- [pythontutor.com](https://pythontutor.com)

## Git + GitHub

Introduzidos na semana 2. O repositório GitHub de cada estudante é o portfólio da disciplina e é avaliado semanalmente.

## Moodle

Plataforma institucional da UnB utilizada para:
- entrega de atividades avaliativas
- comunicação oficial
- registro de notas e menções
- acompanhamento do progresso dos estudantes

Acesse pelo portal da UnB com seu login institucional.

## VisuAlgo

Animações interativas de algoritmos de busca e ordenação em português.

- [visualgo.net/pt](https://visualgo.net/pt)

---

# 7. Dados utilizados — PDAD 2024

Os exercícios de programação com dados reais utilizam os **microdados do PDAD 2024** (Pesquisa Distrital por Amostra de Domicílios Ampliada), produzidos pelo IPEDF — Instituto de Pesquisa e Estatística do Distrito Federal.

**Download:** [pdad.ipe.df.gov.br](https://pdad.ipe.df.gov.br)

**Arquivos utilizados:**
- `PDAD_2024-Moradores.csv` — um registro por morador (~25 000 registros)
- `PDAD_2024-Domicilios.xlsx` — um registro por domicílio
- `Dicionario_de_variaveis_PDAD_2024.xlsx` — descrição de cada coluna

**Atenção:** filtre sempre os valores sentinela `99999` (não se aplica) e `88888` (não declarado) antes de qualquer cálculo numérico.

---

# 8. Avaliação

| Atividade | Peso |
|---|---|
| Portfólio GitHub — acompanhamento semanal | 30% |
| Desafios Code.org Game Lab (semanas 4, 5 e 6) | 20% |
| Exercícios de laboratório (C e Python, semanas 7–12) | 20% |
| Projeto final (Python + tkinter + PDAD) | 20% |
| Participação e frequência em laboratório | 10% |

## Rubrica Code.org Game Lab

| Critério | Pontos |
|---|---|
| Avaliações concluídas (todos os itens "Avaliação" das lições) | 5 |
| Print de progresso publicado no repositório GitHub | 2 |
| Projeto/jogo da semana funcionando com link compartilhado | 3 |

Cada semana de Code.org vale 10 pontos. Os itens "Desafios" ao final de cada lição são opcionais.

---

# 9. Projeto final

O trabalho final é desenvolvido **em dupla** e consiste num **sistema Python com interface gráfica tkinter** para explorar interativamente os microdados do PDAD 2024.

**Entrega:**
- repositório GitHub com código completo, `README.md` e `requirements.txt`
- apresentação ao vivo de 10 minutos com demonstração do sistema funcionando

Consulte o arquivo [`TRABALHO_FINAL.md`](TRABALHO_FINAL.md) neste repositório para o enunciado completo com recortes temáticos disponíveis, requisitos mínimos e critérios de avaliação detalhados.

---

# 10. Cronograma resumido

| Semana | Datas | Conteúdo | Linguagem |
|---|---|---|---|
| 1 | 16–18/mar | Apresentação, OctoStudio, LMC, Git | OctoStudio + LMC |
| 2 | 23–25/mar | Algoritmos, pseudocódigo, arquitetura, GitHub | LMC + Git |
| 3 | 30/mar–01/abr | Variáveis, tipos, operadores, OctoStudio | OctoStudio + Python |
| 4 | 06–08/abr | Code.org lições 1–5 (fundamentos visuais) ⚠️ monitor | JavaScript |
| 5 | 13–15/abr | Code.org lições 6–12 (interatividade) ⚠️ monitor | JavaScript |
| 6 | 20–22/abr | Code.org lições 13–18 (jogo completo) ⚠️ monitor | JavaScript |
| 7 | 27–29/abr | Retomada: do jogo (JS) para Python | Python |
| 8 | 04–06/mai | Linguagem C: estrutura, tipos, operadores, E/S | C |
| 9 | 11–13/mai | C: estruturas de controle, funções, arrays, strings | C |
| 10 | 18–20/mai | C: ponteiros, structs, alocação dinâmica | C |
| 11 | 25–27/mai | Python: listas, pandas, microdados PDAD | Python |
| 12 | 01–03/jun | Python: dicionários, pandas, análise PDAD | Python |
| 13 | 08–10/jun | Prova teórica (Seg) + laboratório Python (Qua) | Python |
| 14 | 15–17/jun | Ordenação, complexidade, algoritmos com PDAD | Python |
| 15 | 22–24/jun | Tkinter, interface gráfica, projeto final | Python |
| 16 | 06–08/jul | Apresentações dos projetos finais | Python |
| 17–18 | 13–18/jul | Período de exames e menções | — |

> ⚠️ Semanas 4–6: professor em viagem; laboratórios conduzidos com apoio de monitores.

---

# 11. Resultados esperados

Ao final da disciplina os estudantes deverão ser capazes de:

- descrever o funcionamento básico de um computador a partir do modelo LMC
- programar em JavaScript, C e Python, identificando as diferenças e semelhanças entre as três
- explicar o que acontece na memória quando uma variável é declarada em C vs Python
- implementar algoritmos de busca e ordenação e analisar sua complexidade
- construir uma aplicação com interface gráfica em Python usando tkinter
- carregar, filtrar e analisar microdados reais com pandas
- manter um portfólio de código público no GitHub com histórico de commits
- propor uma atividade de ensino de computação para a educação básica

---

# 12. Referências

## Livros e materiais

- **Downey, Allen B.** — *Pense em Python* — [penseallen.com.br](https://penseallen.com.br) (tradução livre gratuita)
- **Cormen et al.** — *Introdução a Algoritmos* — Caps. 1–3 (análise de complexidade)
- **Wing, Jeannette** — "Computational Thinking", CACM, 2006

## Plataformas e ferramentas

- [Little Man Computer](https://peterhigginson.co.uk/LMC/) — simulador de linguagem de máquina
- [Code.org Game Lab](https://code.org) — JavaScript no contexto de jogos
- [Python Tutor](https://pythontutor.com) — visualização de execução de código
- [VisuAlgo](https://visualgo.net/pt) — algoritmos animados em português
- [PDAD 2024 — IPEDF](https://pdad.ipe.df.gov.br) — microdados do DF

---

*APCUnB2026.1 — Última atualização: julho/2026*
