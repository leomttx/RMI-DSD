from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input

class Person(object):
    def __init__(self, name):
        self.name = name

    def visitante(self, warehouse):
        print("Olá, eu sou {0}".format(self.name))
        self.deposito(warehouse)
        self.pegar(warehouse)
        print("Obrigado e adeus!")

    def deposito(self, warehouse):
        print("O armazém contém:", warehouse.list_contents())
        item = input("Digite o item que você deseja armazenar: ").strip()
        if item:
            warehouse.store(self.name, item)

    def pegar(self, warehouse):
        print("O armazém contém:", warehouse.list_contents())
        item = input("Digite o item que você deseja pegar: ").strip()
        if item:
            warehouse.take(self.name, item)