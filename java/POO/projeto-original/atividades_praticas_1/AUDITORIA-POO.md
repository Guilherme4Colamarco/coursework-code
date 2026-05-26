# Relatório de Auditoria — Atividades de POO

## Atividades Auditadas

Os seguintes materiais do disco virtual (`/home/geko/uniube/poo-disco-extract`) foram auditados:
- `AtividadePooIdentificandoObjetosComSeusAtributosEM_otodos.pdf` (Modelagem Biblioteca)
- `JavaAula1.pdf` (Fundamentos e entrada de dados)
- `Javaaula2.pdf` (13 exercícios de fixação)
- `Java_aula3.pptx` (10 exercícios de lógica)
- `PooT3.pdf` (Classes Pessoa e Carro)
- `POO T 5.pdf` (Herança: Animais, Pagamentos, Veículos)
- `PooT6.pdf` (Construtores: Carro, Funcionário, Gerente)
- `Poot_1.pdf` (Material teórico, sem atividades práticas)
- Exemplos de arquivos RAR/ZIP (`Aula5.rar`, `Aula6.rar`, `Programacriacaoclasses.zip`) contendo demonstrações.

## Faltantes Encontradas / Implementadas

Durante a auditoria, foi identificada a seguinte atividade faltante:
- **`JavaAula1.pdf` (Página 18):** Programa para exemplificar a diferença entre `System.out.println` e `System.out.print`.

**Ações realizadas:**
- Implementado o arquivo `DiferencaPrintPrintln.java` no pacote `aula1`.
- Atualizado o script `testar_atividades.sh` para incluir a execução da nova atividade.

## Arquivos Alterados / Criados

- `src/main/java/com/mycompany/atividades_praticas_1/aula1/DiferencaPrintPrintln.java` (Criado)
- `testar_atividades.sh` (Alterado)
- `AUDITORIA-POO.md` (Criado)
- `RELATORIO-TESTES.txt` (Atualizado via script)

## Resultado dos Testes

O script de compilação e teste executou corretamente. Todas as atividades (incluindo as recentemente implementadas) foram validadas sem erros.
