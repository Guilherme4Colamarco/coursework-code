package com.mycompany.atividades_praticas_1.aula3;
import java.util.Scanner;
public class Q8ProdutoMaisBarato { public static void main(String[] args){ Scanner in=new Scanner(System.in); double p1=in.nextDouble(),p2=in.nextDouble(),p3=in.nextDouble(); double menor=Math.min(p1,Math.min(p2,p3)); System.out.println("Compre o produto de R$ "+menor); } }
