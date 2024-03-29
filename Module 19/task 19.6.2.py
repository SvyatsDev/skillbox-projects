# Антон помимо программирования также увлекается и географией, поэтому он решил связать эти две области и написать
# для своего проекта небольшую программу-навигатор.
#
# Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся, в одну строку.
# Затем пользователь вводит три названия городов. Реализуйте такую программу и для каждого из трёх городов укажите,
# в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.
#
# Пример:
# Кол-во стран: 2
# 1 страна: Россия Москва Петербург Новгород
# 2 страна: Германия Берлин Лейпциг Мюнхен
#
# 1 город: Москва
# Город Москва расположен в стране Россия.
#
# 2 город: Мюнхен
# Город Мюнхен расположен в стране Германия.
#
# 3 город: Рим
# По городу Рим данных нет.
countries_dict = dict()
count_countries = int(input('Количество стран: '))
for _ in range(count_countries):
    print(_ + 1, 'страна', end= ' ')
    name_country_towns = input().split()
    print(name_country_towns)
    for i in name_country_towns[1::]:
        countries_dict[i] = name_country_towns[0]
    print(countries_dict)
for x in range(3):
    print(x + 1, 'город: ', end= '')
    town = input()
    if town in countries_dict.keys():
        print(f'Город {town} расположен в стране:', countries_dict[town])
    else:
        print(f'По городу {town} данных нет:')
