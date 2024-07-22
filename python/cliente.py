import Pyro4
import sys

def pegarNome():
    if len(sys.argv) < 2:
        print("Uso: python3", sys.argv[0], "<nome-do-aluno>")
        print("Exemplo: python3", sys.argv[0], "Lisiane")
        exit()
    return sys.argv[1].strip()

def instanciarObjetoRemoto():
    try:
        return Pyro4.Proxy("PYRONAME:lista-de-chamada")
    except Pyro4.errors.NamingError:
        print("Erro: Servidor de nomes não encontrado ou objeto remoto 'lista-de-chamada' não registrado.")
        exit()

def mostrarMenu():
    print("0. Assinar chamada")
    print("1. Obter cópia atual da chamada")
    print("99. Encerrar programa")

def aguardarOpcao():
    while True:
        try:
            opcao = int(input("--> "))
            if opcao in [0, 1, 99]:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def decidirCaminho(opcao, ja_assinou, lista_de_chamada, nome):
    try:
        if opcao == 0 and not ja_assinou:
            lista_de_chamada.adicionarAluno(nome)
            ja_assinou = True
            print("Chamada respondida com sucesso")
        elif opcao == 1:
            alunos = lista_de_chamada.verAlunos()
            print("[ LISTA DE CHAMADA DA DISCIPLINA ", lista_de_chamada.verDisciplina(), ", MINISTRADA POR ", lista_de_chamada.verProfessor(), " — DIA ", lista_de_chamada.verData(), "]")
            for index, aluno in enumerate(alunos):
                print("\t — Aluno #", index, ": ", aluno)
        else:
            print("Opção inválida")
    except Pyro4.errors.CommunicationError:
        print("Erro: Não foi possível se comunicar com o servidor. Certifique-se de que o servidor está em execução.")
        exit()
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
    ja_assinou = decidirCaminho(opcao, ja_assinou, lista_de_chamada, nome)
