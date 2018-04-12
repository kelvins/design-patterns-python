
# -*- encoding: UTF-8 -*-

# abc = abstract class
# Ao utilizar o abstractmethod decorator obrigamos as classes filhas a implementarem os métodos
from abc import ABCMeta, abstractmethod


class Template_de_impostos_condicional(object):
    """
    Classe abstrata.
    """
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS(object):

    def calcula(self, orcamento):

        return orcamento.valor * 0.1


class ICMS(object):

    def calcula(self, orcamento):

        return orcamento.valor * 0.06


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
