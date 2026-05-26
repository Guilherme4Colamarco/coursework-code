/* Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license */

package com.mycompany.atividades_praticas_1;

import java.util.Scanner;

/**
 *
 * @author geko
 */
// Enunciado: pedir dois números ao usuário e mostrar a soma entre eles.
public class Q2 {

    public static void main(String[] args) {
      Scanner inp = new Scanner(System.in);

      int n1;
      int n2;
      int soma;

        System.out.println("digite o primeiro numero");
      n1 = inp.nextInt();


        System.out.println("digite o segundo numero");
      n2 = inp.nextInt();


      soma = n1 + n2;

      System.out.println("a soma é: " + soma);

    }
}
