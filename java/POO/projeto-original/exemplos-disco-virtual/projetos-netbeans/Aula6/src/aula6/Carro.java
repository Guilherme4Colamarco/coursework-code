/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula6;

/**
 *
 * @author roberto
 */
public class Carro {
    private String marca;
    private int ano;

    // Construtor que inicializa os atributos
    public Carro(String marca, int ano) {
        this.marca = marca;
        this.ano = ano;
    }

    // Método para mostrar as informações
    public void mostrarInfo() {
        System.out.println("Carro { Marca: " + marca + ", Ano: " + ano + " }");
    }
}

