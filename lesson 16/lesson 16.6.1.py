# Вашему другу, который тоже начал изучать Python, преподаватель дал такую задачу: есть три списка — основной и два побочных. В основном лежат элементы [1, 5, 3], а в побочных [1, 5, 1, 5] и [1, 3, 1, 5, 3, 3] соответственно.
# Первый побочный закидывается в основной, там считается количество цифр 5, количество выводится на экран, и затем они удаляются из основного списка. После этого в основной закидывается второй побочный список, там считается количество цифр 3 и выводится на экран. В конце также выводится и сам список.
#
# Из интереса вы попросили вашего друга показать код его программы и поняли, что сделали это не зря — то, что вы увидели, повергло вас в шок и ужас. Вот сам код:
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)
#
# Используя знания о методах списков, а также о стиле программирования, помогите другу переписать программу. Не используйте дополнительные списки.
#
# Результат работы программы:
# Кол-во цифр 5 при первом объединении: 3
# Кол-во цифр 3 при втором объединении: 4
# Итоговый список: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]


a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
sum_5 = a.count(5)
for i in a:
    if i == 5:
        a.remove(i)
a.extend(c)
sum_3 = a.count(3)
print('Количество цифр 5 в первом случае: ', sum_5)
print('Количество цифр 3 во втором случае: ', sum_3)
print('Итоговый список: ', a)

