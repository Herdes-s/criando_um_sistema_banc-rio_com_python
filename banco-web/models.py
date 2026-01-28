# models.py

def depositar(saldo, valor, extrato):
    if valor <= 0:
        return saldo, extrato, "Valor inválido para depósito"

    saldo += valor
    extrato += f"Depósito: R${valor:.2f}\n"
    return saldo, extrato, "Depósito realizado com sucesso"


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        return saldo, extrato, numero_saques, "Valor inválido para saque"

    if valor > saldo:
        return saldo, extrato, numero_saques, "Saldo insuficiente"

    if valor > limite:
        return saldo, extrato, numero_saques, "Limite por saque é R$500"

    if numero_saques >= limite_saques:
        return saldo, extrato, numero_saques, "Limite diário de saques atingido"

    saldo -= valor
    extrato += f"Saque: R${valor:.2f}\n"
    numero_saques += 1

    return saldo, extrato, numero_saques, "Saque realizado com sucesso"


def gerar_extrato(saldo, extrato):
    if not extrato:
        return "Sem movimentações", saldo

    return extrato, saldo


def criar_usuario(usuarios, cpf, nome, data_nascimento, endereco):
    if filtrar_usuario(cpf, usuarios):
        return False, "Usuário já existe"

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    return True, "Usuário criado com sucesso"


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios, cpf):
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        return None, "Usuário não encontrado"

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }

    return conta, "Conta criada com sucesso"