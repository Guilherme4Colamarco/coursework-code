/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula5;

/**
 *
 * @author roberto
 */
public class Gerente extends Funcionario {
    public Gerente(double salarioBase) {
        super(salarioBase);
    }

    public double pagamentoComoGerente() {
        return salarioBase * 1.2; // +20%
    }
}

