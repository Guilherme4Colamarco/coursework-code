import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        Produto prod1 = new Produto();

        // Populando objeto Produto prod1
        System.out.print("Digite o nome do produto: ");
        prod1.nome = ent.nextLine();
        System.out.print("Digite o preço do produto: ");
        prod1.preco = ent.nextDouble();

        prod1.mostrarPreco();
    }
}
