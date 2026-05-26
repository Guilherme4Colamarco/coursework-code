/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author roberto.dti
 */
public class Gerente extends Funcionario {
    private String departamento;

    // Construtor da subclasse chamando o da superclasse
    public Gerente(String nome, double salario, String departamento) {
        super(nome, salario);
        this.departamento = departamento;
    }

    // Método para exibir as informações
    public void mostrarInfo() {
        System.out.println(
            "Gerente { Nome: " + getNome() +
            ", Salário: " + getSalario() +
            ", Departamento: " + departamento + " }"
        );
    }
}

