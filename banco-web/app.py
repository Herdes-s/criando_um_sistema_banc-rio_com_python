from flask import Flask, render_template, request
import models

app = Flask(__name__)

usuarios = []

contas = []
numero_conta = 1
AGENCIA = "0001"

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/deposito", methods=["GET" ,"POST"])
def deposito():
    global saldo, extrato

    mensagem = None

    if request.method == "POST":
        valor = float(request.form["valor"])
        saldo, extrato, mensagem = models.depositar(saldo, valor, extrato)

    return render_template("deposito.html", saldo=saldo, mensagem=mensagem)

@app.route("/saque", methods=["GET", "POST"])
def saque():
    global saldo, extrato, numero_saques

    mensagem = None

    if request.method == "POST":
        valor =float(request.form["valor"])

        saldo, extrato, numero_saques, mensagem = models.sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=LIMITE,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    return render_template(
        "saque.html",
        saldo=saldo,
        mensagem=mensagem,
        numero_saques=numero_saques
    )

@app.route("/extrato", methods=["GET", "POST"])
def extrato_view(): 
    texto_extrato, saldo_atual = models.gerar_extrato(saldo, extrato)
    return render_template(
        "extrato.html",
        extrato=texto_extrato,
        saldo=saldo_atual
    )

@app.route("/usuario/novo", methods=["GET", "POST"])
def novo_usuario():
    mensagem = None
    sucesso = False

    if request.method == "POST":
        cpf = request.form["cpf"]
        nome = request.form["nome"]
        data_nascimento = request.form["data_nascimento"]
        endereco = request.form["endereco"]

        sucesso, mensagem = models.criar_usuario(
            usuarios,
            cpf,
            nome,
            data_nascimento,
            endereco
        )

    return render_template(
        "novo_usuario.html",
        mensagem=mensagem,
        sucesso=sucesso
    )

@app.route("/conta/nova", methods=["GET", "POST"])
def nova_conta():
    global numero_conta

    mensagem = None

    if request.method == "POST":
        cpf = request.form["cpf"]

        conta, mensagem = models.criar_conta(
            AGENCIA,
            numero_conta,
            usuarios,
            cpf
        )

        if conta:
            contas.append(conta)
            numero_conta += 1

    return render_template(
        "nova_conta.html",
        mensagem=mensagem
    )



if __name__ == "__main__":
    app.run(debug=True)
