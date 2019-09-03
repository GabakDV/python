# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.
# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class ToyCartoon(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = "МультГерой"


class ToyAnimal(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Животное'


class ToyAdult(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self._type = 'Для взрослых'


class ToyFactory:
    def __init__(self, name, color, toy_type):
        Toy.__init__(self, name, color)
        self._buying()
        self._sewing()
        self._coloring()

    def _buying(self):
        print('Закупка метериалов')

    def _sewing(self):
        print('Пошив')

    def _coloring(self):
        print('Покраска игрушки')


def create_toy(name, color, toy_type):
    if toy_type == 'Животное':
         return ToyAnimal(name, color)
    elif toy_type == 'МультГерой':
        return ToyCartoon(name, color)
    else:
        return ToyAdult(name, color)


toy = create_toy ("Бегемот", "Розовый", "Животное")
print(isinstance(toy, ToyCartoon))
print(isinstance(toy, ToyAnimal))
print(isinstance(toy, Toy))

if isinstance(toy, ToyAdult):
    print("Запрещено для детей. 18+")
else:
    print('Детская игрушка')
