from connect import atualizarPessoa, deletarPessoa, inserir, mostrarTabelaTodos, mostrarTodos
from model import Pessoa
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
@app.route('/')
def index():
    result = mostrarTodos()
    return render_template("index.html",
    result = result)
if __name__=="__main__":
    app.run(debug=True)


