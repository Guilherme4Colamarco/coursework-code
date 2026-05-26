/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package programa1;

import java.util.Scanner;

/**
 *
 * @author roberto
 */
public class Principal {

    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        Carro c1 = new Carro();
        Carro c2 = new Carro();
        Pessoa p1 = new Pessoa();
        Aluno a1 = new Aluno();
        Produto prod1 = new Produto();
        
        //Populando objeto carro c1
        System.out.print("Digite a cor do carro: ");
        c1.cor = ent.nextLine();
        System.out.print("Digite o modelo do carro: ");
        c1.modelo = ent.nextLine();
        System.out.print("Digite o ano do carro: ");
        c1.ano = ent.nextInt();

        c1.ligar();
        c1.acelerar();

        //Populando objeto carro c2
        System.out.print("Digite a cor do carro: ");
        ent.nextLine();
        c2.cor = ent.nextLine();
        System.out.print("Digite o modelo do carro: ");
        c2.modelo = ent.nextLine();
        System.out.print("Digite o ano do carro: ");
        c2.ano = ent.nextInt();

        c2.ligar();
        c2.acelerar();

        //popular objeto pessoa p1
        System.out.print("Digite o seu nome:");
        ent.nextLine();
        p1.nome = ent.nextLine();
        System.out.print("Digite a sua idade: ");
        p1.idade = ent.nextInt();

        System.out.println(p1.apresentar());

        //populando objeto Aluno a1
        System.out.print("Digite o nome do aluno: ");
        ent.nextLine();
        a1.nome = ent.nextLine();
        System.out.print("Digite a nota 1: ");
        a1.n1 = ent.nextDouble();
        System.out.print("Digite a nota 2: ");
        a1.n2 = ent.nextDouble();
        
        System.out.println("A média das notas é: " + a1.media());
        
        //Populando objeto Produto prod1
        System.out.print("Digite o nome do produto: ");
        ent.nextLine();
        prod1.nome = ent.nextLine();
        System.out.print("Digite o preço do produto: ");
        prod1.preco = ent.nextDouble();
        
        prod1.mostrarPreco();
    }

}
