import java.util.Scanner;
public class Q8 { public static void main(String[] args){ Scanner in=new Scanner(System.in); System.out.print("Temperatura em Fahrenheit: "); double f=in.nextDouble(); double c=5*((f-32)/9); System.out.printf("Celsius: %.2f%n", c); } }
