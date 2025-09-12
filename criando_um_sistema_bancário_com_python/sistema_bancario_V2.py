menu = """
[d] Deposito
[s] Saque
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[q] Sair
"""

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        print(f"Valor em sua conta R${saldo:.2f}")
        extrato += f"Deposito:  R${valor:.2f}\n"
    else:
        print("Valor invalido para deposito!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Sua conta não possui esse valor!")
    elif valor > limite:
        print("Limite por saque é de R$500.00")
    elif numero_saques >= limite_saques:
        print("Seu numero de saque diário acabou, volte amanhã para mais!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:  R${valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com SUCESSO!")
    else:
        print("Valor invalido para saque!")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Sem movimentações" if not extrato else extrato)
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("=============================\n")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse CPF.")
        return 

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado, fluxo de criação de conta encerrado!")
        return None
    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        print(menu)
        opcao = input("Encira uma opção: ")

        # Deposito
        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        # Saque
        elif opcao == "s":
            valor = float(input("Valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        # Extrato
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        # Novo usuário
        elif opcao == "nu":
            criar_usuario(usuarios)

        # Nova conta
        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        # Sair
        elif opcao == "q":
            print("Obrigado por usar o banco! Volte sempre!")
            break

        else:
            print("Opção inválida!")


main()