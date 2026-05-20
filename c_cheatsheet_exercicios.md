# C Language — Cheatsheet com Exercícios (pythontutor.com)

> **Como usar:** acesse <https://pythontutor.com/c.html>, cole o código do exercício e clique em
> **"Visualize Execution"**. Use os botões **Next** e **Prev** para avançar passo a passo e
> observar o estado das variáveis, da pilha (*stack*) e do heap.

---

## 1. Estrutura de um programa

```c
#include <stdio.h>

int main(void) {
    // código
    return 0;        // 0 = sucesso
}
```

### 🔬 Exercício 1 — Olá, mundo com retorno

Cole e execute. Observe que `main` aparece na **pilha de chamadas** (*call stack*) e
desaparece quando `return 0` é executado.

```c
#include <stdio.h>

int main(void) {
    printf("Ola, mundo!\n");
    return 0;
}
```

**O que observar:** o frame de `main` na stack; o valor de retorno `0` ao final.

---

## 2. Tipos primitivos e tamanhos

| Tipo     | Tamanho típico | Exemplo literal |
|----------|----------------|-----------------|
| `char`   | 1 byte         | `'A'`, `'\n'`   |
| `int`    | 4 bytes        | `42`, `-7`      |
| `long`   | 4–8 bytes      | `100000L`       |
| `float`  | 4 bytes        | `3.14f`         |
| `double` | 8 bytes        | `3.14159`       |
| `_Bool`  | 1 byte         | `0` / `1`       |

Modificadores: `unsigned`, `signed`, `short`, `long`

### 🔬 Exercício 2 — Inspecionando tamanhos

```c
#include <stdio.h>

int main(void) {
    printf("char:   %zu byte(s)\n", sizeof(char));
    printf("int:    %zu byte(s)\n", sizeof(int));
    printf("long:   %zu byte(s)\n", sizeof(long));
    printf("float:  %zu byte(s)\n", sizeof(float));
    printf("double: %zu byte(s)\n", sizeof(double));
    return 0;
}
```

**O que observar:** os valores impressos confirmam a tabela acima.
Tente mudar `sizeof(int)` para `sizeof(short)` e compare.

---

## 3. Declaração e inicialização

```c
int x;           // declaração (valor indefinido!)
int y = 10;      // inicialização
const int N = 5; // constante (read-only)
```

### 🔬 Exercício 3 — Variável não inicializada vs. inicializada

```c
#include <stdio.h>

int main(void) {
    int a = 42;
    int b;          /* valor lixo — NÃO leia antes de atribuir */
    b = a + 8;
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    const int N = 100;
    /* N = 200; */  /* descomente para ver o erro de compilacao */
    printf("N = %d\n", N);
    return 0;
}
```

**O que observar:** o valor de `a` aparece imediatamente no frame; `b` só recebe valor
após a atribuição. Tente descomentar `N = 200` e veja o erro.

---

## 4. Operadores

```
Aritméticos:   +  -  *  /  %
Relacionais:   ==  !=  <  >  <=  >=
Lógicos:       &&  ||  !
Bit a bit:     &  |  ^  ~  <<  >>
Atribuição:    =  +=  -=  *=  /=  %=
Incremento:    ++x  x++  --x  x--
Ternário:      cond ? a : b
Sizeof:        sizeof(tipo)
```

### 🔬 Exercício 4 — Divisão inteira, módulo e incremento

```c
#include <stdio.h>

int main(void) {
    int a = 17, b = 5;

    printf("%d / %d = %d\n", a, b, a / b);  /* divisao inteira */
    printf("%d %% %d = %d\n", a, b, a % b); /* resto */

    int x = 3;
    int pre  = ++x;   /* x vira 4, pre  = 4 */
    int pos  = x++;   /* pos = 4, x  vira 5 */
    printf("pre=%d  pos=%d  x=%d\n", pre, pos, x);

    int max = (a > b) ? a : b;
    printf("max(%d,%d) = %d\n", a, b, max);
    return 0;
}
```

**O que observar:** diferença entre pré e pós-incremento no valor retornado; resultado
da divisão inteira vs. real.

---

## 5. Controle de fluxo

```c
if (x > 0) { ... } else if (x == 0) { ... } else { ... }

switch (op) { case '+': ...; break; default: break; }

while (cond) { ... }
do { ... } while (cond);
for (int i = 0; i < n; i++) { ... }
```

### 🔬 Exercício 5a — if / else if / else

```c
#include <stdio.h>

int main(void) {
    int nota = 72;

    if      (nota >= 90) printf("A\n");
    else if (nota >= 80) printf("B\n");
    else if (nota >= 70) printf("C\n");
    else                 printf("Reprovado\n");

    return 0;
}
```

**Variação:** troque `nota` por 55, 80 e 95; execute cada versão e acompanhe qual
ramo é percorrido.

---

### 🔬 Exercício 5b — for com break e continue

```c
#include <stdio.h>

int main(void) {
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0) continue; /* pula pares */
        if (i == 7)     break;    /* para no 7  */
        printf("%d\n", i);
    }
    return 0;
}
```

**O que observar:** o valor de `i` no frame a cada passo; quando `continue` pula a
impressão e quando `break` encerra o laço.

---

### 🔬 Exercício 5c — do-while

```c
#include <stdio.h>

int main(void) {
    int n = 1;
    do {
        printf("n = %d\n", n);
        n *= 2;
    } while (n < 32);
    return 0;
}
```

**O que observar:** o corpo executa *antes* do teste; `n` dobra a cada iteração
(potências de 2).

---

### 🔬 Exercício 5d — switch com fall-through

```c
#include <stdio.h>

int main(void) {
    int dia = 3;   /* 1=Seg ... 7=Dom */

    switch (dia) {
        case 1: case 2: case 3: case 4: case 5:
            printf("Dia util\n");
            break;
        case 6: case 7:
            printf("Fim de semana\n");
            break;
        default:
            printf("Invalido\n");
    }
    return 0;
}
```

**O que observar:** o *fall-through* intencional agrupa casos; remova um `break` para
ver o comportamento inesperado.

---

## 6. Funções

```c
int soma(int a, int b);          // protótipo

int soma(int a, int b) {         // definição
    return a + b;
}

void dobra(int *x) { *x *= 2; } // passagem por referência
dobra(&valor);
```

### 🔬 Exercício 6 — Pilha de chamadas em ação

```c
#include <stdio.h>

int fatorial(int n) {
    if (n <= 1) return 1;
    return n * fatorial(n - 1);  /* chamada recursiva */
}

void dobra(int *x) { *x *= 2; }

int main(void) {
    int f = fatorial(5);
    printf("5! = %d\n", f);

    int v = 7;
    dobra(&v);
    printf("dobro de 7 = %d\n", v);
    return 0;
}
```

**O que observar:** os frames de `fatorial` empilhando e desempilhando; como `dobra`
modifica `v` via ponteiro — o frame de `dobra` mostra `x` apontando para `v` em `main`.

---

## 7. Arrays

```c
int v[5];                         // 5 ints (índices 0–4)
int v[3] = {10, 20, 30};
int m[2][3] = {{1,2,3},{4,5,6}};  // matriz 2×3
v[0] = 42;
```

> ⚠ C não verifica limites em tempo de execução.

### 🔬 Exercício 7 — Array unidimensional e matriz

```c
#include <stdio.h>

int main(void) {
    int v[5] = {10, 20, 30, 40, 50};

    /* soma dos elementos */
    int soma = 0;
    for (int i = 0; i < 5; i++)
        soma += v[i];
    printf("soma = %d\n", soma);

    /* matriz 2x3 */
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printf("m[1][2] = %d\n", m[1][2]);  /* 6 */
    return 0;
}
```

**O que observar:** o PythonTutor mostra o array como células numeradas; acompanhe
`soma` acumulando a cada iteração.

---

## 8. Strings

```c
char s[] = "hello";      // 6 bytes: h e l l o \0
char *p  = "hello";      // ponteiro para literal (imutável)

strlen(s)        // comprimento sem '\0'
strcpy(dst, src) // cópia
strcmp(a, b)     // 0 se iguais
```

### 🔬 Exercício 8 — Percorrendo uma string caractere a caractere

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[] = "Brasilia";
    int  len = strlen(s);

    printf("Comprimento: %d\n", len);

    /* percorre e imprime cada char e seu codigo ASCII */
    for (int i = 0; i < len; i++)
        printf("s[%d] = '%c'  (ASCII %d)\n", i, s[i], s[i]);

    /* comparacao */
    char t[] = "Brasilia";
    printf("strcmp: %d\n", strcmp(s, t));  /* 0 = iguais */
    return 0;
}
```

**O que observar:** o array `s` no frame de `main` com cada byte; o `'\0'` invisível
no último índice (valor 0). Compare com `char *p = "Brasilia"` — o PythonTutor mostra
`p` como uma seta para fora do frame (memória estática).

---

## 9. Ponteiros

```c
int  x = 10;
int *p = &x;    // p guarda o endereço de x
*p = 20;        // derreferência: altera x via p

// Aritmética de ponteiros
int v[] = {1, 2, 3};
int *p = v;
p++;            // aponta para v[1]
```

### 🔬 Exercício 9a — Ponteiro básico e derreferência

```c
#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;

    printf("x    = %d\n",  x);
    printf("&x   = %p\n",  (void*)&x);
    printf("p    = %p\n",  (void*)p);
    printf("*p   = %d\n",  *p);

    *p = 99;
    printf("x apos *p=99: %d\n", x);
    return 0;
}
```

**O que observar:** no PythonTutor, `p` é exibido como uma **seta** apontando para a
caixa de `x`. Após `*p = 99`, a caixa de `x` muda de valor sem que `x` apareça no
lado esquerdo da atribuição.

---

### 🔬 Exercício 9b — Aritmética de ponteiros e equivalência com índice

```c
#include <stdio.h>

int main(void) {
    int v[4] = {10, 20, 30, 40};
    int *p = v;          /* p aponta para v[0] */

    printf("*p      = %d\n", *p);       /* 10 */
    printf("*(p+1)  = %d\n", *(p+1));  /* 20 */
    printf("*(p+2)  = %d\n", *(p+2));  /* 30 */

    p++;                 /* agora aponta para v[1] */
    printf("apos p++: *p = %d\n", *p); /* 20 */
    return 0;
}
```

**O que observar:** a seta de `p` se mover entre os elementos do array a cada `p++`.

---

### 🔬 Exercício 9c — Ponteiro para ponteiro

```c
#include <stdio.h>

int main(void) {
    int  x  = 42;
    int *p  = &x;
    int **pp = &p;

    printf("x   = %d\n",   x);
    printf("*p  = %d\n",  *p);
    printf("**pp= %d\n", **pp);

    **pp = 100;           /* altera x via dois níveis de indireção */
    printf("x apos **pp=100: %d\n", x);
    return 0;
}
```

**O que observar:** duas setas encadeadas — `pp → p → x`.

---

## 10. Alocação dinâmica

```c
#include <stdlib.h>

int *p = malloc(n * sizeof(int));
if (!p) { /* erro */ }

free(p);
p = NULL;
```

### 🔬 Exercício 10 — Heap vs. Stack

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 4;
    int *v = malloc(n * sizeof(int));  /* aloca no heap */

    for (int i = 0; i < n; i++)
        v[i] = (i + 1) * 10;          /* 10 20 30 40 */

    for (int i = 0; i < n; i++)
        printf("v[%d] = %d\n", i, v[i]);

    free(v);    /* devolve ao heap */
    v = NULL;   /* evita uso acidental */
    return 0;
}
```

**O que observar:** no PythonTutor, o bloco alocado aparece no painel **Heap** (lado
direito), separado do frame da stack. Após `free`, ele desaparece do heap.

---

## 11. Structs e Unions

```c
struct Ponto { int x; int y; };
struct Ponto p = {3, 4};
p.x = 10;

typedef struct { float re; float im; } Complexo;

struct Ponto *pp = &p;
pp->x = 5;   /* equivale a (*pp).x = 5 */

union Data { int i; float f; char c; };
```

### 🔬 Exercício 11a — Struct com acesso direto e via ponteiro

```c
#include <stdio.h>

typedef struct {
    int x;
    int y;
} Ponto;

float distancia(Ponto *a, Ponto *b) {
    int dx = a->x - b->x;
    int dy = a->y - b->y;
    /* evitamos sqrt para simplificar */
    return (float)(dx*dx + dy*dy);
}

int main(void) {
    Ponto origem = {0, 0};
    Ponto p      = {3, 4};

    printf("p.x=%d  p.y=%d\n", p.x, p.y);

    Ponto *ptr = &p;
    ptr->x = 10;
    printf("apos ptr->x=10: p.x=%d\n", p.x);

    printf("dist^2(origem,p) = %.0f\n", distancia(&origem, &p));
    return 0;
}
```

**O que observar:** `origem` e `p` como caixas compostas no frame; `ptr` como seta
para `p`; `->` equivalendo a `(*ptr).x`.

---

### 🔬 Exercício 11b — Union: membros compartilham memória

```c
#include <stdio.h>

union Dado {
    int   i;
    float f;
    char  c;
};

int main(void) {
    union Dado d;
    d.i = 65;
    printf("d.i = %d\n",   d.i);
    printf("d.c = '%c'\n", d.c);  /* mesmo bytes, interpretado como char */
    d.f = 3.14f;
    printf("d.f = %.2f\n", d.f);
    /* d.i agora tem valor indefinido (sobrescrito por f) */
    return 0;
}
```

**O que observar:** o PythonTutor mostra um único bloco de memória; escrever em `d.f`
sobrescreve o mesmo espaço de `d.i`.

---

## 12. Enums

```c
typedef enum { DOM=0, SEG, TER, QUA, QUI, SEX, SAB } DiaSemana;
DiaSemana hoje = TER;   /* vale 2 */
```

### 🔬 Exercício 12 — Enum com switch

```c
#include <stdio.h>

typedef enum { DOM=0, SEG, TER, QUA, QUI, SEX, SAB } DiaSemana;

const char *nome_dia(DiaSemana d) {
    switch (d) {
        case DOM: return "Domingo";
        case SEG: return "Segunda";
        case TER: return "Terca";
        case QUA: return "Quarta";
        case QUI: return "Quinta";
        case SEX: return "Sexta";
        case SAB: return "Sabado";
        default:  return "???";
    }
}

int main(void) {
    for (DiaSemana d = DOM; d <= SAB; d++)
        printf("%d = %s\n", d, nome_dia(d));
    return 0;
}
```

**O que observar:** enum é tratado como `int`; o laço `for` itera incrementando o
valor numérico subjacente.

---

## 13. Entrada / Saída básica

```c
printf("x = %d, f = %.2f\n", x, f);
scanf("%d %f", &x, &f);   // &: passa endereço!

// %d int   %ld long   %f float   %lf double
// %c char  %s string  %p ponteiro  %x hex
```

### 🔬 Exercício 13 — Formatação de saída (sem scanf no PythonTutor)

> ℹ️ O PythonTutor não suporta entrada interativa via `scanf`.
> Use valores literais para testar a formatação.

```c
#include <stdio.h>

int main(void) {
    int    i = 255;
    float  f = 3.14159f;
    char   c = 'Z';
    char   s[] = "Brasilia";

    printf("Decimal:     %d\n",   i);
    printf("Hexadecimal: %x\n",   i);   /* ff */
    printf("Float 2dec:  %.2f\n", f);
    printf("Char:        %c\n",   c);
    printf("String:      %s\n",   s);
    printf("Ponteiro:    %p\n",   (void*)s);
    return 0;
}
```

**O que observar:** como `%x` mostra 255 como `ff`; `%p` mostra o endereço de `s`.

---

## 14. Pré-processador

```c
#define PI  3.14159
#define MAX(a,b) ((a)>(b)?(a):(b))  // macro com parâmetros

#ifdef DEBUG
    printf("debug: x=%d\n", x);
#endif
```

### 🔬 Exercício 14 — Constante e macro com parâmetro

```c
#include <stdio.h>

#define PI        3.14159
#define QUADRADO(x) ((x)*(x))
#define MAX(a,b)  ((a)>(b)?(a):(b))

int main(void) {
    double r = 5.0;
    printf("Area do circulo r=5: %.2f\n", PI * QUADRADO(r));

    int a = 7, b = 3;
    printf("MAX(%d,%d) = %d\n", a, b, MAX(a,b));

    /* armadilha classica de macro sem parenteses */
    printf("QUADRADO(a+1) = %d\n", QUADRADO(a+1)); /* (a+1)*(a+1) = 64 */
    return 0;
}
```

**O que observar:** macros são substituição textual — o PythonTutor mostra o código
**após** a expansão do pré-processador. Tente `MAX(a++, b)` para ver o efeito colateral.

---

## 15. Escopo e duração

| Classe         | Declaração          | Duração       | Escopo       |
|----------------|---------------------|---------------|--------------|
| automática     | dentro da função    | bloco         | local        |
| `static` local | dentro da função    | todo programa | local        |
| `static` global| fora de funções     | todo programa | arquivo .c   |
| `extern`       | fora / referência   | todo programa | múltiplos .c |

### 🔬 Exercício 15a — Escopo de bloco

```c
#include <stdio.h>

int main(void) {
    int x = 1;
    printf("x externo = %d\n", x);

    {
        int x = 2;   /* nova variavel, esconde a externa */
        printf("x interno = %d\n", x);
    }

    printf("x externo apos bloco = %d\n", x);  /* ainda 1 */
    return 0;
}
```

**O que observar:** o `x` interno aparece no frame apenas enquanto o bloco `{}` está
ativo; ao sair, o frame volta a enxergar o `x` externo.

---

### 🔬 Exercício 15b — Variável `static` local (persiste entre chamadas)

```c
#include <stdio.h>

void contador(void) {
    static int n = 0;   /* inicializado UMA VEZ; persiste */
    n++;
    printf("chamada numero %d\n", n);
}

int main(void) {
    contador();  /* 1 */
    contador();  /* 2 */
    contador();  /* 3 */
    return 0;
}
```

**O que observar:** `n` não é recriado a cada chamada — o PythonTutor o mostra como
variável **global** (fora do frame), mesmo sendo declarado dentro da função.

---

## 16. Boas práticas resumidas

- Inicialize todas as variáveis antes de usar.
- Prefira `strncpy` / `snprintf` a `strcpy` / `sprintf`.
- Sempre verifique o retorno de `malloc` / `fopen`.
- Todo `malloc` deve ter um `free` correspondente.
- Compile com `-Wall -Wextra -fsanitize=address` durante o desenvolvimento.
- Use `const` sempre que um ponteiro/variável não deve ser modificado.

### 🔬 Exercício 16 — Detectando estouro de buffer (simulação segura)

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char destino[8];

    /* SEGURO: limita a copia ao tamanho do buffer */
    strncpy(destino, "Brasilia-DF", sizeof(destino) - 1);
    destino[sizeof(destino) - 1] = '\0';   /* garante terminador */

    printf("destino = '%s'\n", destino);
    printf("strlen  = %zu\n",  strlen(destino));
    return 0;
}
```

**O que observar:** `destino` tem 8 bytes; `strncpy` copia no máximo 7 caracteres +
`'\0'`. No PythonTutor, veja como o array é preenchido byte a byte e truncado.

---

> **Dica de uso no PythonTutor:**
> - Ative **"Show all frames"** para ver funções recursivas empilhando.
> - Ative **"Render memory"** → "Show in compact mode" para arrays grandes.
> - Use o link **"Generate permanent link"** para salvar e compartilhar um exercício.
