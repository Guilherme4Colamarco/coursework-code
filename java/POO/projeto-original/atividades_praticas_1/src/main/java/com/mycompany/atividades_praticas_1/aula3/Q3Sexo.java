package com.mycompany.atividades_praticas_1.aula3;
import java.util.Scanner;
public class Q3Sexo { public static void main(String[] args){ String s=new Scanner(System.in).next().toUpperCase(); System.out.println(s.equals("F")?"F - Feminino":s.equals("M")?"M - Masculino":"Sexo Inválido"); } }
