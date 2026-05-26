package com.mycompany.atividades_praticas_1.aula3;
import java.util.Arrays; import java.util.Scanner;
public class Q9OrdemDecrescente { public static void main(String[] args){ Scanner in=new Scanner(System.in); double[] v={in.nextDouble(),in.nextDouble(),in.nextDouble()}; Arrays.sort(v); System.out.println(v[2]+" "+v[1]+" "+v[0]); } }
