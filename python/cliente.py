import Pyro4, sys
from datetime import datetime, date

def pegarNome():
    if(len(sys.argv) < 2):
        print("Uso: python3 ", sys.argv[0], " <nome-do-aluno>")
        print("Exemplo: python3 ", sys.argv[0], " Lisiane")
        exit()
    return sys.argv[1].strip()

def instanciarObjetoRemoto():
    return Pyro4.Proxy("PYRONAME:lista-de-chamada")

def mostrarMenu():
    print("0. Assinar chamada")
    print("1. Obter cópia atual da chamada")
    print("99. Encerrar programa")

def aguardarOpcao():
    while True:
        return int(input("--> "))

def decidirCaminho(opcao, ja_assinou):
    if opcao == 0 and not ja_assinou:
        lista_de_chamada.adicionarAluno(nome)
        ja_assinou = True
        print("Chamada respondida com sucesso")
    elif opcao == 1:
        alunos = lista_de_chamada.verAlunos()
        print("[ LISTA DE CHAMADA DA DISCIPLINA", lista_de_chamada.verDisciplina(), ", MINISTRADA POR", lista_de_chamada.verProfessor(), "— DIA", lista_de_chamada.verData(), "]")
        for index, aluno in enumerate(alunos):
            print("\t — Aluno #", index, ":", aluno)
    else:
        print("Opção inválida")
    return ja_assinou

# início do programa
nome = pegarNome()
lista_de_chamada = instanciarObjetoRemoto()
ja_assinou = False

while True:
    mostrarMenu()
    opcao = aguardarOpcao()
    if opcao == 99:
        break
    ja_assinou = decidirCaminho(opcao, ja_assinou)
