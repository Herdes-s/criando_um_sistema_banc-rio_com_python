menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair"""

saldo = 0
limite = 500
extrato = ''
numeros_de_saque = 0
LIMITE_SAQUE = 3


while True:
    print(menu)
    opcao = input("Encira uma opção:")

    #Deposito
    if opcao == "d":
        valor = float(input("Valor do deposito: "))
        if valor > 0:
            saldo += valor
            print(f"Valor em sua conta R${saldo:.2f}")
            extrato += f"Deposito:  R${valor:.2f}\n"
        else:
            print("Valor invalido para deposito!")

    #Saque
    elif opcao == "s":
        valor = float(input("Valor a ser sacado: "))
        if valor > saldo:
            print("Sua conta não possui esse valor!")
        elif valor > limite:
            print("Limite por saque é de R$500.00")
        elif numeros_de_saque >= LIMITE_SAQUE:
            print("Seu numero de saque diario acabou, volte amanhã para mais!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:  R${valor:.2f}\n"
            numeros_de_saque += 1
            print("Saque realizado com SUCESSO!")
        else:
            print("Valor invalido para saque!")

    #Extrato
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Sem movimentações" if not extrato else extrato)
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("=============================\n")

    #Sair
    elif opcao == "q":
        print("Obrigado pela sua preferencia!")
        break

    else:
        print("Função invalida")