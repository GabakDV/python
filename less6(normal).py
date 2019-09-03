# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)
        self.armor = int(armor)

    def _attack_value(self, who_att, who_def):  # Функция возвращает урон с учетом брони противника
        who_att_k = who_att.damage / who_def.armor
        return who_att_k

    def attack(self, who_att, who_def):  # Функция наносит этот самый урон
        who_def.health -= self._attack_value(who_att, who_def)



class Hero(Person):
    pass


class Enemy(Person):
    pass


class War():
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.hit(hero, enemy)

    def hit(self, hero, enemy):
        while hero.health > 0 and enemy.health > 0:
            hero.attack(hero, enemy)
            print('Игрок {} нанес урон. У игрока {} осталось {} здоровья.'.format(hero.name, enemy.name, enemy.health))

            if enemy.health > 0:
                enemy.attack(enemy, hero)
                print('Игрок {} нанес урон. У игрока {} осталось {} здоровья.'.format(enemy.name, hero.name, hero.health))

        print('*' * 36)

        if hero.health > 0:
            print('Игрок {} выиграл! Осталось {} здоровья.'.format(hero.name, hero.health))
        else:
            print('Игрок {} выиграл! Осталось {} здоровья.'.format(enemy.name, enemy.health))


hero = Hero('IronMan', 1000, 50, 2)
enemy = Enemy('Tanos', 500, 60, 2.5)
war1 = War(hero, enemy)