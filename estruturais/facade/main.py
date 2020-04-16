class Hotelier:

    def __init__(self):
        print('Arranging the Hotel for Marriage? --')

    def __is_available(self):
        print('Is the Hotel free for the event on given day?')
        return True

    def book_hotel(self):
        if self.__is_available():
            print('Registered the Booking\n')


class Florist:

    def __init__(self):
        print('Flowers decoration for the event? --')

    def set_flower_requirements(self):
        print('Carnations, Roses and Lilies would be used for decorations\n')


class Caterer:

    def __init__(self):
        print('Food Arrangements for the event? --')

    def set_cuisine(self):
        print('Chinese & Continental Cuisine to be served\n')


class Musician:

    def __init__(self):
        print('Musical arrangements for the marriage? --')

    def set_music_type(self):
        print('Jazz and Classical will be played\n')


class EventManager:

    def __init__(self):
        print('Event Manager:: Let me talk to the folks\n')

    @staticmethod
    def arrange():
        hotelier = Hotelier()
        hotelier.book_hotel()

        florist = Florist()
        florist.set_flower_requirements()

        caterer = Caterer()
        caterer.set_cuisine()

        musician = Musician()
        musician.set_music_type()


class Client:

    def __init__(self):
        print('Client:: Whoa! Marriage Arrangements???!!!')

    def ask_event_manager(self):
        print('Client:: Let's contact the event manager\n')
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('Client:: Thanks to Event Manager, all preparations done!')


if __name__ == '__main__':
    client = Client()
    client.ask_event_manager()
