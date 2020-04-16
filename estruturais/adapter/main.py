from abc import ABCMeta, abstractmethod


class Lion(metaclass=ABCMeta):

    @abstractmethod
    def roar(self):
        pass


class AfricanLion(Lion):

    def roar(self):
        print('African Lion')


class AsianLion(Lion):

    def roar(self):
        print('Asian Lion')


class Hunter:

    def hunt(self, lion):
        lion.roar()


class WildDog:

    def bark(self):
        print('Wild Dog')


class WildDogAdapter(Lion):

    def __init__(self, wild_dog):
        self.__wild_dog = wild_dog

    def roar(self):
        self.__wild_dog.bark()


if __name__ == '__main__':

    african_lion = AfricanLion()
    asian_lion = AsianLion()
    wild_dog = WildDog()

    wild_dog_adapter = WildDogAdapter(wild_dog)

    hunter = Hunter()
    hunter.hunt(african_lion)
    hunter.hunt(asian_lion)
    hunter.hunt(wild_dog_adapter)
