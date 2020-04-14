# -*- encoding: UTF-8 -*-


class Colaborador(object):

    def __init__(self, nome, salario):
        self.__nome = nome
        self.salario = salario

    @property
    def nome(self):
        return self.__nome


class Desenvolvedor(Colaborador):

    def __init__(self, nome, salario, outro_parametro=None):
        super(Desenvolvedor, self).__init__(nome, salario)
        self.__outro_parametro = outro_parametro

    @property
    def outro_parametro(self):
        return self.__outro_parametro


class Designer(Colaborador):

    def __init__(self, nome, salario, mais_um_parametro=None):
        super(Designer, self).__init__(nome, salario)
        self.__mais_um_parametro = mais_um_parametro

    @property
    def mais_um_parametro(self):
        return self.__mais_um_parametro


class Organizacao(object):

    def __init__(self):
        self.__colaboradores = list()

    def add_colaborador(self, colaborador):
        self.__colaboradores.append(colaborador)

    def total_salarios(self):
        salarios = 0

        for colaborador in self.__colaboradores:
            salarios += colaborador.salario

        return salarios


if __name__ == '__main__':
    joao = Desenvolvedor('Joao da Silva', 1800)
    carla = Designer('Carla Camila', 1900)

    organizacao = Organizacao()
    organizacao.add_colaborador(joao)
    organizacao.add_colaborador(carla)

    print('Total salários: {}'.format(organizacao.total_salarios()))
