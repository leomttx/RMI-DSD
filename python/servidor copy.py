import Pyro4
from ListaDeChamada import ListaDeChamada

daemon = Pyro4.Daemon() # cria um daemon do Pyro
ns = Pyro4.locateNS() # localiza o servidor de nomes
uri = daemon.register(ListaDeChamada("Dev. Distribuído")) 
ns.register("lista-de-chamada", uri) # registra o objeto com um nome no servidor de nomes

print("Pronto! URI = ", uri)
daemon.requestLoop()   # inicia o servidor