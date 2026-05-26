package com.mycompany.atividades_praticas_1;

import java.util.Locale;
import java.util.Scanner;

/**
 * Q3: pedir as 4 notas bimestrais e mostrar a média final.
 */
public class Q3 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner inp = new Scanner(System.in);
        
        System.out.println("Digite as 4 notas bimestrais:");
        
        double n1 = inp.nextDouble();
        double n2 = inp.nextDouble();
        double n3 = inp.nextDouble();
        double n4 = inp.nextDouble();
        
        double media = (n1 + n2 + n3 + n4) / 4.0;
        
        System.out.println("Média final: " + media);
        
        if (media >= 7.0) {
            System.out.println("Aprovado!");
        } else if (media >= 5.0) {
            System.out.println("Recuperação");
        } else {
            System.out.println("Reprovado");
        }
    }
}
