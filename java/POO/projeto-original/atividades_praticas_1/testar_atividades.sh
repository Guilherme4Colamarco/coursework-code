#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
CP="build/classes"
run() { printf "\n### $1\n"; shift; "$@"; }
run_input() { local title="$1" input="$2" class="$3"; printf "\n### $title\n"; printf '%b' "$input" | java -cp "$CP" "$class"; }

run "aula1.PedeArgumento (com argumento)" java -cp "$CP" com.mycompany.atividades_praticas_1.aula1.PedeArgumento "Teste"
run "aula1.PedeArgumento (sem argumento)" java -cp "$CP" com.mycompany.atividades_praticas_1.aula1.PedeArgumento
run "aula1.DiferencaPrintPrintln" java -cp "$CP" com.mycompany.atividades_praticas_1.aula1.DiferencaPrintPrintln

run_input "aula2.Q1" '5\n' com.mycompany.atividades_praticas_1.aula2.Q1
run_input "aula2.Q2" '2\n3\n' com.mycompany.atividades_praticas_1.aula2.Q2
run_input "aula2.Q3" '7\n8\n9\n10\n' com.mycompany.atividades_praticas_1.aula2.Q3
run_input "aula2.Q4" '1.5\n' com.mycompany.atividades_praticas_1.aula2.Q4
run_input "aula2.Q5" '2\n' com.mycompany.atividades_praticas_1.aula2.Q5
run_input "aula2.Q6" '4\n' com.mycompany.atividades_praticas_1.aula2.Q6
run_input "aula2.Q7" '20\n160\n' com.mycompany.atividades_praticas_1.aula2.Q7
run_input "aula2.Q8" '98.6\n' com.mycompany.atividades_praticas_1.aula2.Q8
run_input "aula2.Q9" '37\n' com.mycompany.atividades_praticas_1.aula2.Q9
run_input "aula2.Q10" '2\n4\n3.5\n' com.mycompany.atividades_praticas_1.aula2.Q10
run_input "aula2.Q11" '1.75\n' com.mycompany.atividades_praticas_1.aula2.Q11
run_input "aula2.Q12" '1.65\nM\n' com.mycompany.atividades_praticas_1.aula2.Q12
run_input "aula2.Q13" '55\n' com.mycompany.atividades_praticas_1.aula2.Q13

run_input "aula3.Q1MaiorDeDois" '4\n9\n' com.mycompany.atividades_praticas_1.aula3.Q1MaiorDeDois
run_input "aula3.Q2PositivoNegativo" '-1\n' com.mycompany.atividades_praticas_1.aula3.Q2PositivoNegativo
run_input "aula3.Q3Sexo" 'F\n' com.mycompany.atividades_praticas_1.aula3.Q3Sexo
run_input "aula3.Q4VogalConsoante" 'a\n' com.mycompany.atividades_praticas_1.aula3.Q4VogalConsoante
run_input "aula3.Q5MediaAluno" '10\n10\n' com.mycompany.atividades_praticas_1.aula3.Q5MediaAluno
run_input "aula3.Q6MaiorDeTres" '1\n5\n3\n' com.mycompany.atividades_praticas_1.aula3.Q6MaiorDeTres
run_input "aula3.Q7MaiorMenorDeTres" '1\n5\n3\n' com.mycompany.atividades_praticas_1.aula3.Q7MaiorMenorDeTres
run_input "aula3.Q8ProdutoMaisBarato" '10\n5\n7\n' com.mycompany.atividades_praticas_1.aula3.Q8ProdutoMaisBarato
run_input "aula3.Q9OrdemDecrescente" '1\n5\n3\n' com.mycompany.atividades_praticas_1.aula3.Q9OrdemDecrescente
run_input "aula3.Q10Turno" 'N\n' com.mycompany.atividades_praticas_1.aula3.Q10Turno

run "fixacao.ProgramaFixacao" java -cp "$CP" com.mycompany.atividades_praticas_1.fixacao.ProgramaFixacao
run "heranca.ProgramaPrincipal" java -cp "$CP" com.mycompany.atividades_praticas_1.heranca.ProgramaPrincipal
run "construtores.ProgramaPrincipal" java -cp "$CP" com.mycompany.atividades_praticas_1.construtores.ProgramaPrincipal
run "biblioteca.ProgramaBiblioteca" java -cp "$CP" com.mycompany.atividades_praticas_1.biblioteca.ProgramaBiblioteca
