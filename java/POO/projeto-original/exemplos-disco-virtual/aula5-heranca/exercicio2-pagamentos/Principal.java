public class Principal {
    public static void main(String[] args) {
        Gerente g1 = new Gerente(5000.0);
        Estagiario e1 = new Estagiario(2000.0);

        double pagamentoGerente = g1.pagamentoComoGerente();
        double pagamentoEstagiario = e1.pagamentoComoEstagiario();

        System.out.println("=== Exercício 2: Pagamentos ===");
        System.out.println("Salário base Gerente: " + g1.obterSalarioBase());
        System.out.println("Pagamento como Gerente: " + pagamentoGerente);

        System.out.println("Salário base Estagiário: " + e1.obterSalarioBase());
        System.out.println("Pagamento como Estagiário: " + pagamentoEstagiario);

        if (pagamentoGerente > pagamentoEstagiario) {
            System.out.println("O Gerente recebe mais.");
        } else if (pagamentoGerente < pagamentoEstagiario) {
            System.out.println("O Estagiário recebe mais.");
        } else {
            System.out.println("Ambos recebem o mesmo.");
        }
    }
}
