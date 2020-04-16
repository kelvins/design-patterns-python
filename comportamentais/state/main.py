from abc import ABCMeta, abstractmethod


class EstadoOrcamento(metaclass=ABCMeta):
    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception("Orcamentos em aprovacao nao pode ser finalizado")


class Aprovado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser aprovado novamente")

    def reprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser reprovado")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orcamentos reprovados nao recebem desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser reprovado novamente")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orcamentos finalizados nao recebem desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamentos finalizado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamentos finalizado nao pode ser reprovado")

    def finaliza(self, orcamento):
        raise Exception(
            "Orcamentos finalizado nao pode ser finalizado novamente"
        )


class Orcamento:
    def __init__(self):
        self.__itens = list()
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)


class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":

    orcamento = Orcamento()

    orcamento.adiciona_item(Item("item 0", 100.0))
    orcamento.adiciona_item(Item("item 1", 50.0))
    orcamento.adiciona_item(Item("item 2", 400.0))

    print(orcamento.valor)

    orcamento.aprova()

    orcamento.aplica_desconto_extra()

    print(orcamento.valor)

    orcamento.finaliza()
