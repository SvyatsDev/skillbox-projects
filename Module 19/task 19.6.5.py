# Мы уже писали программу для лингвистов, которая получала на вход текст и считала,
# сколько раз в строке встречается каждый символ. Теперь задача немного поменялась:
# максимальную частоту выводить не нужно, однако теперь необходимо написать функцию,
# которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота,
# а в качестве значения — список символов с этой частотой. Реализуйте такую программу.
#
# Пример:
# Введите текст: Здесь что-то написано
# Оригинальный словарь частот:
#   : 2
# - : 1
# З : 1
# а : 2
# д : 1
# е : 1
# и : 1
# н : 2
# о : 3
# п : 1
# с : 2
# т : 2
# ч : 1
# ь : 1
#
# Инвертированный словарь частот:
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
# 2 : ['с', ' ', 'т', 'н', 'а']
# 3 : ['о']
def revers_dict(dict_text):
    revers_new_dict = dict()
    for _ in dict_text.values():
        revers_new_dict[_] = 0
    temp_list = list()
    for i_key in revers_new_dict:
        temp_list = [i for i in dict_text.keys() if dict_text[i] == i_key]
        revers_new_dict[i_key] = temp_list
        temp_list = ''
    return revers_new_dict
text = input('Введите текст: ').lower()
text_dict = dict()
for i in text:
    if i in text_dict.keys():
        text_dict[i] += 1
    else:
        text_dict[i] = 1
print(text_dict)
revers_text = revers_dict(text_dict)
for i_key in revers_text.keys():
    print(i_key, ':', revers_text.get(i_key))