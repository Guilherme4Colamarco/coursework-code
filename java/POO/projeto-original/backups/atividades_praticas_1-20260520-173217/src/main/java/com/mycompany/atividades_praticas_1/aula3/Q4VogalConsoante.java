package com.mycompany.atividades_praticas_1.aula3;
import java.util.Scanner;
public class Q4VogalConsoante { public static void main(String[] args){ char c=new Scanner(System.in).next().toLowerCase().charAt(0); System.out.println("aeiou".indexOf(c)>=0 ? "Vogal" : "Consoante"); } }
