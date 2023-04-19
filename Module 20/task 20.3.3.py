 # Один заказчик попросил нас написать небольшой скрипт для своих криптографических нужд.
 # При этом он заранее предупредил, что скрипт должен уметь работать с любым итерируемым типом данных.
 # Напишите функцию, которая возвращает список из элементов итерируемого объекта
 # (кортежа, строки, списка, словаря), у которых индекс чётный.
 #
 # Пример 1:
 # Допустим, есть такая строка: 'О Дивный Новый мир!'
 #
 # Результат: ['О', 'Д', 'в', 'ы', ' ', 'о', 'ы', ' ', 'и', '!']
 #
 # Пример 2:
 # Допустим, есть такой список: [100, 200, 300, 'буква', 0, 2, 'а']
 #
 # Результат: [100, 300, 0, 'а']
 #
 # Примечание: для проверки типа можно использовать функцию
 # isinstance(<элемент>, <тип данных>), которая возвращает True, если элемент принадлежит к этому типу данных, и возвращает False в противном случае.
def check_object_type(text):
    if isinstance(text, list):
        print('Допустим есть такой список: ', text)
        text_list = [i_char for i_idx, i_char in enumerate(text) if i_idx % 2 == 0]
        print('Результат: ', text_list)
    if isinstance(text, tuple):
        print('Допустим есть такой кортеж: ', text)
        text_list = [i_char for i_idx, i_char in enumerate(text) if i_idx % 2 == 0]
        text_tuple = tuple(text_list)
        print('Результат: ', text_tuple)
    if isinstance(text, dict):
        print('Допустим есть такой словарь: ', text)
        text_dict = {text[i_name] for i_idx, i_name in enumerate(text) if i_idx % 2 == 0}
        print('Результат: ', text_dict)
    if isinstance(text, str):
        print('Допустим есть такая строка: ', text)
        text_list = [i_char for i_idx, i_char in enumerate(text) if i_idx % 2 == 0]
        print('Результат: ', ' '.join(text_list))

text_list = [100, 200, 300, 'буква', 0, 2, 'а']
text_str = 'О Дивный Новый мир!'
text_dict = {'илья': 'пеперони', 'олег': 'моцарела', 'виктор': 'грибы'}
text_tuple = (1,2,3,4,5,6,7)
new_text_list = check_object_type(text_list)
new_text_str = check_object_type(text_str)
new_text_dict = check_object_type(text_dict)
new_text_tuple = check_object_type(text_tuple)


