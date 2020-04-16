from abc import ABCMeta, abstractmethod


class Theme(metaclass=ABCMeta):

    @abstractmethod
    def color(self):
        pass


class DarkTheme(Theme):

    def color(self):
        return 'Dark Black'


class LightTheme(Theme):

    def color(self):
        return 'Off White'


class AquaTheme(Theme):

    def color(self):
        return 'Light Blue'


class WebPage(metaclass=ABCMeta):

    @abstractmethod
    def content(self):
        pass


class About(WebPage):

    def __init__(self, theme):
        self.__theme = theme

    def content(self):
        return f'About page in {self.__theme.color()}'


class Careers(WebPage):

    def __init__(self, theme):
        self.__theme = theme

    def content(self):
        return f'Careers page in {self.__theme.color()}'


if __name__ == '__main__':
    dark_theme = DarkTheme()

    about = About(dark_theme)
    careers = Careers(dark_theme)

    print(about.content())
    print(careers.content())
