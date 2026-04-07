package com.mycompany.atividades_praticas_1;

import java.util.Scanner;

// Enunciado: pedir as 4 notas bimestrais e mostrar a média final.
public class Q3 {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);

        System.out.println("Digite F para Feminino ou M para Masculino:");
        String entrada = inp.nextLine().trim().toUpperCase();

        if (entrada.equals("F")) {
            System.out.println("F - Feminino");
        } else if (entrada.equals("M")) {
            System.out.println("M - Masculino");
        } else {
            System.out.println("Sexo Invalido");
        }
    }
}


