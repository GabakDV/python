# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math

old_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []
print("Задание 1")
for i in old_list:
    if i > 0 and math.sqrt(i) % 1 == 0:
        new_list.append(int(math.sqrt(i)))
print(new_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
date = '02.11.2013'
date_list = date.split('.')
dict_months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}
dict_days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвёртое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвёртое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое',
}
print("Задание 2")
for key in dict_days:
    if date_list[0] == key:
        date_list[0] = dict_days[key]

for key in dict_months:
    if date_list[1] == key:
        date_list[1] = dict_months[key]

answer_date = date_list[0] + ' ' + date_list[1] + ' ' + date_list[2] + ' ' "года"

print(answer_date)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
print("Задание 3")
n = int(input('Введите необходимое количество случайных чисел в списке:\n'))
n_list = []

for i in range(n):
    n_list.append(random.randint(-100,100))
print(n_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
#А
random_list = [1, 2, 4, 5, 6, 2, 5, 2]
new_list = set(random_list)
print("Задание 4А")

print(new_list)
#Б
orig_list = []

for item in random_list:
    if random_list.count(item) == 1:
        orig_list.append(item)
print("Задание 4Б")
print(orig_list)