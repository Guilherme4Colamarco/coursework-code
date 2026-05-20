import java.util.Arrays; import java.util.Scanner;
public class Q9 { public static void main(String[] args){ Scanner in=new Scanner(System.in); double[] v={in.nextDouble(),in.nextDouble(),in.nextDouble()}; Arrays.sort(v); System.out.println(v[2]+" "+v[1]+" "+v[0]); } }
