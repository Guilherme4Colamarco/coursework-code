package com.mycompany.atividades_praticas_1.biblioteca;

public class ProgramaBiblioteca {
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarUsuario(new Professor("Maria", "Rua A, 100", "Computação"));
        biblioteca.cadastrarUsuario(new Aluno("João", "Rua B, 200", "IA e Ciência de Dados"));
        biblioteca.cadastrarUsuario(new FuncionarioBiblioteca("Carlos", "Rua C, 300", "Bibliotecário"));

        Obra obra = new Obra("Java: Como Programar", "Livro científico");
        obra.adicionarAutor(new Autor("Deitel", "Americana"));

        Exemplar exemplar = new Exemplar(
                obra,
                "Português",
                "Impresso",
                new Editora("Pearson"),
                2020
        );
        biblioteca.cadastrarExemplar(exemplar);

        biblioteca.listarUsuarios();
        biblioteca.listarExemplares();
    }
}
