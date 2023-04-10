# Задача 1. Создание кортежей
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав тем
# самым третий кортеж. С помощью метода кортежа определите в нём количество нулей.
# Выведите на экран третий кортеж и количество нулей в нём.
import random
first_list = [random.randint(0,5) for _ in range(10)]
print(first_list)
second_list = [random.randint(-5,0) for _ in range(10)]
print(second_list)
third_list = []
third_list.extend(first_list)
third_list.extend(second_list)
print(third_list)
third_tuple = tuple(third_list)
print('Третий кортеж: ', third_tuple)
print('Количество нулей в третьем кортеже: ', third_tuple.count(0))