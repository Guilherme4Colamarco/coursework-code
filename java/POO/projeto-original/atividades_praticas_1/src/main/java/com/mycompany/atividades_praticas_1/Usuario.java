package com.mycompany.atividades_praticas_1;

import java.util.ArrayList;
import java.util.List;

public class Usuario {
    private String nome;
    private String endereco;
    private String tipo; // Professor, Aluno, Funcionario

    public Usuario(String nome, String endereco, String tipo) {
        this.nome = nome;
        this.endereco = endereco;
        this.tipo = tipo;
    }

    public void exibirDados() {
        System.out.println("Nome: " + nome);
        System.out.println("Endereço: " + endereco);
        System.out.println("Tipo: " + tipo);
    }

    // Getters and setters
    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }
    public String getEndereco() { return endereco; }
    public void setEndereco(String endereco) { this.endereco = endereco; }
    public String getTipo() { return tipo; }
    public void setTipo(String tipo) { this.tipo = tipo; }
}