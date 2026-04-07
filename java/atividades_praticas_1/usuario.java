public class usuario {
    String nome;
    String tipo;
    String endereco;
    String autor;
    String categoria;
    String titulo;
    String midia;

    void exibirDados() {
        System.out.println("Nome: " + nome);
        System.out.println("Tipo: " + tipo);
        System.out.println("Endereco: " + endereco);
    }

    public static void main(String[] args) {
        usuario u1 = new usuario();

        u1.nome = "Guilherme";
        u1.tipo = "Aluno";
        u1.endereco = "Rua A, 123";

        u1.exibirDados();
    }
}
