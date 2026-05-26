package com.mycompany.atividades_praticas_1.aula3;
import java.util.Scanner;
public class Q10Turno { public static void main(String[] args){ String t=new Scanner(System.in).next().toUpperCase(); System.out.println(t.equals("M")?"Bom Dia!":t.equals("V")?"Boa Tarde!":t.equals("N")?"Boa Noite!":"Valor Inválido!"); } }
