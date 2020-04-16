from datetime import date


class Item:
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class NotaFiscal:
    def __init__(
        self,
        razao_social,
        cnpj,
        itens,
        data_de_emissao=date.today(),
        detalhes="",
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

    from criador_de_nota_fiscal import CriadorNotaFiscal

    itens = [Item("ITEM A", 100), Item("ITEM B", 200)]

    nota_fiscal = NotaFiscal(
        razao_social="FHSA Limitada",
        cnpj="01928391827321",
        itens=itens,
        data_de_emissao=date.today(),
        detalhes="",
    )

    nota_fiscal_criada_com_builder = (
        CriadorNotaFiscal()
        .com_razao_social("FHSA Limitada")
        .com_cnpj("01928391827321")
        .com_itens(itens)
        .constroi()
    )
