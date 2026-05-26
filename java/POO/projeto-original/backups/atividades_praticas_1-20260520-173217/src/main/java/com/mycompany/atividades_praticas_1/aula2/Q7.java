package com.mycompany.atividades_praticas_1.aula2;
import java.util.Scanner;
public class Q7 { public static void main(String[] args){ Scanner in=new Scanner(System.in); System.out.print("Ganho por hora: "); double valor=in.nextDouble(); System.out.print("Horas trabalhadas no mês: "); double horas=in.nextDouble(); System.out.printf("Salário do mês: R$ %.2f%n", valor*horas); } }
