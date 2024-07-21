from warehouse import Warehouse
from person import Person
import Pyro4
import sys

if sys.version_info<(3,0):
    input = raw_input

uri = input("Digite o URI do armazém: ").strip()
armazem = Pyro4.Proxy(uri)

armazem = Warehouse()
Luan = Person("Luan")
Leonardo = Person("Leonardo")
Luan.visitante(armazem)
Leonardo.visitante(armazem)