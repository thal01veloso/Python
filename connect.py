from model import Pessoa
from tinydb import TinyDB, Query
import pandas as pd

bd = TinyDB("Pessoas.json")
usuario = Query()
def inserir(model: Pessoa):
    '''Insere um modelo no banco de dados'''
    bd.insert({"CPF":model.CPF,
    "Nome":model.nome,
    "DataNascimento":model.dataNascimento})
def mostrarTodos():
    '''Mostra todos os contatos cadastrados no banco de dados'''
   
    todos = bd.all()
    return todos
def deletarPessoa(cpf: int):
    '''Busca um CPF e deleta o registro do modelo encontrado'''
    if bd.search(usuario.CPF==str(cpf)):
        bd.remove(usuario.CPF==str(cpf))
    else:
        print("Usuário não encontrado")
def atualizarPessoa(cpf: int, model:Pessoa):
    """Atualiza um modelo no banco de dados"""
    if bd.search(usuario.CPF==str(cpf)):
        bd.remove(usuario.CPF==str(cpf))
        inserir(model)
    else:
        print("Esse usuário não existe")
def mostrarTabelaTodos():
    todos = pd.DataFrame(bd)  
    return todos.to_html()        
def buscarPorCPF(cpf):
    return bd.search(usuario.CPF==str(cpf))
def count():
    total_cadastrado = len(bd.all())
    return total_cadastrado

    

# CRUD = Create/Read/Update/Delete