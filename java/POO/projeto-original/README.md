# Java — Organização de Estudos

Exercícios e testes práticos em Java para a disciplina de Programação Orientada a Objetos (POO), estruturados e organizados.

## Estrutura Geral do Diretório

O diretório está organizado da seguinte forma:

```
/home/geko/uniube/codigo/java/
├── README.md                      <- Esta documentação
│
├── atividades_praticas_1/         <- Projeto Maven principal consolidando todas as atividades
│   ├── src/main/java/com/...      <- Pacotes com resoluções organizadas por aula/tema
│   ├── testar_atividades.sh       <- Script para compilação e teste das atividades
│   └── RELATORIO-DISCO-POO.md     <- Relatório detalhado das resoluções das atividades
│
├── exemplos-disco-virtual/        <- Exemplos de código extraídos do disco virtual do professor
│   ├── programa1-classes-basicas/ <- Exemplos de classes e objetos simples divididos por exercício
│   ├── aula5-heranca/             <- Exemplos de herança divididos por exercício
│   ├── aula6-construtores/        <- Exemplos de construtores divididos por exercício
│   ├── projetos-netbeans/         <- Projetos NetBeans originais com arquivos do IDE
│   └── README.md                  <- Guia detalhado de compilação e execução dos exemplos
│
├── revisao/                       <- Pasta contendo rascunhos, revisões e scripts de testes avulsos
│   ├── print.java                 <- Exercício básico de revisão de saída no terminal
│   ├── Teste.java                 <- Teste rápido e simples de compilação e ambiente
│   └── usuario.java               <- Rascunho com classes avulsas (usuario, Obra, Exemplar)
│
└── backups/                       <- Backups e arquivos históricos
    ├── atividades_praticas_1-.../ <- Cópia de segurança de versão anterior
    └── arquivos-zip/              <- Arquivos compactados (.zip) centralizados para despoluir a raiz
```

---

## Como Executar

### 1. Atividades Práticas Principais (Projeto Maven)
O projeto principal em [atividades_praticas_1](file:///home/geko/uniube/codigo/java/atividades_praticas_1) possui um script para testar todas as soluções:
```bash
cd atividades_praticas_1
./testar_atividades.sh
```

### 2. Exemplos do Disco Virtual
Os códigos de exemplo foram divididos em pastas com suas respectivas classes `Principal.java`. Consulte o [README de exemplos](file:///home/geko/uniube/codigo/java/exemplos-disco-virtual/README.md) para ver como executá-los separadamente.

### 3. Scripts de Revisão Avulsos
Para rodar qualquer script na pasta [revisao](file:///home/geko/uniube/codigo/java/revisao):
```bash
cd revisao
javac <NomeDoArquivo>.java
java <NomeDaClasse>
```
