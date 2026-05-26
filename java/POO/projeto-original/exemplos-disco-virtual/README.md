# Exemplos do Disco Virtual - Programação Orientada a Objetos (Organizados)

Exemplos de código Java extraídos dos arquivos compactados do Disco Virtual da disciplina de POO. Cada atividade e aula foi separada em pastas individuais, contendo seus próprios códigos-fonte e classes de teste (`Principal.java`).

## Estrutura de Atividades

### 1. `programa1-classes-basicas/` (Criação de classes e objetos simples)
- **`exercicio1-carro/`** — Exemplo com a classe `Carro` (métodos `ligar`, `acelerar`).
- **`exercicio2-pessoa/`** — Exemplo com a classe `Pessoa` (método `apresentar`).
- **`exercicio3-aluno/`** — Exemplo com a classe `Aluno` (método `media`).
- **`exercicio4-produto/`** — Exemplo com a classe `Produto` (método `mostrarPreco`).

### 2. `aula5-heranca/` (Conceito de herança e polimorfismo básico)
- **`exercicio1-animais/`** — Herança de som genérico para `Cachorro`, `Gato` e `Vaca`.
- **`exercicio2-pagamentos/`** — Herança de `Funcionario` para `Gerente` e `Estagiario`, calculando salários.
- **`exercicio3-veiculos/`** — Herança de `Veiculo` para `Carro` e `Moto`, alterando aceleração.

### 3. `aula6-construtores/` (Construtores e chamada de superconstrutores)
- **`exercicio1-carro/`** — Construtor customizado na classe `Carro`.
- **`exercicio2-funcionarios/`** — Construtor herdado com `super` na classe `Gerente`.

### 4. `projetos-netbeans/`
- Projetos originais do NetBeans completos (`Aula5`, `Aula6`, `programa1`), contendo os arquivos de configuração do IDE.

---

## Como Compilar e Executar

Para rodar qualquer um dos exercícios, navegue até a pasta correspondente e execute:

```bash
cd <pasta-do-exercicio>
javac *.java
java Principal
```

*Exemplo:*
```bash
cd aula5-heranca/exercicio1-animais
javac *.java
java Principal
```