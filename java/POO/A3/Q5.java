import java.util.Scanner;
public class Q5 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Nota 1: ");
        double n1 = in.nextDouble();
        System.out.print("Nota 2: ");
        double n2 = in.nextDouble();
        double m = (n1 + n2) / 2;
        System.out.println(m == 10 ? "Aprovado com Distinção" : m >= 7 ? "Aprovado" : "Reprovado");
    }
}
