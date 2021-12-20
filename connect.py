from model import Pessoa
from tinydb import TinyDB, Query

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
    if bd.search(usuario.CPF==cpf):
        bd.remove(usuario.CPF==cpf)
    else:
        print("Usuário não encontrado")
def atualizarPessoa(cpf: int, model:Pessoa):
    """Atualiza um modelo no banco de dados"""
    if bd.search(usuario.CPF==cpf):
        bd.remove(usuario.CPF==cpf)
        inserir(model)
    else:
        print("Esse usuário não existe")

    

# CRUD = Create/Read/Update/Delete
