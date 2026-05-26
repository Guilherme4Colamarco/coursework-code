package com.mycompany.atividades_praticas_1;

import java.util.ArrayList;
import java.util.List;

public class Obra {
    private String titulo;
    private List<Autor> autores;
    private String categoria; // Livro científico, Periódico, etc.
    private String lingua;
    private String midia;
    private Editora editora;
    private int anoEdicao;

    public Obra(String titulo, String categoria, String lingua, String midia, Editora editora, int anoEdicao) {
        this.titulo = titulo;
        this.categoria = categoria;
        this.lingua = lingua;
        this.midia = midia;
        this.editora = editora;
        this.anoEdicao = anoEdicao;
        this.autores = new ArrayList<>();
    }

    public void adicionarAutor(Autor autor) {
        this.autores.add(autor);
    }

    public void exibirDados() {
        System.out.println("Título: " + titulo);
        System.out.println("Categoria: " + categoria);
        System.out.println("Língua: " + lingua);
        System.out.println("Mídia: " + midia);
        System.out.println("Ano de Edição: " + anoEdicao);
        if (editora != null) editora.exibirDados();
        for (Autor a : autores) a.exibirDados();
    }

    // Getters and setters
    public String getTitulo() { return titulo; }
    public void setTitulo(String titulo) { this.titulo = titulo; }
    // ... outros getters/setters
}