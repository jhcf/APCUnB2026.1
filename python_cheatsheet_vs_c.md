# Python — Cheatsheet Semântico (espelho da cheatsheet C)

> **Como usar:** acesse <https://pythontutor.com/python-compiler.html>, cole o código
> e clique em **"Visualize Execution"**. Use **Next/Prev** para avançar passo a passo.
>
> Este documento mapeia cada construção da cheatsheet C para seu equivalente Python,
> destacando **diferenças semânticas e de modelo de memória**.

---

## Diferença fundamental: caixas vs. etiquetas

| C | Python |
|---|--------|
| Variável **é** uma caixa de memória com tamanho fixo | Variável é uma **etiqueta** (referência) colada em um objeto |
| `int x = 10` reserva 4 bytes e coloca 10 lá | `x = 10` cria o objeto `10` no heap e faz `x` apontar para ele |
| Tipos são da **variável** (estáticos) | Tipos são do **objeto** (dinâmicos) |
| Memória gerenciada **manualmente** (`malloc`/`free`) | Memória gerenciada pelo **Garbage Collector** (contagem de referências + GC cíclico) |
| `==` compara **valores** | `==` compara **valores**; `is` compara **identidade** (mesmo objeto) |

---

## 1. Estrutura de um programa

**Em C:** obrigatório `#include`, função `main`, `return 0`.

**Em Python:** nenhum boilerplate obrigatório. O módulo de topo é executado
diretamente. A convenção `if __name__ == "__main__"` separa código executável
de código importável.

```python
# modulo.py — tudo no nível de módulo é executado na importação
print("executado sempre")

# guarda de entrada: executado só quando rodado diretamente
if __name__ == "__main__":
    print("ponto de entrada principal")
```

> Em C há **uma** função `main`. Em Python, qualquer `.py` pode ser o ponto de
> entrada; `if __name__` é convenção, não exigência do interpretador.

### 🔬 Exercício 1 — Estrutura mínima

```python
print("Ola, mundo!")
```

**O que observar:** o PythonTutor mostra um único frame `Global` — não há `main`.
Todo código de módulo vive no escopo global.

---

## 2. Tipos e o modelo de objetos

**Em C:** tipos são atributos da *variável* e têm tamanho fixo em bytes.

**Em Python:** tipos são atributos do *objeto*. `int` Python tem precisão
arbitrária (sem overflow); `float` é um double de 64 bits. Tudo é objeto,
inclusive funções e classes.

| C                  | Python          | Observação                                    |
|--------------------|-----------------|-----------------------------------------------|
| `char c = 'A'`     | `c = 'A'`       | `str` de 1 caractere; strings são imutáveis   |
| `int x = 42`       | `x = 42`        | `int` sem tamanho fixo (precisão arbitrária)  |
| `long`             | `int`           | Mesmo tipo — Python não distingue             |
| `float f = 3.14f`  | `f = 3.14`      | `float` = double de 64 bits                   |
| `double d = 3.14`  | `f = 3.14`      | Idem — Python só tem `float`                  |
| `_Bool b = 1`      | `b = True`      | `bool` é subclasse de `int` (True==1)         |
| `unsigned int`     | `int` (sempre ≥0 via lógica) | Python `int` nunca faz wrap-around |
| `void`             | `None`          | Tipo/valor sentinela                           |

```python
x = 42
f = 3.14
c = 'Z'
s = "Brasilia"
b = True
n = None        # equivale ao NULL/void de C

print(type(x))  # <class 'int'>
print(type(f))  # <class 'float'>
print(type(b))  # <class 'bool'>
```

### 🔬 Exercício 2 — Tipos dinâmicos e identidade de objeto

```python
x = 42
print(type(x))      # <class 'int'>
print(id(x))        # endereço do objeto no heap (como %p em C)

x = "agora sou str" # reatribuição: x aponta para outro objeto
print(type(x))      # <class 'str'>

a = 1000
b = 1000
print(a == b)       # True  — mesmo valor
print(a is b)       # pode ser False — objetos diferentes no heap
```

**O que observar:** `x` muda de tipo porque a *etiqueta* foi colada em outro
objeto — não porque a "caixa" foi reformatada. `id()` mostra o endereço real
no heap (equivalente a `%p` no `printf` de C).

---

## 3. Declaração e atribuição

**Em C:** declarar reserva memória; inicializar coloca valor. São atos separáveis.

**Em Python:** não existe *declaração sem valor*. Toda atribuição cria uma
ligação (*binding*) nome → objeto. Não há "valor lixo".

```python
# C: int x;  ← reserva memória, valor indefinido
# Python: não existe equivalente seguro — x existirá somente após atribuição

x = 10          # cria objeto int(10) e liga 'x' a ele
x = x + 5      # cria int(15), religar 'x'; int(10) pode ser coletado

# "constante" — convenção de nomes em MAIÚSCULAS (não imposta pela linguagem)
PI = 3.14159
MAX_ITER = 100
```

> ⚠ Em C, `const` é imposto pelo compilador. Em Python, `PI = 3.14159` é apenas
> uma convenção — nada impede `PI = 0`. Para constantes verdadeiras, use `Final`
> do módulo `typing` (verificado por linters, não pelo interpretador).

```python
from typing import Final
PI: Final = 3.14159
```

### 🔬 Exercício 3 — Reatribuição e contagem de referências

```python
a = [1, 2, 3]   # lista criada no heap; 'a' aponta para ela
b = a            # 'b' é outra etiqueta para o MESMO objeto
b.append(4)
print(a)         # [1, 2, 3, 4] — 'a' vê a mudança!

b = [9, 9]       # 'b' religar para nova lista; 'a' não muda
print(a)         # [1, 2, 3, 4]
print(b)         # [9, 9]
```

**O que observar:** no PythonTutor, `a` e `b` aparecem como setas para o
**mesmo** objeto lista após `b = a`. Após `b = [9,9]`, as setas se separam.
Isso é o equivalente de dois ponteiros C apontando para o mesmo bloco heap.

---

## 4. Operadores

```python
# Aritméticos
+  -  *  /   # / sempre retorna float em Python 3
//           # divisão inteira (floor division) — equivale ao / inteiro de C
%            # módulo
**           # exponenciação (não existe em C sem pow())

# Relacionais
==  !=  <  >  <=  >=

# Lógicos (palavras, não símbolos)
and   or   not     # equivalem a &&  ||  !  de C

# Identidade e pertencimento
is    is not       # mesmo objeto (endereço)
in    not in       # pertencimento a coleção

# Bit a bit (iguais ao C)
&  |  ^  ~  <<  >>

# Atribuição aumentada
+=  -=  *=  /=  //=  %=  **=  &=  |=  ^=  <<=  >>=

# Ternário (expressão condicional)
valor = a if condicao else b   # equivale a: cond ? a : b
```

> **Diferença crítica:** `/` em Python 3 é **sempre divisão real** (`5/2 == 2.5`).
> Para divisão inteira como em C, use `//` (`5//2 == 2`).

### 🔬 Exercício 4 — Divisão, módulo, operador ternário e `is`

```python
a, b = 17, 5

print(a / b)     # 3.4  — float! (C daria 3)
print(a // b)    # 3    — equivale ao / inteiro de C
print(a % b)     # 2

x = 3
x += 1           # x = 4 (religar para novo objeto int(4))
print(x)

maximo = a if a > b else b
print("max =", maximo)

# is vs ==
p = [1, 2]
q = [1, 2]
print(p == q)    # True  — mesmos valores
print(p is q)    # False — objetos distintos no heap
```

**O que observar:** `x += 1` cria um **novo** objeto `int(4)` — no PythonTutor,
a seta de `x` muda de destino. Em C, `x++` modifica os bytes da caixa no lugar.

---

## 5. Controle de fluxo

**Em C:** chaves `{}` delimitam blocos. **Em Python:** indentação delimita blocos.
Não há `switch` nativo até Python 3.10 (`match`/`case`).

```python
# if / elif / else
if x > 0:
    print("positivo")
elif x == 0:
    print("zero")
else:
    print("negativo")

# match/case (Python ≥ 3.10) — equivale ao switch de C
match op:
    case '+': resultado = a + b
    case '-': resultado = a - b
    case _:   resultado = 0    # default

# while
while condicao:
    ...

# for — itera sobre qualquer iterável (não é o for de C)
for i in range(10):       # range(n) → 0..n-1
    ...

for item in lista:        # equivale ao for com índice em C
    ...

for i, item in enumerate(lista):  # índice + valor simultaneamente

# break / continue / else em laços (único em Python)
for i in range(10):
    if i == 5: break
else:                     # executado se o laço terminou SEM break
    print("completo")
```

### 🔬 Exercício 5a — if/elif/else

```python
nota = 72

if   nota >= 90: print("A")
elif nota >= 80: print("B")
elif nota >= 70: print("C")
else:            print("Reprovado")
```

---

### 🔬 Exercício 5b — for com break, continue e cláusula else

```python
for i in range(10):
    if i % 2 == 0:
        continue        # pula pares
    if i == 7:
        break           # para no 7
    print(i)
else:
    print("laço completo sem break")  # NÃO impresso (houve break)

# equivalente ao while de C com contador
n = 1
while n < 32:
    print(n)
    n *= 2
```

**O que observar:** a cláusula `else` do `for` — conceito sem equivalente em C.

---

### 🔬 Exercício 5c — match/case (Python 3.10+)

```python
dia = 3   # 1=Seg ... 7=Dom

match dia:
    case 1 | 2 | 3 | 4 | 5:
        print("Dia útil")
    case 6 | 7:
        print("Fim de semana")
    case _:
        print("Inválido")
```

> ⚠ `match` não tem *fall-through* — em C, esquecer `break` no `switch`
> cai para o próximo case. Em Python, isso não acontece.

---

## 6. Funções

**Em C:** funções têm tipo de retorno declarado, passagem por valor por padrão,
e por referência via ponteiro explícito.

**Em Python:** funções são **objetos de primeira classe** (podem ser passadas
como argumentos, armazenadas em variáveis). Não há declaração de tipo obrigatória.
Tudo é passado **por referência de objeto** (*pass-by-object-reference*).

```python
# definição simples
def soma(a, b):
    return a + b

# parâmetros com valor padrão
def saudacao(nome, prefixo="Olá"):
    return f"{prefixo}, {nome}!"

# múltiplos retornos (na verdade uma tupla)
def divide(a, b):
    return a // b, a % b   # quociente e resto

q, r = divide(17, 5)

# funções como objetos
def aplicar(func, x):
    return func(x)

aplicar(abs, -5)   # 5 — função passada como argumento

# lambda (função anônima)
quadrado = lambda x: x * x
```

### 🔬 Exercício 6a — Passagem por objeto-referência: mutável vs. imutável

```python
# imutável: int — comportamento parece "por valor" (como C)
def dobra_int(x):
    x *= 2       # x religar para novo int — original não muda
    print("dentro:", x)

v = 7
dobra_int(v)
print("fora:", v)   # ainda 7!

# mutável: lista — comportamento parece "por referência" (como ponteiro C)
def dobra_lista(lst):
    for i in range(len(lst)):
        lst[i] *= 2   # modifica o objeto existente

nums = [1, 2, 3]
dobra_lista(nums)
print(nums)   # [2, 4, 6] — alterado!
```

**O que observar:** é a **mutabilidade do objeto**, não a linguagem, que determina
se o chamador vê a mudança. Com `int` (imutável), `x *= 2` cria novo objeto —
a seta dentro da função muda, mas a seta do chamador não. Com lista (mutável),
`lst[i] *= 2` modifica o objeto compartilhado.

---

### 🔬 Exercício 6b — Recursão e pilha de chamadas

```python
def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))   # 120
```

**O que observar:** frames de `fatorial` empilhando exatamente como em C —
o PythonTutor mostra cada frame com seu `n` local.

---

## 7. Listas (equivalente de arrays)

**Em C:** array tem tamanho fixo, tipo homogêneo, armazenamento contíguo na stack
(ou heap se alocado com `malloc`).

**Em Python:** `list` é dinâmica (redimensiona), heterogênea, sempre no heap.
Internamente é um array de *ponteiros* para objetos.

```python
# criação
v = [10, 20, 30, 40, 50]   # equivale a int v[5] = {10,20,30,40,50}
m = [[1,2,3],[4,5,6]]      # lista de listas — equivale a int m[2][3]

# acesso
v[0]        # 10
v[-1]       # 50  (índice negativo — sem equivalente direto em C)
m[1][2]     # 6

# fatia (slice) — sem equivalente direto em C
v[1:3]      # [20, 30]   — cópia dos elementos 1 e 2
v[::-1]     # [50,40,30,20,10] — invertido

# operações dinâmicas
v.append(60)    # equivale a realloc + inserção
v.pop()         # remove e retorna último elemento
len(v)          # comprimento (equivale a sizeof(v)/sizeof(v[0]) em C)
```

> **Diferença de memória:** em C, `int v[5]` são 20 bytes contíguos na stack.
> Em Python, `v = [10,20,30]` é um objeto lista no heap contendo 3 ponteiros
> para objetos `int` também no heap — muito mais indireção.

### 🔬 Exercício 7 — Lista dinâmica e aliasing

```python
v = [10, 20, 30, 40, 50]

soma = 0
for x in v:
    soma += x
print("soma =", soma)   # 150

# aliasing (equivale a dois ponteiros C para o mesmo bloco)
a = [1, 2, 3]
b = a            # mesma lista!
b.append(99)
print(a)         # [1, 2, 3, 99]

# cópia rasa — objetos distintos
c = a.copy()     # ou a[:]
c.append(0)
print(a)         # [1, 2, 3, 99] — não afetado
```

**O que observar:** `b = a` faz duas etiquetas na mesma lista — setas iguais
no PythonTutor. `a.copy()` cria um novo objeto lista com seta separada.

---

## 8. Strings

**Em C:** string é `char[]` terminado por `'\0'`, mutável.

**Em Python:** `str` é um objeto **imutável** de caracteres Unicode. Não há
`'\0'` explícito. Funções de `<string.h>` viram métodos de objeto.

```python
s = "Brasilia"

len(s)             # 8  — equivale a strlen()
s + " - DF"        # concatenação — cria novo objeto (equivale a strcat em novo buffer)
s[0]               # 'B'
s[2:5]             # 'asi' — fatiamento
s.upper()          # 'BRASILIA'
s.lower()          # 'brasilia'
s.replace("a","@") # 'Br@sili@'
s.split("i")       # ['Brasil', 'a']
"ili" in s         # True — equivale a strstr() != NULL
s == "Brasilia"    # True — equivale a strcmp() == 0

# f-string (Python 3.6+) — equivale a snprintf
nome = "mundo"
msg = f"Ola, {nome}! len={len(nome)}"
```

> **Imutabilidade:** `s[0] = 'b'` levanta `TypeError`. Para strings mutáveis,
> use `bytearray` (equivalente mais próximo de `char[]` mutável em C).

### 🔬 Exercício 8 — Imutabilidade e iteração

```python
s = "Brasilia"
print(f"Comprimento: {len(s)}")

for i, c in enumerate(s):
    print(f"s[{i}] = '{c}'  (ord={ord(c)})")   # ord() ≡ valor ASCII

# comparação — equivale a strcmp
t = "Brasilia"
print(s == t)        # True
print(s is t)        # pode ser True (interning) ou False

# tentativa de mutação
try:
    s[0] = 'b'       # TypeError!
except TypeError as e:
    print("Erro:", e)
```

**O que observar:** `ord(c)` equivale ao valor numérico do `char` em C.
A tentativa de mutação levanta exceção — em C, `char *p = "hello"; p[0]='H'`
causa *undefined behavior* (segfault em muitas plataformas).

---

## 9. Referências (equivalente de ponteiros)

**Em C:** ponteiros são endereços numéricos explícitos, aritmética de ponteiros,
derreferência com `*`.

**Em Python:** não há ponteiros explícitos. Toda variável *é* uma referência.
`id()` expõe o endereço real; `is` compara identidade.

```python
# Não há &x nem *p em Python.
# "Ponteiro" é implícito — toda atribuição é por referência de objeto.

x = [1, 2, 3]
p = x          # p "aponta para" o mesmo objeto que x
p.append(4)
print(x)       # [1, 2, 3, 4] — equivale a modificar via ponteiro em C

# id() — equivale ao endereço (%p em printf)
print(id(x))
print(id(p))   # mesmo valor: p e x referenciam o mesmo objeto

# "ponteiro nulo" → None
p = None
```

> **Aritmética de ponteiros** não existe em Python. Iterar sobre elementos
> usa `for item in lista` — o interpretador gerencia os índices internamente.

### 🔬 Exercício 9 — Referências, identidade e cópia profunda

```python
import copy

# cópia rasa (shallow copy) — equivale a copiar array de ponteiros, não o conteúdo
original = [[1, 2], [3, 4]]
rasa = original.copy()
rasa[0].append(99)
print(original)    # [[1, 2, 99], [3, 4]] — sublista compartilhada!

# cópia profunda (deep copy) — equivale a duplicar toda a estrutura heap
original2 = [[1, 2], [3, 4]]
profunda = copy.deepcopy(original2)
profunda[0].append(99)
print(original2)   # [[1, 2], [3, 4]] — intacto
```

**O que observar:** `rasa = original.copy()` cria nova lista mas os elementos
(sublistas) são **compartilhados** — duas setas externas separadas, mas setas
internas convergindo para os mesmos objetos. `deepcopy` duplica toda a árvore.

---

## 10. Gerenciamento de memória (equivalente de malloc/free)

**Em C:** o programador chama `malloc`/`free` explicitamente. Vazamento de memória
(*memory leak*) e acesso após `free` (*use-after-free*) são responsabilidade do
programador.

**Em Python:** o **Garbage Collector** libera memória automaticamente via
*contagem de referências* + GC cíclico. Não há `malloc`/`free` explícitos.

```python
# "malloc" implícito — criação de objeto
v = list(range(1000))    # aloca lista de 1000 ints no heap

# "realloc" implícito — lista cresce automaticamente
v.append(1001)           # Python gerencia o realloc internamente

# "free" implícito — quando a última referência some, o GC libera
v = None                 # objeto lista perde a última referência → elegível para GC
del v                    # remove o nome do escopo (pode acelerar a coleta)
```

> **Gerador vs. lista:** para processar grandes volumes de dados sem alocar tudo
> na memória de uma vez (equivalente a ler um arquivo em chunks em C):

```python
# lista — aloca todos os elementos de uma vez (como malloc do tamanho total)
quadrados = [x**2 for x in range(10**6)]

# gerador — produz um elemento por vez (como ler arquivo em C em loop)
gen = (x**2 for x in range(10**6))
next(gen)   # produz 0
next(gen)   # produz 1
```

### 🔬 Exercício 10 — Ciclo de vida de objetos no heap

```python
a = [10, 20, 30]
b = a              # contagem de referências de [10,20,30] = 2
print(id(a), id(b))

b = None           # contagem cai para 1; objeto ainda vivo
print(a)           # [10, 20, 30]

a = None           # contagem cai para 0; GC pode coletar
# objeto [10,20,30] não é mais acessível

c = [1, 2]
del c              # equivale a c = None + remove nome do escopo
```

**O que observar:** no PythonTutor, quando `b = None` a seta de `b` some mas o
objeto lista ainda existe (seta de `a` presente). Quando `a = None`, o objeto
desaparece do diagrama — GC o coletou.

---

## 11. Classes (equivalente de structs)

**Em C:** `struct` agrupa campos de tipos diferentes em um bloco de memória
contíguo. Sem métodos, sem herança.

**Em Python:** `class` agrupa dados *e* comportamento. Objetos vivem no heap;
`self` é equivalente ao ponteiro `this` implícito.

```python
# equivalente direto de struct Ponto { int x; int y; };
class Ponto:
    def __init__(self, x, y):  # equivale ao construtor
        self.x = x             # self ≡ ponteiro para o struct
        self.y = y

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

p = Ponto(3, 4)
print(p.x)         # 3  — equivale a p.x em C

# acesso via referência — equivale a pp->x em C
ptr = p            # ptr e p referenciam o mesmo objeto
ptr.x = 10
print(p.x)         # 10 — mesma semântica de pp->x = 10 em C
```

**Alternativas mais próximas de `struct` (sem métodos extras):**

```python
from dataclasses import dataclass

@dataclass
class Ponto:
    x: int
    y: int

p = Ponto(3, 4)
print(p)   # Ponto(x=3, y=4)

# ou namedtuple — imutável (equivale a struct const)
from collections import namedtuple
Ponto = namedtuple("Ponto", ["x", "y"])
p = Ponto(3, 4)
```

> **Sem `union`:** Python não tem `union`. O mais próximo é usar um campo com
> valor que pode ser de tipos diferentes (tipagem dinâmica cobre o caso de uso).

### 🔬 Exercício 11 — Classe com método e referência compartilhada

```python
class Complexo:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def modulo_sq(self):       # equivale a função que recebe struct* em C
        return self.re**2 + self.im**2

    def __repr__(self):
        return f"{self.re} + {self.im}i"

c1 = Complexo(3.0, 4.0)
c2 = c1              # c2 é outra referência para o MESMO objeto
c2.re = 0.0
print(c1)            # 0.0 + 4.0i — c1 vê a mudança (mesma semântica de pp->re=0)
print(c1.modulo_sq())
```

**O que observar:** `c1` e `c2` aparecem como setas para o mesmo objeto no heap
— idêntico ao comportamento de `struct Complexo *c2 = c1` em C.

---

## 12. Enums

**Em C:** `enum` é açúcar sintático sobre `int`.

**Em Python:** `enum.Enum` é uma classe real; membros têm nome e valor separados.

```python
from enum import Enum, auto

class DiaSemana(Enum):
    DOM = 0
    SEG = auto()   # auto() atribui valor automaticamente (1, 2, ...)
    TER = auto()
    QUA = auto()
    QUI = auto()
    SEX = auto()
    SAB = auto()

hoje = DiaSemana.TER
print(hoje)          # DiaSemana.TER
print(hoje.value)    # 2
print(hoje.name)     # TER

# iteração — não possível em C sem truques
for d in DiaSemana:
    print(d.value, d.name)
```

### 🔬 Exercício 12 — Enum com match/case

```python
from enum import Enum

class DiaSemana(Enum):
    DOM=0; SEG=1; TER=2; QUA=3; QUI=4; SEX=5; SAB=6

def tipo_dia(d):
    match d:
        case DiaSemana.SAB | DiaSemana.DOM:
            return "Fim de semana"
        case _:
            return "Dia útil"

for d in DiaSemana:
    print(f"{d.name}: {tipo_dia(d)}")
```

**O que observar:** em C, `enum` vira `int` silenciosamente. Em Python,
`DiaSemana.TER == 2` é `False` (são tipos diferentes) — use `.value` para
comparar com inteiros.

---

## 13. Entrada / Saída básica

**Em C:** `printf`/`scanf` com especificadores de formato.

**Em Python:** `print()` com f-strings ou `.format()`; `input()` sempre retorna
`str` (requer conversão explícita).

```python
# saída formatada
x = 255
f_val = 3.14159
print(f"Decimal:     {x}")
print(f"Hexadecimal: {x:#x}")       # equivale a %x → 0xff
print(f"Float 2dec:  {f_val:.2f}")  # equivale a %.2f
print(f"Padding:     {x:08d}")      # equivale a %08d

# entrada — equivale a scanf, mas sempre retorna str
entrada = input("Digite um número: ")
n = int(entrada)    # conversão explícita — equivale ao %d do scanf
f2 = float(input("Digite um float: "))

# print para stderr (equivale a fprintf(stderr, ...))
import sys
print("erro!", file=sys.stderr)
```

> **Diferença de segurança:** `scanf("%s", buf)` em C não limita o tamanho —
> clássico buffer overflow. `input()` em Python retorna uma `str` Python sem
> limite de tamanho e sem risco de overflow.

### 🔬 Exercício 13 — Formatação sem entrada interativa

```python
i    = 255
f    = 3.14159
c    = 'Z'
s    = "Brasilia"

print(f"Decimal:     {i}")
print(f"Hexadecimal: {i:x}")     # ff
print(f"Float 2dec:  {f:.2f}")
print(f"Char:        {c}")
print(f"String:      {s}")
print(f"Endereco:    {id(s)}")   # equivale a %p
print(f"Unicode ord: {ord(c)}")  # equivale ao valor ASCII do char
```

---

## 14. Módulos (equivalente do pré-processador)

**Em C:** `#include` inclui declarações; `#define` cria macros/constantes;
processado *antes* da compilação.

**Em Python:** `import` carrega módulos em *tempo de execução*. Não há macros —
funções são usadas em vez delas. Constantes são convenção (MAIÚSCULAS).

```python
# equivale a #include <math.h>
import math
print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0

# equivale a #include <stdio.h> (seletivo)
from math import pi, sqrt, factorial

# equivale a #define PI 3.14159
PI = 3.14159             # convenção — não imposta

# equivale a #define MAX(a,b) (...)
# em Python: use função normal (sem risco de efeito colateral de macro)
def MAX(a, b):
    return a if a > b else b

# equivale a #ifdef DEBUG
import os
DEBUG = os.getenv("DEBUG", "0") == "1"
if DEBUG:
    print(f"debug: x={PI}")
```

### 🔬 Exercício 14 — Módulo math vs. macro C

```python
import math

PI     = math.pi
R      = 5.0

area   = PI * R ** 2
print(f"Área do círculo r=5: {area:.2f}")

def quadrado(x):
    return x * x

print(f"quadrado(7+1) = {quadrado(7+1)}")   # 64 — sem armadilha de macro

# math.factorial() — equivale a implementar fatorial em C
print(f"10! = {math.factorial(10)}")
```

**O que observar:** `quadrado(7+1)` avalia `7+1=8` *antes* de passar — sem o
problema da macro C `QUADRADO(a+1)` que expande para `(a+1)*(a+1)`.

---

## 15. Escopo e duração (regra LEGB)

**Em C:** escopo de bloco `{}`; `static` persiste; `extern` compartilha entre .c.

**Em Python:** escopo segue a regra **LEGB** — Local → Enclosing → Global → Built-in.
Não há escopo de bloco `if`/`for`/`while` (diferente de C!).

```
L — Local:     variáveis definidas na função atual
E — Enclosing: funções externas (closures)
G — Global:    nível de módulo
B — Built-in:  nomes internos do Python (len, print, etc.)
```

```python
x = "global"        # G

def externa():
    x = "enclosing" # E para interna()

    def interna():
        x = "local" # L — sombra as externas
        print(x)    # "local"

    interna()
    print(x)        # "enclosing"

externa()
print(x)            # "global"
```

> ⚠ **Armadilha sem equivalente em C:** variáveis de laço `for` e blocos `if`
> **não** criam novo escopo em Python — `i` existe após o `for`!

```python
for i in range(5):
    pass
print(i)   # 4 — i ainda existe! Em C, i seria local ao for {}
```

### 🔬 Exercício 15a — LEGB e nonlocal (equivalente de static local em C)

```python
def make_contador():
    n = 0                  # variável no escopo enclosing (persiste!)

    def contador():
        nonlocal n         # declara que n é do escopo enclosing (≡ static local)
        n += 1
        print(f"chamada número {n}")

    return contador

c = make_contador()
c()   # 1
c()   # 2
c()   # 3
```

**O que observar:** `n` vive no frame de `make_contador` no heap (closure),
não é recriado a cada chamada de `contador` — exatamente como `static int n`
em C. O PythonTutor mostra `n` no frame da função externa.

---

### 🔬 Exercício 15b — global vs. local

```python
contador = 0           # variável global

def incrementa():
    global contador    # sem isso, Python criaria local 'contador'
    contador += 1

incrementa()
incrementa()
incrementa()
print(contador)        # 3
```

---

## 16. Boas práticas (equivalentes Python)

| Boa prática em C | Equivalente em Python |
|---|---|
| Inicialize todas as variáveis | Toda atribuição inicializa; leitura de nome inexistente → `NameError` |
| Prefira `strncpy` a `strcpy` | Use f-strings ou `str.format()` em vez de concatenação manual |
| Verifique retorno de `malloc` | Use `try/except MemoryError` (raro — Python gerencia) |
| Todo `malloc` tem `free` | Deixe o GC trabalhar; use `with` para recursos explícitos |
| Compile com `-Wall -Wextra` | Use `mypy` (tipos estáticos), `ruff`/`flake8` (linting) |
| Use `const` para imutabilidade | Use `tuple` (imutável), `Final` do `typing`, ou objetos `frozen` |

```python
# Equivalente de "verificar retorno de fopen"
try:
    with open("arq.txt", "r") as fp:  # with garante fclose() automático
        conteudo = fp.read()
except FileNotFoundError as e:
    print("Erro:", e)

# Equivalente de const / array imutável
DIAS = ("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab")  # tuple — imutável
# DIAS[0] = "X" → TypeError

# Equivalente de strncpy seguro — f-string com limite
nome = "Brasilia-DF-Centro"
truncado = f"{nome[:7]}"   # "Brasili"
```

### 🔬 Exercício 16 — with, tuple imutável e tratamento de exceção

```python
# tuple como array imutável (equivale a const int v[] em C)
PRIMOS = (2, 3, 5, 7, 11, 13)
print(PRIMOS[0])

try:
    PRIMOS[0] = 99    # TypeError — imutável
except TypeError as e:
    print("Imutável:", e)

# iteração segura sobre arquivo (sem fopen/fclose explícito)
# (PythonTutor não suporta I/O de arquivo — simulamos com lista)
linhas = ["linha 1\n", "linha 2\n", "linha 3\n"]
for linha in linhas:
    print(linha.strip())
```

**O que observar:** `tuple` aparece no PythonTutor como objeto imutável (sem
operações de mutação disponíveis). A exceção `TypeError` é capturada sem
encerrar o programa — ao contrário de um `segfault` em C.

---

## Resumo comparativo final

| Conceito C | Python | Diferença-chave |
|---|---|---|
| `int x = 10` | `x = 10` | Python: etiqueta→objeto; C: caixa com bytes |
| `int *p = &x` | `p = x` (objetos mutáveis) | Python: referência implícita |
| `*p = 20` | `p[0] = 20` (lista) | Python: sem derreferência explícita |
| `malloc` / `free` | automático (GC) | Python: sem gestão manual |
| `struct` | `class`, `@dataclass`, `namedtuple` | Python: dados + comportamento |
| `char[]` mutável | `bytearray` | `str` Python é imutável |
| `#include` | `import` | Em runtime, não pré-compilação |
| `#define MAX(a,b)` | função `def MAX(a,b)` | Sem armadilha de expansão textual |
| Escopo de bloco `{}` | Escopo de função (LEGB) | `for`/`if` não criam escopo em Python |
| `static` local | `nonlocal` + closure | Closure substitui variável estática local |
| `sizeof(int) = 4` | `sys.getsizeof(42) ≈ 28` | Objeto Python carrega metadados extras |

> **Por que `sys.getsizeof(42) ≈ 28` bytes e não 4?**
> Todo objeto Python carrega: contagem de referências (8 bytes), ponteiro para
> o tipo/classe (8 bytes), valor do inteiro (8 bytes) + overhead do alocador.
> Em C, `int` são exatamente os 4 bytes do valor — sem metadados.
