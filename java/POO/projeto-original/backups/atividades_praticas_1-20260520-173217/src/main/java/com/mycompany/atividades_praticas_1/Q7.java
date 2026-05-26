package com.mycompany.atividades_praticas_1;

import java.util.Locale;
import java.util.Scanner;

/**
 * Q7: ler o valor ganho por hora e as horas trabalhadas no mês, depois calcular o salário total.
 */
public class Q7 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner inp = new Scanner(System.in);
        
        System.out.print("Digite o valor ganho por hora: ");
        double valorHora = inp.nextDouble();
        
        System.out.print("Digite o número de horas trabalhadas no mês: ");
        double horas = inp.nextDouble();
        
        double salario = valorHora * horas;
        
        System.out.println("Salário total: R$ " + salario);
    }
}
