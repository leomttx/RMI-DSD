from __future__ import print_function 
import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Warehouse(object):
    def __init__(self):
        self.contents = ["Melancias", "laranjas", "peras", "uvas"]

    def list_contents(self):
        return self.contents
    
    def take(self, name, item):
        self.contents.remove(item)
        print("{0} pegou o item {1}".format(name, item))

    def store(self, name, item):
        self.contents.append(item)
        print("{0} guardou o item {1}".format(name, item))


def main():
    Pyro4.Daemon.serveSimple(
        {
            Warehouse: "liziane.warehouse" 
        },
        ns = False)

if __name__ == "__main__":
    main()    