package com.mycompany.atividades_praticas_1.aula2;
import java.util.Scanner;
public class Q10 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Primeiro inteiro: ");
        int a = in.nextInt();
        System.out.print("Segundo inteiro: ");
        int b = in.nextInt();
        System.out.print("Número real: ");
        double c = in.nextDouble();
        System.out.println("Produto do dobro do primeiro com metade do segundo: " + ((2 * a) * (b / 2.0)));
        System.out.println("Soma do triplo do primeiro com o terceiro: " + ((3 * a) + c));
        System.out.println("Terceiro elevado ao cubo: " + Math.pow(c, 3));
    }
}
