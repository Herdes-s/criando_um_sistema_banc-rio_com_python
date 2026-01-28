from flask import Flask, render_template, request
import models

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
