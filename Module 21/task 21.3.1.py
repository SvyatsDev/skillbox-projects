# В одном проекте на 10 000 строк кода произошла критическая ошибка. Хорошо, что
# старший разработчик быстро её нашёл и исправил. Он решил проверить, смогли бы вы её исправить,
# если бы его не было на месте. Поэтому он написал для вас код с аналогичной ошибкой:
#
# import random
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
#
# change_dict(common_dict)
# print(common_dict)
#
# Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых равны ранее объявленным переменным.
# Затем вызывается функция, которая должна изменять значения словаря, добавляя к значениям случайное число, в зависимости
# от типа данных. Но при этом меняются и ранее объявленные переменные. Исправьте эту ошибку и убедитесь, что nums_list, some_dict и uniq_nums не меняются.

import random

def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            list_copy = i_value.copy()
            list_copy.append(num)
            dct[i_key] = list_copy
        if isinstance(i_value, dict):
            dict_copy = i_value.copy()
            dict_copy[num] = i_key
            dct[i_key] = dict_copy
        if isinstance(i_value, set):
            set_copy = i_value.copy()
            set_copy.add(num)
            dct[i_key] = set_copy

# респисун(маример) 3мл 3мл декосан 3 раза в день
nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
change_dict(common_dict)
print(common_dict)
print(nums_list)
print(some_dict)
print(uniq_nums)