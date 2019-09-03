# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
name_player = input('Введите имя своего героя: ')
name_enemy = input('Введите имя своего врага: ')
game_player = {'name': name_player, 'health': 100, 'damage': 75}
game_enemy = {'name': name_enemy, 'health': 100, 'damage': 50}

def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']
    print('{}. получил урон, в размере: {}. Текущие очки жизни составляет: ' '{}'.format(game_enemy['name'], game_player['damage'], game_enemy['health']))

attack(game_player, game_enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

print("вторая задача")

game_player['health'] = 250
game_enemy['health'] = 250
game_player['armor'] = 1.2
game_enemy['armor'] = 1.2

def defense(damage, armor):
    damage /= armor
    return damage

def commentator(person1, person2):
    print('{}. получил урон, в размере: {}. Текущие очки жизни составляет: ' '{}'.format(person2['name'], person1['damage'], person2['health']))

def attack(person1, person2):
    person2['health'] = person2['health'] - (defense(person1['damage'], person2['armor']))

def alive(person):
    if person['health'] > 0:
        return True
    else:
        return False

def winner(person):
    print('Победа за :', person['name'])

def save_game_entity(entity):
    with open(entity['name'] + '.txt', 'w', encoding='UTF-8') as file:
        for key, value in entity.items():
            file.write('{} {}\n'.format(key, value))

def load_game_entity(entity):
    with open(entity['name'] + '.txt', 'r', encoding='UTF-8') as file:
        buffer_dick = {}
        buffer = []
        for line in file:
            buffer = line.split()
            if buffer[0] == 'name':
                buffer_dick[buffer[0]] = buffer[1]
            elif buffer[0] == 'armor':
                buffer_dick[buffer[0]] = float(buffer[1])
            else:
                buffer_dick[buffer[0]] = int(buffer[1])
        return buffer_dick

# Сохранения данных
save_game_entity(game_player)
save_game_entity(game_enemy)

# Загрузка данных
game_player = load_game_entity(game_player)
game_enemy = load_game_entity(game_enemy)

# Игровая сессия
while True:
    pause = input('Нажмите Enter, чтобы продолжить текущий бой')
    if alive(game_player):
        attack(game_player, game_enemy)
        commentator(game_player, game_enemy)
        if alive(game_enemy):
            pause = input('Нажмите Enter, чтобы продолжить текущий бой')
            attack(game_enemy, game_player)
            commentator(game_enemy, game_player)
        else:
            winner(game_player)
            break
    else:
        winner(game_enemy)
        break

print('Конец игры')