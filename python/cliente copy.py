import Pyro4, sys
from datetime import datetime, date

nome = sys.argv[1].strip()

lista_de_chamada = Pyro4.Proxy("PYRONAME:lista-de-chamada")
ja_respondeu = False


while True:
    print("0. Responder chamada")
    print("1. Ver lista de alunos")
    print("2. Ver disciplina")
    print("3. Ver data")
    print("4. Ver professor")
    print("99. Encerrar programa")
    opcao = int(input("--> "))
    if(opcao == 0):
        if(ja_respondeu == False):
            lista_de_chamada.adicionarAluno(nome)
            ja_respondeu = True
            print("Chamada respondida com sucesso")
        else:
            print("Já respondeste, marreco")
    elif(opcao == 1):
        for i in range(len(lista_de_chamada.verAlunos())):
            print(" — Aluno #", i, ": ", lista_de_chamada.verAlunos()[i])
    elif(opcao == 99):
        break    
    elif(opcao == 2):   
        print("Disciplina: ", lista_de_chamada.verDisciplina())
    elif(opcao == 3):
        print(lista_de_chamada.verData())
    elif(opcao == 4):
        print(lista_de_chamada.verProfessor())
    else:
        print("Opção inválida")