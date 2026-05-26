import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        Carro c1 = new Carro();
        Carro c2 = new Carro();

        // Populando objeto carro c1
        System.out.print("Digite a cor do carro: ");
        c1.cor = ent.nextLine();
        System.out.print("Digite o modelo do carro: ");
        c1.modelo = ent.nextLine();
        System.out.print("Digite o ano do carro: ");
        c1.ano = ent.nextInt();

        c1.ligar();
        c1.acelerar();

        // Populando objeto carro c2
        System.out.print("Digite a cor do carro: ");
        ent.nextLine();
        c2.cor = ent.nextLine();
        System.out.print("Digite o modelo do carro: ");
        c2.modelo = ent.nextLine();
        System.out.print("Digite o ano do carro: ");
        c2.ano = ent.nextInt();

        c2.ligar();
        c2.acelerar();
    }
}
