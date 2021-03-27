from abc import ABCMeta, abstractmethod
from datetime import date


class Pedido:
    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__status = 'FINALIZADO'
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


class Comando(metaclass=ABCMeta):
    @abstractmethod
    def executa(self):
        pass


class PagaPedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


class FinalizaPedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()


class FilaTrabalho:
    def __init__(self):
        self.__comandos = list()

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


if __name__ == '__main__':

    pedido1 = Pedido('Joao', 200.0)
    pedido2 = Pedido('Ana', 400.0)

    fila = FilaTrabalho()

    comando1 = FinalizaPedido(pedido1)
    comando2 = PagaPedido(pedido1)
    comando3 = FinalizaPedido(pedido2)

    fila.adiciona(comando1)
    fila.adiciona(comando2)
    fila.adiciona(comando3)

    fila.processa()

    print(pedido1.status)
    print(pedido2.status)
