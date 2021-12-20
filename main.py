from connect import atualizarPessoa, deletarPessoa, inserir, mostrarTodos
from model import Pessoa


def main():
    p = Pessoa(125588874,"Marcos","20-08-1987")
    p1 = Pessoa(7854152569,"Judson","20-08-1988")
    p2 = Pessoa(20012500253,"Angelina","20-08-2005")
    
    #atualizarPessoa(18293,p1)
    t = mostrarTodos()
    for i in t:
        print(i)
main()