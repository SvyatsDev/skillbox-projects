# Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент (его можно вводить с клавиатуры).
# Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе — вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж,
# который начинается с него и идёт до конца исходного.
#
def check_elem(tuple_1, random_elem):
    count_elem = [i for i in tuple_1 if i == random_elem]
    if len(count_elem) == 0:
        return tuple()
    if len(count_elem) == 1:
        elem_idx = [i_idx for i_idx, i_name in enumerate(tuple_1) if i_name == random_elem]
        return tuple_1[elem_idx[0]::]
    if len(count_elem) >= 2:
        elem_idx = [i_idx for i_idx, i_name in enumerate(tuple_1) if i_name == random_elem]
        return tuple_1[elem_idx[0]:elem_idx[1] + 1]


sample_tuple = ('1','2','4','4','4','5','5','6','8')
elem = input('Введите элемент: ')
print(check_elem(sample_tuple, elem))