# -*- encoding: UTF-8 -*-

# Duas maneiras diferentes de criar um unico objeto utilizando o padrao Singleton


class Singleton1(object):

    __instance = None

    def __new__(cls, nome):
        if Singleton1.__instance is None:
            Singleton1.__instance = object.__new__(cls)
            Singleton1.__instance.__nome = nome

        return Singleton1.__instance

    @property
    def nome(self):
        return self.__nome


class Singleton2(object):

    def __new__(cls, nome):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton2, cls).__new__(cls)
            cls.instance.__nome = nome
        return cls.instance

    @property
    def nome(self):
        return self.__nome

if __name__ == "__main__":

    foo = Singleton1("Maria")
    print(foo.nome)
    print(foo)

    bar = Singleton1("Joao")
    print(bar.nome)
    print(bar)

    print(foo is bar)

    foo = Singleton2("Maria")
    print(foo.nome)
    print(foo)

    bar = Singleton2("Joao")
    print(bar.nome)
    print(bar)

    print(foo is bar)