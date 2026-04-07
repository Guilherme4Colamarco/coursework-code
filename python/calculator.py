# --- Simple Calculator Program ---

while True:

    print("=====================")
    print("<<----programas---->>")
    print("=====================")

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        num1 = float(input("digite o 1º número: "))
        num2 = float(input("digite o 2º número: "))
        result = num1 + num2
        print("o resultado é", result)

    elif opcao == 2:
        num1 = float(input("digite o 1º número: "))
        num2 = float(input("digite o 2º número: "))
        result = num1 - num2
        print("o resultado é", result)

    elif opcao == 3:
        num1 = float(input("digite o 1º número: "))
        num2 = float(input("digite o 2º número: "))
        result = num1 * num2
        print("o resultado é", result)

    elif opcao == 4:
        num1 = float(input("digite o 1º número: "))
        num2 = float(input("digite o 2º número: "))
        if num2 != 0:
            result = num1 / num2
            print("o resultado é", result)
        else:
            print("não é possível dividir por zero")
    elif opcao == 5:
        print("sair")
        break

    else:
        print("opção inválida")
