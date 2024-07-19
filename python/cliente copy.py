import Pyro4, sys

nome = sys.argv[1].strip()

lista_de_chamada = Pyro4.Proxy("PYRONAME:lista-de-chamada")
ja_respondeu = False


while True:
    print("0. Responder chamada")
    print("99. Encerrar programa")
    opcao = int(input("-- >"))
    if(opcao == 0):
        if(ja_respondeu == False):
            lista_de_chamada.adicionarAluno(nome)
            ja_respondeu = True
        else:
            print("Já respondeste, marreco")
    elif(opcao == 99):
        break    



# lista_de_chamada = Pyro4.Proxy("PYRONAME:lista-de-chamada")
#     lista_de_chamada.adicionarAluno(nome)
#     jarespondeu = True
#     if VerificaSeJaRespondeu():
#         print("Seu nome já está na lista: ", lista_de_chamada.verAlunos())
#     print(lista_de_chamada.verAlunos())
#     print("Disciplina: ", lista_de_chamada.verDisciplina())
