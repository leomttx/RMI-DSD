import Pyro4, sys

nome = sys.argv[1].strip()

lista_de_chamada = Pyro4.Proxy("PYRONAME:lista-de-chamada")
lista_de_chamada.adicionarAluno(nome)
print(lista_de_chamada.verAlunos())
print("Disciplina: ", lista_de_chamada.verDisciplina())
