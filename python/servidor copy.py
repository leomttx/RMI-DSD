import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Olá, {0}! Aqui está sua mmensagem da fortuna: \n" \
            "é... Olha o teu watsap".format(name)

daemon = Pyro4.Daemon() # cria um daemon do Pyro
ns = Pyro4.locateNS() # localiza o servidor de nomes
uri = daemon.register(GreetingMaker) 
ns.register("example.greeting", uri) # registra o objeto com um nome no servidor de nomes

print("Pronto! URI = ", uri)
daemon.requestLoop()   # inicia o servidor