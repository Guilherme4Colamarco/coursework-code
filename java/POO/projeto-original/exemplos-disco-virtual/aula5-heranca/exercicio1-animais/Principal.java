public class Principal {
    public static void main(String[] args) {
        Animal a1 = new Animal();
        Cachorro dog = new Cachorro();
        Gato cat = new Gato();
        Vaca cow = new Vaca();

        System.out.println("=== Exercício 1: Animais ===");
        System.out.println("Som genérico: " + a1.somGenerico());
        System.out.println("Cachorro: " + dog.somDoCachorro());
        System.out.println("Gato: " + cat.somDoGato());
        System.out.println("Vaca: " + cow.somDaVaca());
    }
}
