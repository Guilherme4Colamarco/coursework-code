package com.mycompany.atividades_praticas_1;

import java.util.Locale;
import java.util.Scanner;

/**
 * Q9: pedir a temperatura em graus Celsius e converter para graus Fahrenheit.
 */
public class Q9 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner inp = new Scanner(System.in);
        
        System.out.print("Digite a temperatura em Celsius: ");
        double celsius = inp.nextDouble();
        
        double fahrenheit = (celsius * 9/5) + 32;
        
        System.out.println(celsius + "°C = " + fahrenheit + "°F");
    }
}
