import Pyro4, sys
from ListaDeChamada import ListaDeChamada

professor = sys.argv[1]
disciplina = sys.argv[2]
data = None
if(len(sys.argv) > 3):
    data = sys.argv[3]

daemon = Pyro4.Daemon() # cria um daemon do Pyro
ns = Pyro4.locateNS() # localiza o servidor de nomes
objeto_original = ListaDeChamada(professor, disciplina, data)
uri = daemon.register(objeto_original)
print("URI: ", uri)
ns.register("lista-de-chamada", uri) # registra o objeto com um nome no servidor de nomes

daemon.requestLoop()   # inicia o servidor