package com.mycompany.atividades_praticas_1;

import java.util.Locale;
import java.util.Scanner;

/**
 * Q6: calcular a área de um quadrado e mostrar o dobro dessa área.
 */
public class Q6 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner inp = new Scanner(System.in);
        
        System.out.print("Digite o lado do quadrado: ");
        double lado = inp.nextDouble();
        
        double area = lado * lado;
        double dobro = area * 2;
        
        System.out.println("Área do quadrado: " + area);
        System.out.println("Dobro da área: " + dobro);
    }
}
