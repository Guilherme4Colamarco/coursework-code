/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula6;

/**
 *
 * @author roberto.dti
 */
public class Principal {
    public static void main(String[] args) {
        // Objeto da classe Carro
        Carro c1 = new Carro("Toyota", 2022);
        c1.mostrarInfo();

        // Objeto da classe Gerente
        Gerente g1 = new Gerente("Maria", 8000.0, "TI");
        g1.mostrarInfo();
    }
}

