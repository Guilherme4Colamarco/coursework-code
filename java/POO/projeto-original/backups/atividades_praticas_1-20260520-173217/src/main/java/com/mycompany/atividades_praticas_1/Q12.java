package com.mycompany.atividades_praticas_1;

import java.util.Locale;
import java.util.Scanner;

/**
 * Q12: ler a altura e calcular o peso ideal usando fórmulas diferentes para homens e mulheres.
 */
public class Q12 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner inp = new Scanner(System.in);
        
        System.out.print("Digite a altura (em metros): ");
        double altura = inp.nextDouble();
        
        System.out.print("Digite o sexo (H para homem, M para mulher): ");
        String sexo = inp.next().toUpperCase();
        
        double pesoIdeal;
        if (sexo.equals("H")) {
            pesoIdeal = (72.7 * altura) - 58;
        } else {
            pesoIdeal = (62.1 * altura) - 44.7;
        }
        
        System.out.println("Peso ideal: " + String.format("%.2f", pesoIdeal) + " kg");
    }
}
