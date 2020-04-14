
# -*- encoding: UTF-8 -*-

# abc = abstract class
# Ao utilizar o abstractmethod decorator obrigamos as classes filhas a implementarem os métodos
from abc import ABCMeta, abstractmethod


class Imposto(object):

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if self.__outro_imposto is not None:
            return self.__outro_imposto.calcula(orcamento)
        else:
            return 0

    @abstractmethod
    def calcula(self, orcamento):
        pass


class Template_de_impostos_condicional(Imposto, metaclass=ABCMeta):
    """
    Classe abstrata.
    """

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


def IPVX(metodo_ou_funcao):
    # Chama o calculo do imposto ISS, pega o resultado e soma com R$ 50,00
    # O wrapper eh chamado antes do calcula do ISS
    # Recebe o self do ISS, onde o decorator esta aplicado
    # metodo_ou_funcao sera o metodo calcula
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50.0
    return wrapper


class ISS(Imposto):

    @IPVX
    def calcula(self, orcamento):

        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):

    def calcula(self, orcamento):

        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)


class ICPP(Template_de_impostos_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):

        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):

        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):

        return orcamento.valor * 0.05


class IKCV(Template_de_impostos_condicional):

    def __tem_item_maior_que_cem_reais(self, orcamento):

        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

    def deve_usar_maxima_taxacao(self, orcamento):

        return orcamento.valor > 500 and self.__tem_item_maior_que_cem_reais(orcamento)

    def maxima_taxacao(self, orcamento):

        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):

        return orcamento.valor * 0.06
