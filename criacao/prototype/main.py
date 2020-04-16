import copy


class Sheep:

    def __init__(self, name, category='Mountain Sheep'):
        self.name = name
        self.category = category


if __name__ == '__main__':
    original_sheep = Sheep('Jolly')
    print(original_sheep.name)
    print(original_sheep.category)

    cloned_sheep = copy.deepcopy(original_sheep)
    cloned_sheep.name = 'Dolly'
    print(cloned_sheep.name)
    print(cloned_sheep.category)
