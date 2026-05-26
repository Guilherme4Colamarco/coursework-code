package com.mycompany.atividades_praticas_1.aula3;
import java.util.Scanner;
public class Q5MediaAluno { public static void main(String[] args){ Scanner in=new Scanner(System.in); double m=(in.nextDouble()+in.nextDouble())/2; System.out.println(m==10?"Aprovado com Distinção":m>=7?"Aprovado":"Reprovado"); } }
