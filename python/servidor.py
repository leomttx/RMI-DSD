import Pyro4, sys
from ListaDeChamada import ListaDeChamada

def pegarArgumentosDaLinhaDeComando():
    if(len(sys.argv) < 3):
        print("Uso: python3 ", sys.argv[0], " <professor> <disciplina> [data]")
        print("Exemplo: python3 ", sys.argv[0], " Lisiane POO 2020-09-01")
        exit()
    return sys.argv[1], sys.argv[2], sys.argv[3] if(len(sys.argv) > 3) else None

def iniciarProcessoEmSegundoPlano():
    return Pyro4.Daemon()

def procurarServidorDeNomes():
    return Pyro4.locateNS()

def transformarObjetoOriginalEmObjetoPyro(objeto):
    return daemon.register(objeto)

def registrarObjetoPyroNoServidorDeNomes(servidor_de_nomes, uri):
    servidor_de_nomes.register("lista-de-chamada", uri)

def rodarOProcesso():
    daemon.requestLoop()

# início do programa
professor, disciplina, data = pegarArgumentosDaLinhaDeComando()

daemon = iniciarProcessoEmSegundoPlano() # cria um daemon do Pyro
ns = procurarServidorDeNomes() # localiza o servidor de nomes
objeto_original = ListaDeChamada(professor, disciplina, data)
uri = transformarObjetoOriginalEmObjetoPyro(objeto_original) # registra o objeto no daemon e retorna a URI
print("URI: ", uri)
registrarObjetoPyroNoServidorDeNomes(ns, uri) # registra o objeto com um nome no servidor de nomes
rodarOProcesso()   # inicia o servidor