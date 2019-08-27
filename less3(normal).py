# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


people = ['Igor', 'Denis', 'Artem', 'Alex', 'Viktor', 'Aleksey']
people_bax = [12000, 15000, 710000, 17000, 13500, 1000000]

salary = dict(zip(people, people_bax))
print(salary)
file = open("salary.txt", 'w', encoding='utf-8')

for key, val in salary.items():
    file.write(f"{key} - {val}\n")

file_read = open("salary.txt", encoding="utf-8")
for line in file_read:
    list_line = line.split("-")
    print(list_line)

file.close()
file_read = open("salary.txt", encoding="utf-8")
for line in file_read:
    list_line = line.split("-")
    print(list_line)
file.close()

for i in salary:
    salary[i] = round(int(salary[i]) * 0.87)
    if salary[i] > 500000:
        continue
    salary_2 = i.upper() + " - " + str(salary[i])
    print(salary_2)