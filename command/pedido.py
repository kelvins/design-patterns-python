# -*- encoding: UTF-8 -*-

from datetime import date
from abc import ABCMeta, abstractmethod


class Pedido(object):

    def __init__(self, cliente, valor):

        self.__cliente = cliente
        self.__valor = valor
        self.__status = "NOVO"
        self.__data_finalizacao = None

    def paga(self):
        self.__status = "PAGO"

    def finaliza(self):
        self.__status = "FINALIZADO"
        self.__data_finalizacao = date.today()

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao


class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class Paga_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


class Finaliza_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()


class Fila_de_trabalho(object):

    def __init__(self):

        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()

if __name__ == "__main__":

    pedido1 = Pedido("Joao", 200.0)
    pedido2 = Pedido("Ana", 400.0)

    fila = Fila_de_trabalho()

    comando1 = Finaliza_pedido(pedido1)
    comando2 = Paga_pedido(pedido1)
    comando3 = Finaliza_pedido(pedido2)

    fila.adiciona(comando1)
    fila.adiciona(comando2)
    fila.adiciona(comando3)

    fila.processa()

    print pedido1.status
    print pedido2.status

