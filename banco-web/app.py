from flask import Flask, render_template
import models

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# dados = [
#     LIMITE_SAQUES = 3,
#     AGENCIA = '0001',

#     saldo = 0,
#     limite = 500,
#     extrato = '',
#     numero_saques = 0,
#     usuarios = [],
#     contas = [],
#     numero_conta = 1
# ]