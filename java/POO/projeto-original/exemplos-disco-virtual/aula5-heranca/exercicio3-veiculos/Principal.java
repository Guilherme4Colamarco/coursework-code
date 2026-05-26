public class Principal {
    public static void main(String[] args) {
        Veiculo v1 = new Veiculo();
        Carro c1 = new Carro();
        Moto m1 = new Moto();

        System.out.println("=== Exercício 3: Veículos ===");
        System.out.println("Genérico: " + v1.acelerarGenerico());
        System.out.println("Carro: " + c1.acelerarCarro());
        System.out.println("Moto: " + m1.acelerarMoto());
    }
}
