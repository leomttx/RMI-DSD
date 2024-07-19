import Pyro4, sys

nome = sys.argv[1].strip()

greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")
print(greeting_maker.get_fortune(nome))
