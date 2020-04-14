# -*- coding: UTF-8 -*-

from descontos import (
    Desconto_por_cinco_itens,
    Desconto_por_mais_de_quinhentos_reais,
    Sem_desconto,
)


class Calculador_de_descontos(object):
    def calcula(self, orcamento):

        return Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
        ).calcula(orcamento)


if __name__ == "__main__":

    from orcamento import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item("item 0", 100.0))
    orcamento.adiciona_item(Item("item 1", 100.0))
    orcamento.adiciona_item(Item("item 2", 100.0))
    orcamento.adiciona_item(Item("item 3", 100.0))
    orcamento.adiciona_item(Item("item 4", 100.0))
    orcamento.adiciona_item(Item("item 5", 100.0))
    orcamento.adiciona_item(Item("item 6", 100.0))
    orcamento.adiciona_item(Item("item 7", 100.0))
    orcamento.adiciona_item(Item("item 8", 100.0))
    orcamento.adiciona_item(Item("item 9", 100.0))

    print(orcamento.valor)

    calculator = Calculador_de_descontos()

    desconto = calculator.calcula(orcamento)

    print("Desconto calculado %s" % desconto)
