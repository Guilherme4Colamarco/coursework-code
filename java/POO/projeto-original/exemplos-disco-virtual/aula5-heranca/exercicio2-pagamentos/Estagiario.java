/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author roberto
 */
public class Estagiario extends Funcionario {
    public Estagiario(double salarioBase) {
        super(salarioBase);
    }

    public double pagamentoComoEstagiario() {
        return salarioBase / 2; // metade
    }
}

