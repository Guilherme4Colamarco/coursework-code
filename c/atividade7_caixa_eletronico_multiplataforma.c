/*
 * ATIVIDADE 7 - Linguagem e Técnicas de Programação
 * Programa: Simulador de Caixa Eletrônico (Versão Multiplataforma)
 * Descrição: Sistema de caixa eletrônico com operações de saldo, depósito e saque
 * Autor: [Seu Nome]
 * Data: Novembro/2024
 */

#include <stdio.h>
#include <stdlib.h>

// Função para pausar o programa (alternativa ao getch())
void pausar() {
    printf("\nPressione ENTER para continuar...");
    getchar();
}

// Função para limpar a tela (multiplataforma)
void limparTela() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

// Função para exibir o menu principal
void exibirMenu() {
    printf("\n========================================\n");
    printf("         CAIXA ELETRONICO               \n");
    printf("========================================\n");
    printf("1 - Verificar saldo\n");
    printf("2 - Realizar um deposito\n");
    printf("3 - Realizar um saque\n");
    printf("4 - Sair do caixa eletronico\n");
    printf("========================================\n");
    printf("Digite sua opcao: ");
}

// Função para verificar saldo
void verificarSaldo(float saldo) {
    limparTela();
    printf("\n========================================\n");
    printf("         CONSULTA DE SALDO              \n");
    printf("========================================\n");
    printf("Saldo atual: R$ %.2f\n", saldo);
    printf("========================================\n");
    pausar();
}

// Função para realizar depósito
float realizarDeposito(float saldo) {
    float valor;
    int entradaValida;
    
    limparTela();
    printf("\n========================================\n");
    printf("           DEPOSITO                     \n");
    printf("========================================\n");
    printf("Saldo atual: R$ %.2f\n", saldo);
    printf("----------------------------------------\n");
    
    do {
        printf("Digite o valor do deposito: R$ ");
        entradaValida = scanf("%f", &valor);
        
        // Limpa o buffer de entrada
        while (getchar() != '\n');
        
        if (entradaValida != 1) {
            printf("Erro: Entrada invalida! Digite apenas numeros.\n");
        } else if (valor <= 0) {
            printf("Erro: O valor do deposito deve ser maior que zero!\n");
            entradaValida = 0;
        }
    } while (entradaValida != 1);
    
    saldo += valor;
    
    printf("\n========================================\n");
    printf("Deposito bem-sucedido!\n");
    printf("Valor depositado: R$ %.2f\n", valor);
    printf("Novo saldo: R$ %.2f\n", saldo);
    printf("========================================\n");
    pausar();
    
    return saldo;
}

// Função para realizar saque
float realizarSaque(float saldo) {
    float valor;
    int entradaValida;
    
    limparTela();
    printf("\n========================================\n");
    printf("             SAQUE                      \n");
    printf("========================================\n");
    printf("Saldo atual: R$ %.2f\n", saldo);
    printf("----------------------------------------\n");
    
    do {
        printf("Digite o valor do saque: R$ ");
        entradaValida = scanf("%f", &valor);
        
        // Limpa o buffer de entrada
        while (getchar() != '\n');
        
        if (entradaValida != 1) {
            printf("Erro: Entrada invalida! Digite apenas numeros.\n");
        } else if (valor <= 0) {
            printf("Erro: O valor do saque deve ser maior que zero!\n");
            entradaValida = 0;
        } else if (valor > saldo) {
            printf("\n========================================\n");
            printf("Saldo insuficiente!\n");
            printf("Saldo disponivel: R$ %.2f\n", saldo);
            printf("========================================\n");
            pausar();
            return saldo;
        }
    } while (entradaValida != 1);
    
    saldo -= valor;
    
    printf("\n========================================\n");
    printf("Saque bem-sucedido!\n");
    printf("Valor sacado: R$ %.2f\n", valor);
    printf("Novo saldo: R$ %.2f\n", saldo);
    printf("========================================\n");
    pausar();
    
    return saldo;
}

int main() {
    // Saldo inicial conforme requisito
    float saldo = 1000.00;
    int opcao;
    int entradaValida;
    
    // Mensagem de boas-vindas
    printf("\n========================================\n");
    printf("   BEM-VINDO AO CAIXA ELETRONICO!      \n");
    printf("========================================\n");
    printf("Saldo inicial: R$ %.2f\n", saldo);
    pausar();
    
    // Loop principal do programa
    do {
        limparTela();
        exibirMenu();
        
        // Validação da entrada do menu
        entradaValida = scanf("%d", &opcao);
        
        // Limpa o buffer de entrada
        while (getchar() != '\n');
        
        if (entradaValida != 1) {
            printf("\nErro: Opcao invalida! Digite um numero de 1 a 4.");
            pausar();
            continue;
        }
        
        // Processamento das opções do menu
        switch(opcao) {
            case 1:
                verificarSaldo(saldo);
                break;
                
            case 2:
                saldo = realizarDeposito(saldo);
                break;
                
            case 3:
                saldo = realizarSaque(saldo);
                break;
                
            case 4:
                limparTela();
                printf("\n========================================\n");
                printf("         ENCERRANDO SISTEMA             \n");
                printf("========================================\n");
                printf("Obrigado por utilizar nosso caixa eletronico!\n");
                printf("Saldo final: R$ %.2f\n", saldo);
                printf("========================================\n");
                pausar();
                break;
                
            default:
                printf("\nErro: Opcao invalida! Escolha uma opcao de 1 a 4.");
                pausar();
        }
        
    } while (opcao != 4);
    
    return 0;
}
