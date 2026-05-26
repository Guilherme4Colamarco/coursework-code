package com.mycompany.atividades_praticas_1;

import java.util.Locale;
import java.util.Scanner;

/**
 * Q13: calcular o excesso de peso de peixes e a multa quando passar de 50 kg.
 */
public class Q13 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner inp = new Scanner(System.in);
        
        System.out.print("Digite o peso dos peixes (kg): ");
        double peso = inp.nextDouble();
        
        if (peso > 50) {
            double excesso = peso - 50;
            double multa = excesso * 4.0;
            System.out.println("Excesso: " + excesso + " kg");
            System.out.println("Multa: R$ " + String.format("%.2f", multa));
        } else {
            System.out.println("Não há excesso. Multa = R$ 0.00");
        }
    }
}
