package com.mycompany.atividades_praticas_1;

/**
 * Representa um autor de uma obra no exercício de biblioteca.
 */
public class Autor {
    private String nome;
    private String nacionalidade;

    public Autor(String nome, String nacionalidade) {
        this.nome = nome;
        this.nacionalidade = nacionalidade;
    }

    public void exibirDados() {
        System.out.println("Autor: " + nome);
        System.out.println("Nacionalidade: " + nacionalidade);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }
}
