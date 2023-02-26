# N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание,
# где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.
#
# На вход подаётся количество человек N и номер K. Напишите программу, которая выводит число от 1 до N — это номер человека,
# который останется в кругу последним.
#
# Пример:
# Кол-во человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7 человек
#
# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2
#
# Текущий круг людей: [1, 3, 4, 5]
# Начало счёта с номера 3
# Выбывает человек под номером 5
#
# Текущий круг людей: [1, 3, 4]
# Начало счёта с номера 1
# Выбывает человек под номером 1
#
# Текущий круг людей: [3, 4]
# Начало счёта с номера 3
# Выбывает человек под номером 3
#
# Остался человек под номером 4

n = int(input('Введите количество человек: '))
list_people = list(range(1, n + 1))
idx = 0
k = int(input('Какое число в считалке: '))
print('Значит выбывает каждый', k, 'человек')
print('\nТекущий круг людей: ', list_people)
print('Начало счета с номера: ', list_people[0])
while len(list_people) > 1:
    idx = (idx + k - 1) % len(list_people)
    print('Выбывает человек под номером: ', list_people[idx])
    list_people.remove(list_people[idx])
    print('Текущий круг людей: ', list_people)
    print('Начало счета с номера: ', list_people[0])