# -*- encoding: UTF-8 -*-

# Exemplo de aplicação do padrão Singleton utilizando metaclasses


class MetaSingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(object):

    __metaclass__ = MetaSingleton

    def __init__(self, x):
        self.x = x

if __name__ == "__main__":

    logger1 = Logger(1)
    logger2 = Logger(2)

    print(logger1)
    print(logger1.x)
    print(logger2)
    print(logger2.x)