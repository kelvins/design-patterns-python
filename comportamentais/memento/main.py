from datetime import date


class Contrato:
    def __init__(self, data, cliente, tipo):
        self.data = data
        self.cliente = cliente
        self.tipo = tipo

    def avanca(self):
        if self.tipo == "NOVO":
            self.tipo = "EM ANDAMENTO"
        elif self.tipo == "EM ANDAMENTO":
            self.tipo = "ACERTADO"
        elif self.tipo == "ACERTADO":
            self.tipo = "CONCLUIDO"

    def salva_estado(self):
        # Não podemos passar o self para o Estado pois se o contrato fosse
        # alterado o estado anterior dele também seria alterado
        return Estado(
            Contrato(data=self.data, cliente=self.cliente, tipo=self.tipo)
        )

    def restaura_estado(self, estado):
        self.cliente = estado.contrato.cliente
        self.data = estado.contrato.data
        self.tipo = estado.contrato.tipo


class Estado:
    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato


class Historico:
    def __init__(self):
        self.__estados_salvos = list()

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)


if __name__ == "__main__":

    historico = Historico()

    contrato = Contrato(data=date.today(), cliente="Kelvin", tipo="NOVO")

    contrato.avanca()

    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()

    contrato.cliente = "Joao da Silva"

    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()

    historico.adiciona_estado(contrato.salva_estado())

    print(contrato.tipo)
    print(contrato.cliente)

    contrato.restaura_estado(historico.obtem_estado(0))

    print(contrato.tipo)
    print(contrato.cliente)
