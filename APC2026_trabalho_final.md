# Trabalho Final — APC 2026/1
## Sistema de Exploração dos Microdados PDAD 2024 com Interface Gráfica

**Disciplina:** Algoritmos e Programação de Computadores
**Entrega:** até a última aula do semestre
**Formato:** dupla (trabalhos individuais somente com justificativa prévia)
**Apresentação:** 10 minutos por dupla — demonstração ao vivo do sistema em funcionamento

---

## Contexto

Ao longo do semestre vocês aprenderam:

- lógica de programação com JavaScript (Code.org Game Lab)
- Python: variáveis, tipos, estruturas de controle, funções, listas, dicionários
- pandas: leitura de CSV/Excel, filtragem, agrupamento, `value_counts`, `merge`
- tkinter: janelas, widgets, layout com `grid`, eventos, diálogos, gráficos com matplotlib
- microdados PDAD 2024: estrutura de duas tabelas relacionadas por `A01nficha`, dicionário de variáveis, valores sentinela (99999, 88888), blocos temáticos (domicílio, educação, saúde, trabalho, renda)

O trabalho final integra esses conhecimentos num único produto: um **sistema com interface gráfica** que permite a uma pessoa explorar interativamente algum recorte da realidade social do Distrito Federal a partir dos dados do PDAD.

---

## Os dados

Vocês já trabalharam com os arquivos parciais. Para o trabalho final, usem os arquivos completos disponíveis em:

> **https://pdad.ipe.df.gov.br**

- `PDAD_2024-Moradores.csv` — uma linha por morador (~25 000 registros)
- `PDAD_2024-Domicilios.xlsx` — uma linha por domicílio
- `Dicionario_de_variaveis_PDAD_2024.xlsx` — descrição de cada coluna

**Lembrete essencial:** antes de qualquer análise, filtre os valores sentinela `99999` (não se aplica) e `88888` (não declarado) nas variáveis que usar.

---

## Escolha do recorte temático

Cada dupla escolhe **um** dos recortes abaixo. Dois grupos não podem ter o mesmo recorte — comuniquem a escolha ao professor até uma semana antes da entrega.

---

### Recorte A — Perfil educacional por Região Administrativa

**Pergunta central:** como varia o nível de escolaridade da população adulta entre as RAs do DF?

Variáveis principais: `escolaridade`, `localidade`, `idade_calculada`, `id_genero`

O sistema deve permitir selecionar uma ou mais RAs e visualizar a distribuição de escolaridade, comparar com a média do DF, e filtrar por faixa etária.

---

### Recorte B — Renda e desigualdade

**Pergunta central:** como se distribui a renda individual no DF? Quais RAs concentram mais renda?

Variáveis principais: `renda_ind`, `localidade`, `escolaridade`, `id_genero`, `E05`

O sistema deve permitir visualizar a distribuição de renda por RA, comparar rendas médias entre grupos (por gênero, por escolaridade), e identificar as 5 RAs com maior e menor renda média.

---

### Recorte C — Saúde e acesso a serviços

**Pergunta central:** qual é a cobertura de plano de saúde e o uso de serviços de saúde no DF?

Variáveis principais: blocos G (saúde) dos moradores, `localidade`, `idade_calculada`, `renda_ind`

O sistema deve permitir visualizar a taxa de cobertura por RA, correlacionar com renda ou escolaridade, e comparar grupos etários.

---

### Recorte D — Infraestrutura e condições dos domicílios

**Pergunta central:** como varia o acesso a infraestrutura (água, esgoto, internet, energia) entre as RAs?

Variáveis principais: blocos B e D da tabela de domicílios, `localidade`, `A01npessoas`

O sistema deve usar a tabela de domicílios como fonte principal, permitindo comparar indicadores de infraestrutura entre RAs e visualizar a relação entre tamanho do domicílio e tipo de imóvel.

---

### Recorte E — Trabalho e ocupação

**Pergunta central:** como se distribui a população ocupada no DF? Quais setores de atividade predominam?

Variáveis principais: bloco I (trabalho e renda) dos moradores, `localidade`, `escolaridade`, `id_genero`, `idade_calculada`

O sistema deve permitir filtrar por setor de atividade, visualizar a distribuição de ocupação por RA e gênero, e identificar a relação entre escolaridade e renda.

---

### Recorte F — Perfil demográfico e composição domiciliar

**Pergunta central:** como é a composição etária e familiar dos domicílios do DF?

Variáveis principais: `idade_calculada`, `id_genero`, `E05`, `A01npessoas`, `A01ncriancas`, `localidade`

O sistema deve usar o `merge` entre as duas tabelas, visualizar pirâmides etárias por RA, e mostrar a distribuição de domicílios por tamanho e tipo de arranjo familiar.

---

## Requisitos mínimos do sistema

O sistema deve ser um **programa Python com interface gráfica tkinter** que, ao ser executado com `python sistema.py`, abre uma janela principal a partir da qual o usuário consegue explorar os dados **sem precisar editar o código**.

### Requisito 1 — Janela principal com menu ou abas

A tela inicial deve apresentar:
- título do sistema e breve descrição do recorte
- pelo menos dois botões ou abas que levam a funcionalidades distintas
- indicação de quantos registros estão carregados (ex: "25.847 moradores · 9.312 domicílios")

### Requisito 2 — Pelo menos um filtro interativo

O usuário deve poder filtrar os dados por pelo menos uma variável usando widgets tkinter:
- uma lista suspensa (`OptionMenu` ou `ttk.Combobox`) para selecionar RA ou categoria
- ou um campo de texto (`Entry`) para buscar valor específico
- os resultados da filtragem devem aparecer na mesma janela, sem abrir um novo arquivo

### Requisito 3 — Pelo menos uma visualização com matplotlib

O sistema deve gerar pelo menos um gráfico de barras, histograma ou gráfico de linhas embutido na janela tkinter usando `FigureCanvasTkAgg`, conforme o exemplo `06_grafico.py`. O gráfico deve mudar quando o usuário alterar o filtro.

### Requisito 4 — Exibição de estatísticas descritivas

Para o recorte selecionado, o sistema deve calcular e exibir na janela:
- pelo menos três estatísticas numéricas relevantes (média, mediana, contagem, percentual ou similar)
- usando `tk.Label` com texto formatado em f-string

### Requisito 5 — Diálogo de exportação

O usuário deve poder exportar os dados filtrados ou as estatísticas para um arquivo `.txt` ou `.csv`, usando `filedialog.asksaveasfilename` (conforme `05_dialogos.py`). O arquivo gerado deve ser legível sem o programa.

### Requisito 6 — Tratamento de valores sentinela

O código deve explicitamente filtrar `99999` e `88888` nas variáveis utilizadas, com comentário indicando o motivo. Sistemas que calculam médias sem filtrar esses valores serão penalizados.

### Requisito 7 — Código organizado em funções

O programa deve ter pelo menos quatro funções com nome descritivo, cada uma com docstring de uma linha. Não é aceitável colocar tudo no escopo global.

### Requisito 8 — README no repositório GitHub

O repositório deve ter um `README.md` com:
- descrição do sistema em 3–5 frases
- como executar (`python sistema.py`)
- dependências (`pip install pandas matplotlib`)
- nome dos arquivos de dados necessários
- nomes dos integrantes da dupla

---

## Diferenciais para nota máxima

Os requisitos acima garantem a nota base. Para alcançar a nota máxima, o sistema deve implementar ao menos **dois** dos seguintes diferenciais:

**D1 — Segundo gráfico de tipo diferente**
Além do gráfico obrigatório, incluir um segundo gráfico de tipo distinto (ex: se o obrigatório é barras, o adicional pode ser histograma ou dispersão).

**D2 — Comparação entre duas RAs**
Permitir que o usuário selecione duas RAs e visualize uma comparação lado a lado no mesmo gráfico.

**D3 — Merge entre as duas tabelas**
Usar `pd.merge()` para cruzar a tabela de moradores com a de domicílios, produzindo alguma análise que exige dados das duas fontes (ex: escolaridade do responsável × infraestrutura do domicílio).

**D4 — Ordenação implementada à mão**
Para pelo menos uma lista exibida no sistema (ex: ranking de RAs por renda), implementar o algoritmo de ordenação manualmente (Bubble Sort, Selection Sort ou Insertion Sort) em vez de usar `.sort()` ou `.sort_values()` do pandas.

**D5 — Janela secundária com detalhes**
Ao clicar num item de uma lista ou barra do gráfico, abrir uma `tk.Toplevel` com informações detalhadas daquele item.

**D6 — Barra de progresso de carregamento**
Usar `ttk.Progressbar` para indicar visualmente o carregamento dos arquivos, que pode ser lento para os arquivos completos (~25 mil linhas).

---

## Avaliação

| Critério | Peso |
|---|---|
| Requisitos 1–8 implementados e funcionando | 50% |
| Qualidade da análise dos dados (pertinência, tratamento de sentinelas, interpretação) | 20% |
| Qualidade do código (funções, nomes descritivos, comentários, docstrings) | 15% |
| Diferenciais implementados (D1–D6) | 10% |
| Apresentação oral (clareza, domínio do código, resposta a perguntas) | 5% |

**Penalizações:**
- Sistema que não executa com `python sistema.py`: −30%
- Valores sentinela não tratados em variáveis numéricas: −20%
- Ausência de README no GitHub: −10%
- Trabalho individual sem justificativa prévia: não aceito

---

## Estrutura sugerida do repositório

```
pdad-explorer-dupla/
├── sistema.py              ← arquivo principal (python sistema.py)
├── utils/
│   ├── carregar.py         ← funções de leitura e limpeza dos dados
│   ├── calcular.py         ← funções de estatística e ordenação
│   └── exportar.py         ← função de exportação para arquivo
├── dados/
│   ├── moradores_parcial.csv       ← arquivo de teste local
│   └── domicilios_parcial.xlsx     ← arquivo de teste local
├── README.md
└── requirements.txt        ← pandas matplotlib openpyxl
```

Os arquivos completos do PDAD são grandes demais para o repositório — incluam apenas os parciais para teste. O README deve indicar onde baixar os completos.

---

## Dica de arquitetura

Uma estrutura que funciona bem para projetos desse tipo:

```python
import tkinter as tk
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")

# 1. Carregar dados ao iniciar
def carregar_dados():
    """Lê e limpa os arquivos PDAD; retorna dois DataFrames."""
    ...

# 2. Funções de análise (sem tkinter)
def calcular_distribuicao(df, variavel, filtro_ra=None):
    """Retorna contagem por categoria, com filtro opcional de RA."""
    ...

# 3. Funções de interface (chamam as de análise)
def atualizar_grafico():
    """Redesenha o gráfico com base nos filtros selecionados."""
    ...

# 4. Construir a janela
janela = tk.Tk()
moradores, domicilios = carregar_dados()
# ... montar widgets ...
janela.mainloop()
```

Separar a lógica de dados da interface facilita testar as funções individualmente e dividir o trabalho na dupla: uma pessoa cuida de `carregar.py` e `calcular.py`, a outra cuida da interface em `sistema.py`.

---

## Perguntas frequentes

**Posso usar outras bibliotecas além de pandas e matplotlib?**
Sim, desde que estejam disponíveis via `pip install` e listadas no `requirements.txt`.

**E se o arquivo completo do PDAD for muito lento para carregar?**
Usem os arquivos parciais durante o desenvolvimento. Para a apresentação, podem mostrar com os completos ou justificar o uso dos parciais.

**Posso usar o mesmo recorte de outro grupo?**
Não. Comuniquem a escolha ao professor para reservar o tema.

**O gráfico precisa ter título e eixos rotulados?**
Sim — gráficos sem título e sem rótulos de eixo serão penalizados na avaliação de qualidade do código.

---

*APC 2026/1 — Licenciatura em Computação — UnB/CIC*
*Prof. Jorge Henrique Cabral Fernandes | jhcf@unb.br*
