from descontos import (
    DescontoCincoItens, DescontoMaisDeQuinhentosReais, SemDesconto
)


class CalculadorDescontos:

    def calcula(self, orcamento):
        return DescontoCincoItens(
            DescontoMaisDeQuinhentosReais(SemDesconto())
        ).calcula(orcamento)


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('item 0', 100.0))
    orcamento.adiciona_item(Item('item 1', 100.0))
    orcamento.adiciona_item(Item('item 2', 100.0))
    orcamento.adiciona_item(Item('item 3', 100.0))
    orcamento.adiciona_item(Item('item 4', 100.0))
    orcamento.adiciona_item(Item('item 5', 100.0))
    orcamento.adiciona_item(Item('item 6', 100.0))
    orcamento.adiciona_item(Item('item 7', 100.0))
    orcamento.adiciona_item(Item('item 8', 100.0))
    orcamento.adiciona_item(Item('item 9', 100.0))

    print(orcamento.valor)

    calculator = CalculadorDescontos()

    desconto = calculator.calcula(orcamento)

    print(f'Desconto calculado {desconto}')
