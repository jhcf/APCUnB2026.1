# Exercícios de Programação com Microdados do PDAD 2024 — Distrito Federal

**Disciplina:** Algoritmos e Programação de Computadores  
**Dados:** PDAD-A 2024 — Pesquisa Distrital por Amostra de Domicílios Ampliada  
**Arquivos:** `moradores_parcial.csv` · `domicilios_parcial.xlsx` · `dicionario_de_variaveis_pdad_2024.xlsx`

---

## Parte 1 — Entendendo os dados antes de programar

Antes de escrever uma linha de código, é fundamental entender de onde vêm os dados, como eles estão organizados e o que cada número significa. Esta seção é tão importante quanto os exercícios de programação.

---

### 1.1 — O que é o PDAD?

A **Pesquisa Distrital por Amostra de Domicílios (PDAD)** é realizada pelo **IPEDF** — Instituto de Pesquisa e Estatística do Distrito Federal — com o objetivo de traçar o perfil socioeconômico da população e das moradias do Distrito Federal. A versão de 2024 é chamada de **PDAD-A (Ampliada)** porque, pela primeira vez, incluiu áreas rurais e os 12 municípios da Periferia Metropolitana de Brasília (PMB).

Os microdados e o dicionário de variáveis estão disponíveis publicamente em:

> **https://pdad.ipe.df.gov.br**

Lá você encontra, para download:
- `PDAD_2024-Domicilios.xlsx` — um registro por domicílio visitado
- `PDAD_2024-Moradores.csv` — um registro por pessoa entrevistada
- `Dicionario_de_variaveis_PDAD_2024.xlsx` — descrição de cada coluna
- O questionário aplicado em campo e o manual do entrevistador

A pesquisa de 2024 visitou cerca de **25 mil domicílios** nas 35 Regiões Administrativas do DF. Os arquivos que usaremos nestes exercícios são amostras parciais desses dados.

---

### 1.2 — Como os dados estão organizados: duas tabelas relacionadas

Os microdados do PDAD seguem o modelo de **duas tabelas relacionadas**, muito comum em bancos de dados e pesquisas domiciliares:

```
┌─────────────────────────────────────┐
│         TABELA: domicílios          │  ← uma linha por domicílio
│  A01nficha | localidade | B01 | ... │
│    00001   |    5330    |  1  | ... │
│    00002   |    5320    |  1  | ... │
└──────────────┬──────────────────────┘
               │  chave de ligação: A01nficha
               │  (número da ficha do domicílio)
               ▼
┌─────────────────────────────────────┐
│         TABELA: moradores           │  ← várias linhas por domicílio
│  A01nficha | morador_id | E05 | ... │
│    00002   |  00002-1   |  2  | ... │
│    00002   |  00002-2   |  2  | ... │
│    00002   |  00002-3   |  2  | ... │
└─────────────────────────────────────┘
```

**Regra fundamental:** um domicílio pode ter vários moradores, mas cada morador pertence a exatamente um domicílio. A coluna `A01nficha` (número da ficha) é o elo entre as duas tabelas.

---

### 1.3 — O dicionário de variáveis: como ler os dados corretamente

Os nomes das colunas nos arquivos (`E05`, `B07`, `I20`) não dizem nada por si só. O **dicionário de variáveis** é o documento que traduz esses códigos em perguntas reais do questionário.

Abra o arquivo `dicionario_de_variaveis_pdad_2024.xlsx` e procure, por exemplo, a variável `E05`. Você verá algo como:

| Variável | Descrição | Categorias |
|----------|-----------|------------|
| E05 | Situação de residência no domicílio | 1=Chefe, 2=Cônjuge, 3=Filho(a), 4=Outros |

**Exercício mental:** antes de programar qualquer coisa, abra o dicionário e localize as variáveis listadas abaixo. Para cada uma, anote: o que a pergunta mede? Quais são os valores possíveis?

| Variável | Tabela | Sua anotação |
|----------|--------|--------------|
| `idade_calculada` | moradores | |
| `id_genero` | moradores | |
| `escolaridade` | moradores | |
| `renda_ind` | moradores | |
| `A01npessoas` | domicílios | |
| `A01ncriancas` | domicílios | |
| `B07` | domicílios | |
| `B08` | domicílios | |

---

### 1.4 — Os blocos temáticos do questionário

As colunas dos microdados seguem a estrutura do questionário aplicado em campo. Cada letra identifica um bloco temático:

**Tabela de domicílios:**

| Bloco | Letra | Temas abordados |
|-------|-------|-----------------|
| Identificação | A | Número da ficha, UF, localidade, setor, contagem de moradores |
| Domicílio | B | Tipo de imóvel, posse, aluguel, infraestrutura (água, esgoto, energia) |
| Equipamentos | C | Eletrodomésticos, veículos, acesso à internet |
| Saneamento | D | Coleta de lixo, abastecimento de água |
| Renda domiciliar | — | Variáveis derivadas: renda total, per capita, deflacionada |

**Tabela de moradores:**

| Bloco | Letra | Temas abordados |
|-------|-------|-----------------|
| Identificação | A | Ficha, localidade, identificador do morador |
| Composição | E | Idade, gênero, cor/raça, naturalidade, religião, deficiência |
| Migração | F | Local de nascimento, tempo de residência no DF |
| Saúde | G | Plano de saúde, uso de serviços de saúde |
| Educação | H | Frequência escolar, escolaridade, curso atual |
| Trabalho e Renda | I | Ocupação, setor de atividade, renda individual |
| Derivadas | — | `renda_ind`, `escolaridade`, `id_genero`, `lgbtqiam`, `peso_mor` |

---

### 1.5 — Valores especiais: o que significam 99999 e 88888?

Ao abrir os dados pela primeira vez, você verá muitos números como `99999` e `88888`. Eles não são dados reais — são **códigos de ausência**:

| Código | Significado |
|--------|-------------|
| `99999` | Não se aplica (a pergunta não era válida para essa pessoa/domicílio) |
| `88888` | Não declarado / recusou responder |

**Exemplo prático:** a variável `renda_ind` tem `99999` para crianças pequenas — elas não têm renda, então a pergunta simplesmente não foi feita. Já `88888` aparece quando a pessoa foi entrevistada mas preferiu não informar a renda.

Isso significa que, em qualquer análise, você precisa **filtrar esses valores** antes de calcular médias, ordenar ou gerar relatórios. Um erro comum de iniciantes é calcular a média de idades incluindo os `99999`, obtendo um resultado completamente sem sentido.

---

### 1.6 — O que é o peso amostral?

A coluna `peso_mor` (moradores) e `peso_dom` (domicílios) contém o **peso amostral** de cada registro. Como a pesquisa visitou apenas uma amostra da população total, cada entrevistado "representa" um certo número de pessoas reais no DF.

Por exemplo, se `peso_mor = 78.6`, significa que aquele morador representa aproximadamente 79 pessoas na população real do DF.

Nos exercícios deste caderno, **não usaremos o peso amostral** — trabalharemos com contagens simples. Mas é importante saber que ele existe: análises estatísticas oficiais precisam multiplicar os valores pelo peso para obter estimativas corretas da população.

---

### 1.7 — As Regiões Administrativas (RAs)

O DF é dividido em **35 Regiões Administrativas**. Nos microdados, cada domicílio e morador está identificado pelo código numérico da RA na coluna `localidade`. Os dados de exemplo que usaremos contêm moradores de 7 RAs:

| Código | Nome da RA | Característica geral |
|--------|------------|----------------------|
| 5249 | Arniqueira | RA mais nova, criada em 2019 |
| 5314 | Sobradinho II | Região satélite ao norte |
| 5315 | Jardim Botânico | Área de alta renda ao leste |
| 5319 | Lago Sul | Uma das RAs de maior renda do DF |
| 5320 | Gama | Uma das cidades-satélite mais antigas |
| 5326 | Samambaia | Segunda maior população do DF |
| 5330 | São Sebastião | Crescimento acelerado nas últimas décadas |

Para ver todas as 35 RAs com seus códigos, consulte o dicionário de variáveis ou o relatório de resultados disponível em https://pdad.ipe.df.gov.br.

---

### 1.8 — Como as duas tabelas se conectam na prática

Imagine que você quer saber: *"Quantas crianças vivem em domicílios onde o responsável tem ensino superior?"*

Para responder isso, você precisa cruzar as duas tabelas:

1. Na tabela de **moradores**, encontre quem é o responsável pelo domicílio (`E05 = 1`) e qual é sua escolaridade (`escolaridade = 7 ou 8`)
2. Pegue o `A01nficha` dessas pessoas
3. Na tabela de **domicílios**, use esse `A01nficha` para encontrar o domicílio correspondente
4. Leia o campo `A01ncriancas` para saber quantas crianças moram lá

Esse tipo de operação — juntar duas tabelas por uma chave em comum — é chamado de **junção (join)** e é um dos conceitos mais importantes da programação com dados. Em pandas, fazemos isso com `pd.merge()`.

---

### 1.9 — Roteiro de leitura antes de programar

Antes de começar os exercícios, faça o seguinte:

1. **Baixe os arquivos completos** em https://pdad.ipe.df.gov.br
2. **Abra o dicionário de variáveis** no Excel e leia as primeiras 50 linhas
3. **Abra `moradores_parcial.csv`** em um editor de texto ou no Excel e observe:
   - Qual é o separador de campos? (`;` ponto e vírgula)
   - Qual é o separador decimal? (`,` vírgula)
   - Quantas colunas existem? (134)
   - Quantas linhas de dados? (além do cabeçalho)
4. **Identifique manualmente** um domicílio com mais de uma linha na tabela de moradores (procure por `A01nficha` repetido)
5. **Localize no dicionário** as variáveis `E05`, `I20` e `H03` — o que elas perguntam?

Só depois disso, siga para os exercícios de código.

---

## Parte 2 — Exercícios de Programação

Os exercícios estão organizados em quatro níveis progressivos:

- 🟢 **Nível 1 — Trivial:** leitura e exibição de dados
- 🟡 **Nível 2 — Básico:** filtragem e cálculos simples
- 🟠 **Nível 3 — Intermediário:** algoritmos de ordenação implementados à mão
- 🔴 **Nível 4 — Avançado:** relatórios completos via linha de comando

---

## 🟢 Nível 1 — Trivial

### Exercício 1.1 — Lendo os dados

**Objetivo:** Carregar a tabela de moradores e exibir as primeiras linhas.

**O que aprender:** `import`, `pandas`, `read_csv`, `head`.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")
print(moradores.head())
```

**Tarefa:** Execute o código. Quantas linhas e colunas aparecem?  
Dica: use `moradores.shape` para descobrir.

---

### Exercício 1.2 — Selecionando colunas

**Objetivo:** Exibir apenas as colunas relevantes para análise humana.

**O que aprender:** Seleção de colunas por nome.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

colunas = ["morador_id", "localidade", "idade_calculada", "id_genero", "escolaridade", "renda_ind"]
print(moradores[colunas])
```

**Tarefa:** Adicione a coluna `peso_mor` à lista e reexecute.

---

### Exercício 1.3 — Contando moradores por domicílio

**Objetivo:** Ler a tabela de domicílios e mostrar quantas pessoas moram em cada um.

**O que aprender:** `read_excel`, iteração sobre linhas de um DataFrame.

```python
import pandas as pd

domicilios = pd.read_excel("domicilios_parcial.xlsx")

for _, linha in domicilios.iterrows():
    print(f"Domicílio {linha['A01nficha']}: {linha['A01npessoas']} moradores, {linha['A01ncriancas']} crianças")
```

**Tarefa:** Qual domicílio tem mais moradores? Qual tem mais crianças?

---

### Exercício 1.4 — Exibindo idades

**Objetivo:** Listar todas as idades dos moradores, excluindo o valor 99999.

**O que aprender:** Filtragem simples com condição booleana.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

adultos = moradores[moradores["idade_calculada"] != 99999]
print(adultos[["morador_id", "idade_calculada"]])
```

**Tarefa:** Quantos moradores têm idade declarada? Quantos têm 99999?  
Reflita: por que uma pessoa teria 99999 no campo de idade?  
(Dica: releia a seção 1.5 sobre valores especiais.)

---

## 🟡 Nível 2 — Básico

### Exercício 2.1 — Calculando a idade média

**Objetivo:** Calcular a média de idade dos moradores com idade declarada.

**O que aprender:** Média aritmética, filtragem, listas em Python.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

idades = moradores[moradores["idade_calculada"] != 99999]["idade_calculada"].tolist()

soma = 0
for idade in idades:
    soma = soma + idade

media = soma / len(idades)
print(f"Total de moradores com idade declarada: {len(idades)}")
print(f"Soma das idades: {soma}")
print(f"Média de idade: {media:.1f} anos")
```

> ⚠️ **Atenção:** calcule a média manualmente com `for`, não use `.mean()`.  
> O objetivo é aprender o algoritmo por dentro.

**Tarefa:** Qual é o morador mais velho? E o mais novo com idade > 0?

---

### Exercício 2.2 — Contando por escolaridade

**Objetivo:** Contar quantos moradores há em cada nível de escolaridade.

**O que aprender:** Dicionários, contagem manual, mapeamento de códigos.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

escolaridade_nome = {
    1: "Sem instrução",
    2: "Fundamental incompleto",
    3: "Fundamental completo",
    4: "Médio incompleto",
    5: "Médio completo",
    6: "Superior incompleto",
    7: "Superior completo",
    8: "Pós-graduação",
}

contagem = {}
for _, linha in moradores.iterrows():
    nivel = linha["escolaridade"]
    if nivel in escolaridade_nome:
        if nivel not in contagem:
            contagem[nivel] = 0
        contagem[nivel] += 1

print("Escolaridade dos moradores:")
for nivel, total in contagem.items():
    print(f"  {escolaridade_nome[nivel]}: {total} moradores")
```

**Tarefa:** Qual é o nível de escolaridade mais comum nos dados?

---

### Exercício 2.3 — Filtrando por Região Administrativa

**Objetivo:** Listar os moradores de uma RA específica.

**O que aprender:** Parâmetros, filtragem por valor, formatação de saída.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

ra_alvo = 5320  # Gama

filtro = moradores[moradores["localidade"] == ra_alvo]

print(f"Moradores da RA {ra_alvo}:")
for _, linha in filtro.iterrows():
    print(f"  {linha['morador_id']} — {linha['idade_calculada']} anos — escolaridade: {linha['escolaridade']}")
```

**Tarefa:** Altere `ra_alvo` para `5330` (São Sebastião) e compare os resultados.

---

### Exercício 2.4 — Renda dos moradores declarantes

**Objetivo:** Listar apenas os moradores que declararam renda.

**O que aprender:** Múltiplas condições de filtragem.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

com_renda = moradores[(moradores["renda_ind"] > 0) & (moradores["renda_ind"] != 99999)]

print(f"Moradores com renda declarada: {len(com_renda)}")
for _, linha in com_renda.iterrows():
    print(f"  {linha['morador_id']} — R$ {linha['renda_ind']:,.0f}")
```

**Tarefa:** Calcule a média de renda entre quem declarou. Use um `for`, não `.mean()`.

---

## 🟠 Nível 3 — Intermediário (Algoritmos de Ordenação)

### Exercício 3.1 — Ordenando por idade (Bubble Sort)

**Objetivo:** Ordenar a lista de moradores por idade usando Bubble Sort implementado à mão.

**O que aprender:** Bubble Sort, listas de dicionários, complexidade O(n²).

**Como funciona o Bubble Sort:**  
O algoritmo percorre a lista repetidamente. A cada passagem, compara dois elementos adjacentes e os troca de lugar se estiverem fora de ordem. Elementos maiores "borbulham" para o final da lista a cada passagem.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

validos = moradores[moradores["idade_calculada"] != 99999].copy()
lista = validos[["morador_id", "idade_calculada"]].to_dict("records")

# Bubble Sort por idade
n = len(lista)
for i in range(n):
    for j in range(n - i - 1):
        if lista[j]["idade_calculada"] > lista[j + 1]["idade_calculada"]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Moradores ordenados do mais novo ao mais velho:")
for m in lista:
    print(f"  {m['morador_id']}: {m['idade_calculada']} anos")
```

**Tarefa:**
1. Conte quantas trocas (`swap`) o algoritmo realizou. Adicione um contador.
2. Inverta a ordenação: do mais velho ao mais novo.

---

### Exercício 3.2 — Ordenando por renda (Selection Sort)

**Objetivo:** Ordenar moradores com renda declarada usando Selection Sort.

**O que aprender:** Selection Sort, busca de mínimo, O(n²).

**Como funciona o Selection Sort:**  
A cada passagem, o algoritmo encontra o menor elemento do trecho ainda não ordenado e o coloca na posição correta. Em vez de fazer muitas trocas pequenas como o Bubble Sort, ele faz exatamente uma troca por passagem.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

com_renda = moradores[(moradores["renda_ind"] > 0) & (moradores["renda_ind"] != 99999)].copy()
lista = com_renda[["morador_id", "renda_ind"]].to_dict("records")

# Selection Sort por renda (crescente)
n = len(lista)
for i in range(n):
    idx_min = i
    for j in range(i + 1, n):
        if lista[j]["renda_ind"] < lista[idx_min]["renda_ind"]:
            idx_min = j
    lista[i], lista[idx_min] = lista[idx_min], lista[i]

print("Moradores ordenados por renda (menor para maior):")
for m in lista:
    print(f"  {m['morador_id']}: R$ {m['renda_ind']:,.0f}")
```

**Tarefa:**
1. Modifique para ordenar do maior para o menor.
2. Adicione a escolaridade do morador na exibição.

---

### Exercício 3.3 — Ordenando por nome de RA (Insertion Sort)

**Objetivo:** Ordenar as Regiões Administrativas encontradas nos dados por nome, usando Insertion Sort.

**O que aprender:** Insertion Sort, ordenação de strings, O(n²).

**Como funciona o Insertion Sort:**  
Funciona como organizar cartas na mão. Pega um elemento de cada vez e o insere na posição correta dentro da parte já ordenada. É eficiente para listas pequenas ou quase ordenadas.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")

ra_nomes = {
    5249: "Arniqueira",    5301: "Brasília",       5303: "Taguatinga",
    5305: "Sobradinho",    5311: "Cruzeiro",        5313: "Ceilândia",
    5314: "Sobradinho II", 5315: "Jardim Botânico", 5319: "Lago Sul",
    5320: "Gama",          5326: "Samambaia",       5328: "Santa Maria",
    5330: "São Sebastião",
}

codigos = moradores["localidade"].unique().tolist()
ras = [{"codigo": c, "nome": ra_nomes.get(c, f"RA-{c}")} for c in codigos]

# Insertion Sort por nome
for i in range(1, len(ras)):
    chave = ras[i]
    j = i - 1
    while j >= 0 and ras[j]["nome"] > chave["nome"]:
        ras[j + 1] = ras[j]
        j -= 1
    ras[j + 1] = chave

print("Regiões Administrativas (ordem alfabética):")
for ra in ras:
    total = (moradores["localidade"] == ra["codigo"]).sum()
    print(f"  {ra['nome']} (cód. {ra['codigo']}): {total} moradores na amostra")
```

**Tarefa:** Adicione, após o nome, a média de idade dos moradores daquela RA.

---

### Exercício 3.4 — Comparando algoritmos de ordenação

**Objetivo:** Medir quantas comparações cada algoritmo realiza para ordenar a mesma lista.

**O que aprender:** Análise empírica de complexidade, contagem de operações.

```python
import pandas as pd

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")
validos = moradores[moradores["idade_calculada"] != 99999].copy()
idades_base = validos["idade_calculada"].tolist()

def bubble_sort_conta(lista):
    lst = lista[:]
    comparacoes = 0
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            comparacoes += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst, comparacoes

def selection_sort_conta(lista):
    lst = lista[:]
    comparacoes = 0
    n = len(lst)
    for i in range(n):
        idx_min = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lst[j] < lst[idx_min]:
                idx_min = j
        lst[i], lst[idx_min] = lst[idx_min], lst[i]
    return lst, comparacoes

def insertion_sort_conta(lista):
    lst = lista[:]
    comparacoes = 0
    for i in range(1, len(lst)):
        chave = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > chave:
            comparacoes += 1
            lst[j + 1] = lst[j]
            j -= 1
        comparacoes += 1
        lst[j + 1] = chave
    return lst, comparacoes

n = len(idades_base)
_, c_bubble    = bubble_sort_conta(idades_base)
_, c_selection = selection_sort_conta(idades_base)
_, c_insertion = insertion_sort_conta(idades_base)

print(f"Ordenando {n} elementos (idades dos moradores):")
print(f"  Bubble Sort:    {c_bubble} comparações")
print(f"  Selection Sort: {c_selection} comparações")
print(f"  Insertion Sort: {c_insertion} comparações")
print(f"  Teórico O(n²):  {n*n}  (n={n}, n²={n}²)")
```

**Tarefa:**
1. O que acontece com as contagens se a lista já estiver ordenada?
2. E se estiver ordenada ao contrário?

---

## 🔴 Nível 4 — Avançado (Relatórios via CLI)

### Exercício 4.1 — Relatório em TXT por linha de comando

**Objetivo:** Gerar um arquivo `.txt` com estatísticas, com o nome definido pelo usuário via `sys.argv`.

**O que aprender:** `sys.argv`, `open()`, escrita em arquivo, CLI.

```python
# relatorio_moradores.py
import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Uso: python relatorio_moradores.py <nome_do_arquivo.txt>")
    sys.exit(1)

arquivo_saida = sys.argv[1]

moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")
validos = moradores[moradores["idade_calculada"] != 99999]
idades = validos["idade_calculada"].tolist()
media_idade = sum(idades) / len(idades)

linhas = []
linhas.append("=" * 50)
linhas.append("RELATÓRIO PDAD 2024 — MORADORES")
linhas.append("=" * 50)
linhas.append(f"Total de moradores na amostra : {len(moradores)}")
linhas.append(f"Com idade declarada           : {len(validos)}")
linhas.append(f"Média de idade                : {media_idade:.1f} anos")
linhas.append(f"Idade mínima                  : {min(idades)} anos")
linhas.append(f"Idade máxima                  : {max(idades)} anos")
linhas.append("")

with open(arquivo_saida, "w", encoding="utf-8") as f:
    for linha in linhas:
        f.write(linha + "\n")

print(f"Relatório salvo em: {arquivo_saida}")
```

**Como executar no terminal:**
```bash
python relatorio_moradores.py relatorio_moradores.txt
```

**Tarefa:** Adicione ao relatório a contagem por RA, ordenada pelo nome usando Insertion Sort.

---

### Exercício 4.2 — Relatório interativo com menu

**Objetivo:** Criar um programa com menu de opções na linha de comando.

**O que aprender:** `input()`, laço `while`, separação em funções.

```python
# menu_pdad.py
import pandas as pd

def carregar_dados():
    mor = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")
    dom = pd.read_excel("domicilios_parcial.xlsx")
    return mor, dom

def relatorio_idades(moradores):
    validos = moradores[moradores["idade_calculada"] != 99999]
    idades = validos["idade_calculada"].tolist()
    print(f"\n  Total com idade declarada: {len(idades)}")
    print(f"  Média: {sum(idades)/len(idades):.1f} anos")
    print(f"  Mínima: {min(idades)} | Máxima: {max(idades)}")

def relatorio_escolaridade(moradores):
    nomes = {1:"Sem instrução",2:"Fund. incompleto",3:"Fund. completo",
             4:"Médio incompleto",5:"Médio completo",6:"Superior incompleto",
             7:"Superior completo",8:"Pós-graduação"}
    contagem = {}
    for _, linha in moradores.iterrows():
        n = linha["escolaridade"]
        if n in nomes:
            contagem[n] = contagem.get(n, 0) + 1
    print("\n  Escolaridade:")
    for nivel, total in sorted(contagem.items()):
        print(f"    {nomes[nivel]}: {total}")

def relatorio_domicilios(domicilios):
    print(f"\n  Total de domicílios: {len(domicilios)}")
    media_pessoas = sum(domicilios["A01npessoas"]) / len(domicilios)
    print(f"  Média de moradores por domicílio: {media_pessoas:.1f}")

moradores, domicilios = carregar_dados()

while True:
    print("\n" + "=" * 40)
    print("  PDAD 2024 — Menu de Relatórios")
    print("=" * 40)
    print("  1. Relatório de idades")
    print("  2. Relatório de escolaridade")
    print("  3. Relatório de domicílios")
    print("  0. Sair")
    opcao = input("\n  Escolha uma opção: ").strip()

    if opcao == "1":
        relatorio_idades(moradores)
    elif opcao == "2":
        relatorio_escolaridade(moradores)
    elif opcao == "3":
        relatorio_domicilios(domicilios)
    elif opcao == "0":
        print("  Até logo!")
        break
    else:
        print("  Opção inválida.")
```

**Tarefa:** Adicione a opção `4. Salvar relatório completo em TXT` que chama as três funções e grava o resultado em `relatorio_completo.txt`.

---

### Exercício 4.3 — Programa completo com argumento de RA

**Objetivo:** Programa que recebe o código de uma RA como argumento, gera estatísticas e salva relatório com moradores ordenados por idade.

**O que aprender:** Integração de tudo — CLI, filtragem, Bubble Sort, escrita em arquivo.

```python
# analise_ra.py
import sys
import pandas as pd

RA_NOMES = {
    5249: "Arniqueira",    5301: "Brasília",       5303: "Taguatinga",
    5305: "Sobradinho",    5311: "Cruzeiro",        5313: "Ceilândia",
    5314: "Sobradinho II", 5315: "Jardim Botânico", 5319: "Lago Sul",
    5320: "Gama",          5326: "Samambaia",       5328: "Santa Maria",
    5330: "São Sebastião",
}

ESCOLARIDADE = {1:"Sem instrução",2:"Fund. incompleto",3:"Fund. completo",
                4:"Médio incompleto",5:"Médio completo",6:"Superior incompleto",
                7:"Superior completo",8:"Pós-graduação"}

def bubble_sort_por_idade(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j]["idade"] > lista[j + 1]["idade"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def gerar_relatorio(ra_codigo):
    moradores = pd.read_csv("moradores_parcial.csv", sep=";", decimal=",", encoding="utf-8-sig")
    filtro = moradores[moradores["localidade"] == ra_codigo]

    if filtro.empty:
        print(f"Nenhum dado encontrado para a RA {ra_codigo}.")
        sys.exit(1)

    ra_nome = RA_NOMES.get(ra_codigo, f"RA-{ra_codigo}")
    validos = filtro[filtro["idade_calculada"] != 99999]
    idades = validos["idade_calculada"].tolist()

    lista_moradores = []
    for _, linha in validos.iterrows():
        lista_moradores.append({
            "id": linha["morador_id"],
            "idade": linha["idade_calculada"],
            "escolaridade": ESCOLARIDADE.get(linha["escolaridade"], "?"),
            "renda": linha["renda_ind"] if linha["renda_ind"] != 99999 else None,
        })
    lista_moradores = bubble_sort_por_idade(lista_moradores)

    linhas = []
    linhas.append("=" * 55)
    linhas.append(f"  PDAD 2024 — Análise da RA: {ra_nome} (cód. {ra_codigo})")
    linhas.append("=" * 55)
    linhas.append(f"  Total de moradores na amostra : {len(filtro)}")
    linhas.append(f"  Com idade declarada           : {len(validos)}")
    if idades:
        linhas.append(f"  Média de idade                : {sum(idades)/len(idades):.1f} anos")
        linhas.append(f"  Faixa etária                  : {min(idades)} a {max(idades)} anos")
    linhas.append("")
    linhas.append("  Moradores (ordenados por idade):")
    linhas.append("  " + "-" * 50)
    for m in lista_moradores:
        renda_str = f"R$ {m['renda']:,.0f}" if m["renda"] else "não declarada"
        linhas.append(f"  {m['id']:12s} | {m['idade']:3d} anos | {m['escolaridade']:25s} | {renda_str}")
    linhas.append("")
    return linhas, ra_nome

if len(sys.argv) < 2:
    print("Uso: python analise_ra.py <codigo_ra> [arquivo_saida.txt]")
    print("Exemplo: python analise_ra.py 5320")
    print("Exemplo: python analise_ra.py 5320 relatorio_gama.txt")
    sys.exit(1)

ra = int(sys.argv[1])
linhas, nome = gerar_relatorio(ra)

for linha in linhas:
    print(linha)

if len(sys.argv) >= 3:
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        for linha in linhas:
            f.write(linha + "\n")
    print(f"\n  Relatório salvo em: {sys.argv[2]}")
```

**Como executar:**
```bash
# Só exibe na tela
python analise_ra.py 5320

# Exibe e salva em arquivo
python analise_ra.py 5320 relatorio_gama.txt

# Outra RA
python analise_ra.py 5330 relatorio_sao_sebastiao.txt
```

**Tarefa final (desafio):**
1. Adicione ao relatório a distribuição de escolaridade da RA, ordenada por Insertion Sort.
2. Adicione uma opção `--todas` que gera um relatório para todas as RAs presentes, salvando um arquivo por RA.
3. Compare a velocidade dos três algoritmos para ordenar os moradores. Qual é mais rápido nos seus dados?

---

## Tabela-resumo dos exercícios

| # | Nível | Conceito principal | Algoritmo |
|---|-------|--------------------|-----------|
| 1.1 | 🟢 | Leitura de CSV | — |
| 1.2 | 🟢 | Seleção de colunas | — |
| 1.3 | 🟢 | Leitura de Excel | — |
| 1.4 | 🟢 | Filtragem + valores especiais | — |
| 2.1 | 🟡 | Média aritmética manual | Soma acumulada |
| 2.2 | 🟡 | Contagem com dicionário | Varredura linear |
| 2.3 | 🟡 | Filtro por RA | Busca linear |
| 2.4 | 🟡 | Múltiplas condições | — |
| 3.1 | 🟠 | Ordenação por idade | **Bubble Sort** |
| 3.2 | 🟠 | Ordenação por renda | **Selection Sort** |
| 3.3 | 🟠 | Ordenação alfabética | **Insertion Sort** |
| 3.4 | 🟠 | Análise de complexidade | Os três juntos |
| 4.1 | 🔴 | Relatório TXT + CLI | Insertion Sort |
| 4.2 | 🔴 | Menu interativo | — |
| 4.3 | 🔴 | Programa completo por RA | **Bubble Sort** |
