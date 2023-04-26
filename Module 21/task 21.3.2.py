# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id.
# Видя, как он мучается, вы решили добить помочь ему и объяснить эту тему наглядно.
#
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
# информацию о его изменяемости, а также id этого объекта.
#
# Пример 1:
# Введите данные: привет
#
# Тип данных: str (строка)
# Неизменяемый (immutable)
# Id объекта: 1705156583984
#
# Пример 2:
# Введите данные: {‘a’: 10, ‘b’: 20}
#
# Тип данных: dict (словарь)
# Изменяемый (mutable)
# Id объекта: 1705205308536
#

while True:
    text = input('Введите данные: ').format()
    if isinstance(text, str):
        print('Тип данных str (строка)')
        print('Неизменяемый (immutable)')
        print('Id объекта: ', id(text))
    if isinstance(text, int):
        print('Тип данных int (целое число)')
        print('Неизменяемый (immutable)')
        print('Id объекта: ', id(text))
    if isinstance(text, float):
        print('Тип данных float (вещественное число)')
        print('Неизменяемый (immutable)')
        print('Id объекта: ', id(text))
    if isinstance(text, bool):
        print('Тип данных bool (тип данных True or False)')
        print('Неизменяемый (immutable)')
        print('Id объекта: ', id(text))
    if isinstance(text, tuple):
        print('Тип данных tuple (кортеж)')
        print('Неизменяемый (immutable)')
        print('Id объекта: ', id(text))
    if isinstance(text, dict):
        print('Тип данных dict (словарь)')
        print('Изменяемый (mutable)')
        print('Id объекта: ', id(text))
    if isinstance(text, list):
        print('Тип данных list (список)')
        print('Изменяемый (mutable)')
        print('Id объекта: ', id(text))
    if isinstance(text, set):
        print('Тип данных set (множество)')
        print('Изменяемый (mutable)')
        print('Id объекта: ', id(text))
