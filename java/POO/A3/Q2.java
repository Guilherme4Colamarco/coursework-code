import java.util.Scanner;
public class Q2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Digite um número: ");
        double n = in.nextDouble();
        System.out.println(n > 0 ? "Positivo" : n < 0 ? "Negativo" : "Zero");
    }
}
