

class Subtracao(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()


class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()


class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == "__main__":

    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Soma(Numero(5), Numero(2))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    print expressao_conta.avalia()

    expressao_conta2 = Subtracao(Numero(100), Numero(70))
    print expressao_conta2.avalia()