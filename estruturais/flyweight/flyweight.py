class KarakTea(object):
    def __init__(self, tea_type):
        self.__tea_type = tea_type

    @property
    def tea_type(self):
        return self.__tea_type


class TeaMaker(object):
    def __init__(self):
        self.__available_tea = dict()

    def make(self, preference):

        if preference not in self.__available_tea:
            self.__available_tea[preference] = KarakTea(preference)

        return self.__available_tea[preference]


class TeaShop(object):
    def __init__(self, tea_maker):
        self.__orders = dict()
        self.__tea_maker = tea_maker

    def take_order(self, tea_type, table):

        if table not in self.__orders:
            self.__orders[table] = list()

        self.__orders[table].append(self.__tea_maker.make(tea_type))

    def serve(self):
        for table, orders in self.__orders.items():
            print("Serving tea to table {}".format(table))


if __name__ == "__main__":
    tea_maker = TeaMaker()
    shop = TeaShop(tea_maker)

    shop.take_order("red tea", 1)
    shop.take_order("red tea more sugar", 2)
    shop.take_order("red tea more milk", 3)

    shop.serve()
