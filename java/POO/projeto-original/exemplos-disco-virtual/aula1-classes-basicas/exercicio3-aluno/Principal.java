import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        Aluno a1 = new Aluno();

        // Populando objeto Aluno a1
        System.out.print("Digite o nome do aluno: ");
        a1.nome = ent.nextLine();
        System.out.print("Digite a nota 1: ");
        a1.n1 = ent.nextDouble();
        System.out.print("Digite a nota 2: ");
        a1.n2 = ent.nextDouble();

        System.out.println("A média das notas é " + a1.media());
    }
}
