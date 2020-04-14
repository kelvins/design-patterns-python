# -*- coding: UTF-8 -*-

from datetime import date


class Item(object):
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal(object):
    def __init__(
        self,
        razao_social,
        cnpj,
        itens,
        data_de_emissao=date.today(),
        detalhes="",
        observadores=[],
    ):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception(
                "Detalhes da nota fiscal nao pode ter mais que 20 chars"
            )
        self.__detalhes = detalhes
        self.__itens = itens

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        return self.__itens


if __name__ == "__main__":

    from observadores import imprime, envia_por_email, salva_no_banco

    itens = [Item("ITEM A", 100), Item("ITEM B", 200)]

    nota_fiscal = Nota_fiscal(
        razao_social="FHSA Limitada",
        cnpj="01928391827321",
        itens=itens,
        data_de_emissao=date.today(),
        detalhes="",
        observadores=[imprime, envia_por_email, salva_no_banco],
    )
