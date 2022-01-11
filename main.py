from connect import atualizarPessoa, buscarPorCPF, count, deletarPessoa, inserir, mostrarTabelaTodos, mostrarTodos
from model import Pessoa
from flask import Flask, render_template, redirect
import pandas as pd
from flask.globals import request

app = Flask(__name__)
@app.route('/')
def index():
    result = mostrarTodos()
    total_cadastrado = count()
    return render_template("index.html",
    result = result,
    total = total_cadastrado)

@app.route("/cadastrar", methods=["POST","GET"])
def cadastrar():
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    dataNascimento = request.form["dataNascimento"]
    pessoa = Pessoa(cpf,nome,dataNascimento)
    inserir(pessoa)
    return redirect("/")
@app.route('/atualizar/<int:cpf>',methods=["POST","GET"])
def atualizar(cpf):    
    if request.method =='POST':
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        dataNascimento = request.form["dataNascimento"]
        pessoa = Pessoa(cpf,nome,dataNascimento)
        try:
            atualizarPessoa(cpf,pessoa)
            return redirect('/')
        except:
            return 'algo deu errado'
    else:
        pessoa = buscarPorCPF(cpf)
        return render_template('update.html',pessoa = pessoa)
        


@app.route('/deletar/<int:cpf>')
def deletar(cpf):
    try:
        deletarPessoa(cpf)
        return redirect("/")
    except:
        return "Algo de errado aconteceu"
if __name__=="__main__":
    app.run(debug=True)