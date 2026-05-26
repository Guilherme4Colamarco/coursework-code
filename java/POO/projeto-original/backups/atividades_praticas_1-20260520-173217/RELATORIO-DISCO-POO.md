# Relatório — Atividades dos arquivos do Disco Virtual de POO

## Status

Concluído localmente em `/home/geko/uniube/codigo/java/atividades_praticas_1`.

## Arquivos do Disco Virtual lidos

- `AtividadePooIdentificandoObjetosComSeusAtributosEM_otodos.pdf`
- `JavaAula1.pdf`
- `Javaaula2.pdf`
- `Java_aula3.pptx`
- `PooT3.pdf`
- `POO T 5.pdf`
- `PooT6.pdf`
- `Poot_1.pdf`
- Compactados conferidos: `Aula5.rar`, `Aula6.rar`, `Programacriacaoclasses.zip`

Textos extraídos em: `/home/geko/uniube/poo-disco-extract/`

## Tarefas implementadas

- `aula1/`: `PedeArgumento` (Exercício 1 — argumento via linha de comando) do `JavaAula1.pdf`.
- `aula1/`: `DiferencaPrintPrintln` (exemplo de diferença entre `System.out.print` e `System.out.println`) do `JavaAula1.pdf`.
- `aula2/`: Q1 a Q13 do `Javaaula2.pdf`.
- `aula3/`: 10 exercícios do `Java_aula3.pptx`.
- `fixacao/`: atividades de classe `Pessoa`, método `apresentar`, objeto `Pessoa`, classe `Carro` e dois objetos `Carro` do `PooT3.pdf`.
- `heranca/`: exercícios 1 a 4 do `POO T 5.pdf`.
- `construtores/`: atividades 1 a 3 do `PooT6.pdf`.
- `biblioteca/`: modelagem de biblioteca universitária do PDF de identificação de objetos/atributos/métodos.

## Auditoria

Relatório detalhado em `AUDITORIA-POO.md`.

Resultado da auditoria: após comparação dos materiais extraídos com o projeto, as faltantes localizadas foram implementadas.

## Verificação

Comandos executados:

```bash
rm -rf build/classes
mkdir -p build/classes
javac -encoding UTF-8 -d build/classes $(find src/main/java -name '*.java')
./testar_atividades.sh > RELATORIO-TESTES.txt
```

Resultado: compilação OK e smoke tests OK.

## Observação

O Maven não foi usado porque `mvn` não está instalado nesse ambiente. A validação foi feita diretamente com `javac` e `java`.
