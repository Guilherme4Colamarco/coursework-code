package com.mycompany.atividades_praticas_1.aula2;
import java.util.Scanner;
public class Q13 { public static void main(String[] args){ Scanner in=new Scanner(System.in); System.out.print("Peso dos peixes (kg): "); double peso=in.nextDouble(); double excesso=Math.max(0,peso-50); double multa=excesso*4; System.out.printf("Excesso: %.2f kg%n", excesso); System.out.printf("Multa: R$ %.2f%n", multa); } }
