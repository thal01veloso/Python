from connect import atualizarPessoa, deletarPessoa, inserir, mostrarTabelaTodos, mostrarTodos
from model import Pessoa


def main():
    p = Pessoa(125588874,"Marcos","20-08-1987")
    p1 = Pessoa(7854152569,"Judson","20-08-1988")
    p2 = Pessoa(20012500253,"Angelina","20-08-2005")
    p3 = Pessoa(345228879,"Theobaldo","13-07-1995")

    #inserir(p3)
    #atualizarPessoa(18293,p1)
    t = mostrarTodos()
    for i in t:
        print(i)
    tt = mostrarTabelaTodos()
    print(tt)
main()