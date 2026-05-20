import java.util.Scanner;
public class Q7 { public static void main(String[] args){ Scanner in=new Scanner(System.in); double a=in.nextDouble(),b=in.nextDouble(),c=in.nextDouble(); System.out.println("Maior: "+Math.max(a,Math.max(b,c))); System.out.println("Menor: "+Math.min(a,Math.min(b,c))); } }
