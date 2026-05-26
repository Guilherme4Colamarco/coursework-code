# C

Exercícios e pequenos programas em C focados em lógica, entrada de dados e estrutura de controle.

## Destaque

O arquivo mais forte desta pasta hoje é `atividade7_caixa_eletronico_multiplataforma.c`, porque ele mostra:

- menu em terminal
- operações básicas com estado
- validação de entrada
- adaptação para mais de um sistema operacional

## O que é vitrine e o que é estudo

- `atividade7_caixa_eletronico_multiplataforma.c` é a peça mais forte desta pasta
- `atividade7_caixa_eletronico.c` mostra a versão anterior, ainda útil para contexto
- os demais arquivos funcionam mais como base de estudo e prática de lógica

## Arquivos

### `atividade4.c`
- exercício simples de validação de entrada
- lê um número entre 1 e 130
- imprime contagem regressiva até zero

### `atividade7_caixa_eletronico.c`
- simulador de caixa eletrônico para ambiente Windows
- usa `conio.h`, `getch()` e `system("cls")`
- permite consultar saldo, depositar e sacar

### `atividade7_caixa_eletronico_multiplataforma.c`
- versão adaptada do caixa eletrônico para rodar em mais de um sistema
- troca `getch()` por pausa com `ENTER`
- usa limpeza de tela condicional para Windows e Unix-like
- é a melhor peça desta pasta para portfólio inicial

### `pgr.c`
- exercício básico com nome, cidade e idade
- mostra mensagem diferente para maior e menor de idade

## Leitura da pasta

Esta pasta deve ser lida como vitrine de fundamentos em C, não como coleção de sistemas complexos. O valor aqui está em mostrar base, prática constante e evolução de raciocínio.

## Como compilar

Exemplo com `gcc`:

```bash
gcc atividade4.c -o atividade4
./atividade4
```

Para a versão multiplataforma:

```bash
gcc atividade7_caixa_eletronico_multiplataforma.c -o caixa
./caixa
```
