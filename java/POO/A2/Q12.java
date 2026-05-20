import java.util.Scanner;
public class Q12 { public static void main(String[] args){ Scanner in=new Scanner(System.in); System.out.print("Altura em metros: "); double h=in.nextDouble(); System.out.print("Sexo (H/M): "); String sexo=in.next().trim().toUpperCase(); double peso=sexo.equals("H") ? (72.7*h)-58 : (62.1*h)-44.7; System.out.printf("Peso ideal: %.2f kg%n", peso); } }
