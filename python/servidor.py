import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Olá, {0}! Aqui está sua mmensagem da fortuna: \n" \
            "é... Olha o teu watsap".format(name)

daemon = Pyro4.Daemon()
uri = daemon.register(GreetingMaker)

print("Pronto! URI = ", uri)
daemon.requestLoop()