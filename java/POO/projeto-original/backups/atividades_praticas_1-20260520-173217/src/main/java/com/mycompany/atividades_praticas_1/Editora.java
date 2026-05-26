package com.mycompany.atividades_praticas_1;

/**
 * Representa uma editora de uma obra no exercício de biblioteca.
 */
public class Editora {
    private String nome;
    private String cidade;

    public Editora(String nome, String cidade) {
        this.nome = nome;
        this.cidade = cidade;
    }

    public void exibirDados() {
        System.out.println("Editora: " + nome);
        System.out.println("Cidade: " + cidade);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }
}
