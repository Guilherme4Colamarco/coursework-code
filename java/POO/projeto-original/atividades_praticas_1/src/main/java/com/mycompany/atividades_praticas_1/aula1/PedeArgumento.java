package com.mycompany.atividades_praticas_1.aula1;

public class PedeArgumento {
    public static void main(String[] args) {
        if (args.length > 0) {
            System.out.println("Argumento passado: " + args[0]);
        } else {
            System.out.println("Nenhum argumento foi passado.");
        }
    }
}
