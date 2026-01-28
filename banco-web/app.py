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

if __name__ == "__main__":
    app.run(debug=True)
