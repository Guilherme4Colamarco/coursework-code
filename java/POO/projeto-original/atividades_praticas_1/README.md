# Atividades Práticas — Programação Orientada a Objetos / Java

Projeto com as tarefas dos arquivos do Disco Virtual de POO.

## Fontes usadas

- `Javaaula2.pdf`: exercícios 1 a 13 de entrada, operadores e cálculos básicos.
- `Java_aula3.pptx`: exercícios de `if`, comparação, média, maior/menor, ordenação e turno.
- `PooT3.pdf`: classes, atributos, métodos e objetos (`Pessoa`, `Carro`).
- `POO T 5.pdf`: herança (`Animal`, `Funcionario`, `Veiculo` e subclasses).
- `PooT6.pdf`: construtores e herança com `super`.
- `AtividadePooIdentificandoObjetosComSeusAtributosEM_otodos.pdf`: modelagem de biblioteca universitária.
- Arquivos compactados `Aula5.rar`, `Aula6.rar` e `Programacriacaoclasses.zip` foram extraídos para conferência dos exemplos.

## Estrutura

- `src/main/java/com/mycompany/atividades_praticas_1/aula2/`
  - `Q1` a `Q13`.
- `src/main/java/com/mycompany/atividades_praticas_1/aula3/`
  - 10 exercícios de controle de fluxo.
- `src/main/java/com/mycompany/atividades_praticas_1/fixacao/`
  - `Pessoa`, `Carro`, `ProgramaFixacao`.
- `src/main/java/com/mycompany/atividades_praticas_1/heranca/`
  - exercícios de herança do `POO T 5.pdf`.
- `src/main/java/com/mycompany/atividades_praticas_1/construtores/`
  - exercícios de construtores do `PooT6.pdf`.
- `src/main/java/com/mycompany/atividades_praticas_1/biblioteca/`
  - modelagem da biblioteca universitária.

Também mantive as classes anteriores na raiz do pacote para compatibilidade com o envio antigo.

## Como compilar

```bash
javac -encoding UTF-8 -d build/classes $(find src/main/java -name '*.java')
```

## Como executar exemplos

```bash
java -cp build/classes com.mycompany.atividades_praticas_1.aula2.Q1
java -cp build/classes com.mycompany.atividades_praticas_1.aula3.Q10Turno
java -cp build/classes com.mycompany.atividades_praticas_1.fixacao.ProgramaFixacao
java -cp build/classes com.mycompany.atividades_praticas_1.heranca.ProgramaPrincipal
java -cp build/classes com.mycompany.atividades_praticas_1.construtores.ProgramaPrincipal
java -cp build/classes com.mycompany.atividades_praticas_1.biblioteca.ProgramaBiblioteca
```
