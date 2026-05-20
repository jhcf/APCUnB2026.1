# Exercícios em C — Operadores Aritméticos, Relacionais, Lógicos e Bit a Bit

> **Como usar:**
> 1. Leia o programa de cada grupo com atenção.
> 2. Responda todas as perguntas **no papel**, sem executar o código.
> 3. Cole o programa em <https://pythontutor.com/c.html> e avance passo a passo
>    para **verificar** suas respostas.
> 4. Anote o que errou e por quê.

---

## Grupo 1 — Operadores Aritméticos (`+` `-` `*` `/` `%` `++` `--`)

> **Regras fundamentais:**
> - `/` entre dois `int` faz **divisão inteira** — o resultado é truncado, não arredondado.
> - `%` (módulo) retorna o resto da divisão inteira.
> - `++x` incrementa *antes* de usar o valor; `x++` usa *depois*.
> - A ordem de avaliação de subexpressões dentro de uma mesma expressão pode ser
>   indefinida — nunca escreva `v[i] = i++` em código real.

### Programa-base

```c
#include <stdio.h>

int main(void) {
    int a = 17, b = 5;

    int r1 = a + b;        /* linha 5  */
    int r2 = a - b;        /* linha 6  */
    int r3 = a * b;        /* linha 7  */
    int r4 = a / b;        /* linha 8  — divisão inteira! */
    int r5 = a % b;        /* linha 9  */

    printf("r1=%d  r2=%d  r3=%d\n", r1, r2, r3);
    printf("r4=%d  r5=%d\n",         r4, r5);

    /* pré e pós incremento */
    int x = 10;
    int pre = ++x;         /* linha 14 */
    int pos = x++;         /* linha 15 */
    printf("pre=%d  pos=%d  x=%d\n", pre, pos, x);

    /* armadilha: misturar / e % com negativos */
    int neg = -17 / 5;     /* linha 19 */
    int rem = -17 % 5;     /* linha 20 */
    printf("neg=%d  rem=%d\n", neg, rem);

    return 0;
}
```

---

### Perguntas fechadas

**Q1.** Qual é o valor de `r4 = a / b` com `a=17` e `b=5`?

- ( ) a) 3.4
- ( ) b) 4
- ( ) **c) 3**
- ( ) d) 2

---

**Q2.** Qual é o valor de `r5 = a % b`?

- ( ) a) 0
- ( ) b) 3
- ( ) c) 2
- ( ) d) 5

> _Dica: `17 = 5×3 + ?`_

---

**Q3.** Após a linha 14 (`pre = ++x`) com `x=10` inicialmente, quais são
os valores de `pre` e `x` imediatamente após a atribuição?

- ( ) a) `pre=10`, `x=10`
- ( ) b) `pre=10`, `x=11`
- ( ) c) `pre=11`, `x=11`
- ( ) d) `pre=11`, `x=10`

---

**Q4.** Após a linha 15 (`pos = x++`) — atenção: `x` já é 11 neste ponto —
quais são os valores de `pos` e `x`?

- ( ) a) `pos=12`, `x=12`
- ( ) b) `pos=11`, `x=12`
- ( ) c) `pos=11`, `x=11`
- ( ) d) `pos=12`, `x=11`

---

**Q5.** Em C, `-17 / 5` e `-17 % 5` valem, respectivamente:

- ( ) a) `-4` e `3`
- ( ) b) `-3` e `2`
- ( ) c) `-3` e `-2`
- ( ) d) `-4` e `-3`

> _Em C99 e posteriores, a divisão trunca em direção ao zero._

---

### Perguntas abertas

**A1.** Sem executar, calcule manualmente e preencha a tabela para `a=23`, `b=4`.
Depois modifique o programa com esses valores e confira no PythonTutor.

| Expressão  | Seu resultado | PythonTutor |
|------------|:-------------:|:-----------:|
| `a / b`    |               |             |
| `a % b`    |               |             |
| `a * b`    |               |             |
| `a - b*5`  |               |             |

---

**A2.** O programa abaixo tem a intenção de verificar se um número é par.
Execute-o no PythonTutor com `n = 7` e `n = -4`. O resultado está correto
para números negativos? Explique por que `% 2` pode retornar `-1` em C e
reescreva a condição para funcionar corretamente com qualquer inteiro.

```c
#include <stdio.h>
int main(void) {
    int n = -4;
    if (n % 2 == 0)
        printf("%d é par\n", n);
    else
        printf("%d é ímpar\n", n);
    return 0;
}
```

---
---

## Grupo 2 — Operadores Relacionais (`==` `!=` `<` `>` `<=` `>=`)

> **Regras fundamentais:**
> - Toda expressão relacional retorna exatamente `0` ou `1` — um `int` comum.
> - `=` é atribuição; `==` é comparação. Confundi-los é o bug mais clássico de C.
> - Comparar `char` usa o valor numérico ASCII (`'A'`=65, `'a'`=97).

### Programa-base

```c
#include <stdio.h>

int main(void) {
    int a = 5, b = 10, c = 5;
    char x = 'A', y = 'a';       /* 'A'=65, 'a'=97 */

    int r1 = (a == c);            /* linha 6  */
    int r2 = (a == b);            /* linha 7  */
    int r3 = (a != b);            /* linha 8  */
    int r4 = (b > a);             /* linha 9  */
    int r5 = (a >= c);            /* linha 10 */
    int r6 = (x < y);             /* linha 11 */
    int r7 = (a + 3 == b - 2);   /* linha 12 */
    int r8 = (a = 99);            /* linha 13 — ARMADILHA */

    printf("r1=%d  r2=%d  r3=%d  r4=%d\n", r1, r2, r3, r4);
    printf("r5=%d  r6=%d  r7=%d\n",         r5, r6, r7);
    printf("r8=%d  a=%d\n",                  r8, a);
    return 0;
}
```

---

### Perguntas fechadas

**Q1.** Qual é o valor de `r1` após a linha 6?

- ( ) a) -1
- ( ) b) 0
- ( ) c) 1
- ( ) d) 5

---

**Q2.** Qual é o valor de `r6`? (`'A'`=65, `'a'`=97)

- ( ) a) 0 — letras maiúsculas são "maiores" semanticamente
- ( ) b) 1 — porque 65 < 97
- ( ) c) Erro de compilação — não se compara `char` com `<`
- ( ) d) -1

---

**Q3.** O que a linha 12 calcula? (`a=5`, `b=10`)

- ( ) a) `5+3` vs `10-2` → `8 == 8` → 0
- ( ) b) `8 == 8` → 1
- ( ) c) `5+3` vs `10` → `8 == 10` → 0
- ( ) d) Erro — não se usa `==` com expressões

---

**Q4.** A linha 13 tem `r8 = (a = 99)`. O que acontece?

- ( ) a) Erro de compilação
- ( ) b) `r8=0`, `a` não muda
- ( ) c) `r8=99`, `a=99` — `=` retorna o valor atribuído
- ( ) d) `r8=1`, `a=99`

---

**Q5.** Qual é a saída da primeira linha de `printf`?

- ( ) a) `r1=1  r2=1  r3=0  r4=1`
- ( ) b) `r1=1  r2=0  r3=1  r4=1`
- ( ) c) `r1=0  r2=0  r3=1  r4=1`
- ( ) d) `r1=1  r2=0  r3=0  r4=1`

---

### Perguntas abertas

**A1.** Antes de executar, preencha a tabela para `a=5`, `b=10`, `c=5`.
Verifique no PythonTutor.

| Expressão      | Seu resultado | PythonTutor |
|----------------|:-------------:|:-----------:|
| `a <= b`       |               |             |
| `b >= b`       |               |             |
| `c != a`       |               |             |
| `a + 5 != b`   |               |             |

---

**A2.** O trecho abaixo tem um bug clássico. Identifique-o e explique
o que acontece em C. Depois corrija e teste no PythonTutor com `nota=7`
e `nota=5`.

```c
#include <stdio.h>
int main(void) {
    int nota = 7;
    if (nota = 5)
        printf("nota é 5\n");
    else
        printf("nota não é 5\n");
    return 0;
}
```

_O que você esperava que imprimisse com `nota=7`? O que ele realmente imprime? Por quê?_

---
---

## Grupo 3 — Operadores Lógicos (`&&` `||` `!`)

> **Regras fundamentais:**
> - Qualquer valor **diferente de zero** é verdadeiro; **zero** é falso.
> - **Curto-circuito:** em `A && B`, se `A=0` o lado `B` não é avaliado.
>   Em `A || B`, se `A≠0` o lado `B` não é avaliado.
> - `!0 == 1`; `!n == 0` para qualquer `n ≠ 0`.
> - `!!n` normaliza qualquer valor para `0` ou `1`.

### Programa-base

```c
#include <stdio.h>

int avalia(char *nome, int val) {
    printf("  -> %s avaliado\n", nome);
    return val;
}

int main(void) {
    int a = 1, b = 0, c = 5;

    printf("=== AND ===\n");
    printf("a && b  = %d\n", a && b);
    printf("b && a  = %d\n", b && a);
    printf("a && c  = %d\n", a && c);

    printf("=== OR ===\n");
    printf("a || b  = %d\n", a || b);
    printf("b || b  = %d\n", b || b);
    printf("c || b  = %d\n", c || b);

    printf("=== NOT ===\n");
    printf("!a      = %d\n", !a);
    printf("!b      = %d\n", !b);
    printf("!c      = %d\n", !c);
    printf("!!c     = %d\n", !!c);

    printf("=== CURTO-CIRCUITO ===\n");
    printf("b && avalia(\"D\",1): %d\n", b && avalia("D", 1));
    printf("a || avalia(\"E\",1): %d\n", a || avalia("E", 1));
    printf("a && avalia(\"F\",0): %d\n", a && avalia("F", 0));
    printf("b || avalia(\"G\",1): %d\n", b || avalia("G", 1));

    return 0;
}
```

---

### Perguntas fechadas

**Q1.** Qual é o resultado de `a && c`? (`a=1`, `c=5`)

- ( ) a) 0 — `c` não é 1
- ( ) b) 5 — retorna o valor do lado direito
- ( ) c) 1 — ambos não-zero, resultado é sempre 0 ou 1
- ( ) d) Erro de compilação

---

**Q2.** Qual é o resultado de `!c` com `c=5`?

- ( ) a) -5
- ( ) b) 4
- ( ) c) 1
- ( ) d) 0 — `!` de qualquer não-zero é sempre 0

---

**Q3.** O que `!!c` produz com `c=5`?

- ( ) a) 0
- ( ) b) 1 — `!5=0`, depois `!0=1` (converte para "bool canônico")
- ( ) c) 5
- ( ) d) -1

---

**Q4.** A linha `b && avalia("D",1)` vai imprimir `-> D avaliado`?

- ( ) a) Não — `b=0` já torna `&&` falso; o lado direito é descartado
- ( ) b) Sim — C sempre avalia os dois lados de `&&`
- ( ) c) Depende do compilador
- ( ) d) Sim, mas `avalia` retorna 0

---

**Q5.** A linha `a || avalia("E",1)` vai imprimir `-> E avaliado`?

- ( ) a) Não — `a=1` já torna `||` verdadeiro; lado direito é descartado
- ( ) b) Sim — `||` sempre avalia os dois lados
- ( ) c) Não, porque `avalia` não é `_Bool`
- ( ) d) Sim, e o resultado total muda para 0

---

### Perguntas abertas

**A1.** Para a condição abaixo, determine para quais valores de `x` ela é
**verdadeira**. Preencha a tabela antes de executar; depois teste cada `x`
no PythonTutor trocando o valor literal.

```c
(x > 0) && (x % 2 == 0)
```

| `x`  | Esperado | PythonTutor |
|------|:--------:|:-----------:|
| -4   |          |             |
|  0   |          |             |
|  3   |          |             |
|  4   |          |             |
|  8   |          |             |

_O que essa condição verifica em linguagem natural?_

---

**A2.** Explique com suas palavras por que o curto-circuito pode ser
**útil** na prática. Depois complete e execute o programa abaixo;
o `printf` dentro de `seguro` deve aparecer somente quando `p != NULL`.
Troque `p = v` por `p = NULL` e veja o que muda.

```c
#include <stdio.h>

int seguro(int *p) {
    printf("  [acessando *p]\n");
    return *p > 0;
}

int main(void) {
    int v = 42;
    int *p = v;          /* corrija esta linha para p = &v */

    if (p != NULL && seguro(p))
        printf("valor positivo\n");
    else
        printf("ponteiro nulo ou valor <= 0\n");

    return 0;
}
```

---
---

## Grupo 4 — Operadores Bit a Bit (`&` `|` `^` `~` `<<` `>>`)

> **Regras fundamentais:**
> - Operam sobre os **bits individuais** do inteiro, não sobre seu valor booleano.
> - `&` (AND bit a bit) ≠ `&&` (AND lógico). Confundi-los é erro grave.
> - `<<` multiplica por potências de 2; `>>` divide (com ressalvas para negativos).
> - `~x` inverte todos os bits — em complemento de 2, `~x == -(x+1)`.
> - `^` (XOR) zera bits iguais e seta bits diferentes — útil para toggle.

### Programa-base

```c
#include <stdio.h>

/* imprime os 8 bits menos significativos de um int */
void bits8(const char *nome, int v) {
    printf("%s = %3d | ", nome, v);
    for (int i = 7; i >= 0; i--)
        printf("%d", (v >> i) & 1);
    printf("\n");
}

int main(void) {
    unsigned char a = 0b00111100;  /* 60  */
    unsigned char b = 0b00001111;  /* 15  */

    bits8("a      ", a);
    bits8("b      ", b);
    printf("---\n");
    bits8("a & b  ", a & b);   /* AND   */
    bits8("a | b  ", a | b);   /* OR    */
    bits8("a ^ b  ", a ^ b);   /* XOR   */
    bits8("~a     ", ~a & 0xFF);/* NOT (8 bits) */
    printf("---\n");
    bits8("a << 2 ", (a << 2) & 0xFF);   /* desloca esquerda */
    bits8("a >> 2 ", a >> 2);            /* desloca direita  */

    /* aplicações práticas */
    int flags = 0;
    flags |=  (1 << 3);   /* seta bit 3        */
    flags &= ~(1 << 3);   /* limpa bit 3       */
    flags ^=  (1 << 5);   /* toggle bit 5      */
    printf("flags  = %d\n", flags);

    return 0;
}
```

> **Lembre:** `a=60` em binário de 8 bits é `00111100`; `b=15` é `00001111`.
> Resolva bit a bit antes de executar.

---

### Perguntas fechadas

**Q1.** Qual é o resultado de `a & b`? (`a=00111100`, `b=00001111`)

- ( ) a) `01111111` = 127
- ( ) b) `00001100` = 12
- ( ) c) `00111111` = 63
- ( ) d) `00110011` = 51

> _AND: bit 1 somente onde AMBOS são 1._

---

**Q2.** Qual é o resultado de `a | b`?

- ( ) a) `00001100` = 12
- ( ) b) `00110011` = 51
- ( ) c) `00111111` = 63
- ( ) d) `01111111` = 127

> _OR: bit 1 onde PELO MENOS UM é 1._

---

**Q3.** Qual é o resultado de `a ^ b`?

- ( ) a) `00001100` = 12
- ( ) b) `00111111` = 63
- ( ) c) `00110011` = 51
- ( ) d) `11000011` = 195

> _XOR: bit 1 onde os bits são DIFERENTES._

---

**Q4.** O que `a << 2` faz com `a=60` (`00111100`)?

- ( ) a) Divide por 4 → 15
- ( ) b) Multiplica por 4 → 240 (descartando bits que saem pelo topo)
- ( ) c) Rotaciona 2 posições → 63
- ( ) d) Subtrai 2 → 58

> _Deslocar N posições à esquerda equivale a multiplicar por 2ᴺ._

---

**Q5.** A expressão `flags &= ~(1 << 3)` serve para:

- ( ) a) Setar (ligar) o bit 3 de `flags`
- ( ) b) Testar se o bit 3 está ligado
- ( ) c) Fazer toggle do bit 3
- ( ) d) Limpar (desligar) o bit 3 de `flags`

> _`~(1<<3)` cria uma máscara com todos os bits em 1 exceto o bit 3. O `&=` preserva
> os demais bits e força o bit 3 a 0._

---

### Perguntas abertas

**A1.** Preencha a tabela manualmente, depois confirme no PythonTutor.
Use `a=0b00111100` (60) e `b=0b00001111` (15).

| Expressão   | Binário (8 bits) | Decimal | PythonTutor |
|-------------|:----------------:|:-------:|:-----------:|
| `a & b`     |                  |         |             |
| `a \| b`    |                  |         |             |
| `a ^ b`     |                  |         |             |
| `a >> 2`    |                  |         |             |
| `~a & 0xFF` |                  |         |             |

---

**A2.** Escreva e execute no PythonTutor um programa que:

1. Declara `int x = 13` (`00001101`).
2. **Seta** o bit 1 (segundo bit da direita) usando `|`.
3. **Limpa** o bit 0 (bit menos significativo) usando `&` e `~`.
4. Faz **toggle** do bit 4 usando `^`.
5. Imprime o valor de `x` após cada operação, usando a função `bits8`
   do programa-base.

Preencha os valores esperados antes de executar:

| Passo | Operação          | Binário esperado | Decimal |
|-------|-------------------|:----------------:|:-------:|
| Inicial | `x = 13`        | `00001101`       | 13      |
| 1     | seta bit 1        |                  |         |
| 2     | limpa bit 0       |                  |         |
| 3     | toggle bit 4      |                  |         |

---
---

## Gabarito — Perguntas Fechadas

| Grupo | Q1 | Q2 | Q3 | Q4 | Q5 |
|-------|:--:|:--:|:--:|:--:|:--:|
| Aritméticos  | c | c | c | b | c |
| Relacionais  | c | b | b | c | b |
| Lógicos      | c | d | b | a | a |
| Bit a Bit    | b | c | c | b | d |

---

## Dicas para uso no PythonTutor

- **"Show all frames"** — veja todas as funções ativas na pilha ao mesmo tempo.
- **Avance linha por linha** com Next e observe como cada variável muda no painel direito.
- **Clique no valor** de uma variável no painel para destacar todas as referências a ela.
- Use o link **"Generate permanent link"** para salvar sua sessão e compartilhar com o professor.
- Para os exercícios de bit a bit, copie a função `bits8` do programa-base — ela
  facilita muito a visualização.
