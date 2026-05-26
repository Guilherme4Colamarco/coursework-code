/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula5;

/**
 *
 * @author roberto
 */
public class Principal {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // ------------------------
        // Exercício 1: Animais
        // ------------------------
        Animal a1 = new Animal();
        Cachorro dog = new Cachorro();
        Gato cat = new Gato();
        Vaca cow = new Vaca();

        System.out.println("=== Exercício 1: Animais ===");
        System.out.println("Som genérico: " + a1.somGenerico());
        System.out.println("Cachorro: " + dog.somDoCachorro());
        System.out.println("Gato: " + cat.somDoGato());
        System.out.println("Vaca: " + cow.somDaVaca());

        System.out.println();

        // ------------------------
        // Exercício 2: Pagamentos
        // ------------------------
        Gerente g1 = new Gerente(5000.0);
        Estagiario e1 = new Estagiario(2000.0);

        double pagamentoGerente = g1.pagamentoComoGerente();
        double pagamentoEstagiario = e1.pagamentoComoEstagiario();

        System.out.println("=== Exercício 2: Pagamentos ===");
        System.out.println("Salário base Gerente: " + g1.obterSalarioBase());
        System.out.println("Pagamento como Gerente: " + pagamentoGerente);

        System.out.println("Salário base Estagiário: " + e1.obterSalarioBase());
        System.out.println("Pagamento como Estagiário: " + pagamentoEstagiario);

        if (pagamentoGerente > pagamentoEstagiario) {
            System.out.println("O Gerente recebe mais.");
        } else if (pagamentoGerente < pagamentoEstagiario) {
            System.out.println("O Estagiário recebe mais.");
        } else {
            System.out.println("Ambos recebem o mesmo.");
        }

        System.out.println();

        // ------------------------
        // Exercício 3: Veículos
        // ------------------------
        Veiculo v1 = new Veiculo();
        Carro c1 = new Carro();
        Moto m1 = new Moto();

        System.out.println("=== Exercício 3: Veículos ===");
        System.out.println("Genérico: " + v1.acelerarGenerico());
        System.out.println("Carro: " + c1.acelerarCarro());
        System.out.println("Moto: " + m1.acelerarMoto());
    }

}
