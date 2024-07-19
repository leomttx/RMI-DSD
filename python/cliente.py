import Pyro4, sys

uri = sys.argv[1].strip()
nome = sys.argv[2].strip()

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune(nome))