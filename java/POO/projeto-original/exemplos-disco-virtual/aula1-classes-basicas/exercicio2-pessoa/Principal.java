import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        Pessoa p1 = new Pessoa();

        // Popular objeto pessoa p1
        System.out.print("Digite o seu nome: ");
        p1.nome = ent.nextLine();
        System.out.print("Digite a sua idade: ");
        p1.idade = ent.nextInt();

        System.out.println(p1.apresentar());
    }
}
