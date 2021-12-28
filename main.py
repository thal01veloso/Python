from connect import atualizarPessoa, deletarPessoa, inserir, mostrarTabelaTodos, mostrarTodos
from model import Pessoa
from flask import Flask, render_template
import pandas as pd
from flask.globals import request

app = Flask(__name__)
@app.route('/')
def index():
    result = mostrarTodos()
    return render_template("index.html",
    result = result)

@app.route("/cadastrar", methods=["POST","GET"])
def cadastrar():
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    dataNascimento = request.form["dataNascimento"]
    pessoa = Pessoa(cpf,nome,dataNascimento)
    inserir(pessoa)
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)


