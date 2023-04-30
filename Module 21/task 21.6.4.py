# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень,
# до которого будет просматриваться структура. Напишите функцию, которая находит заданный пользователем
# ключ в словаре и выдаёт значение этого ключа на экран. По умолчанию уровень не задан.
# В качестве примера можно использовать такой словарь:

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search_key(dict_x, key, depth=None):
    if depth == None:
        if key in dict_x:
            return dict_x[key]
        for i_name in dict_x.values():
            if isinstance(i_name, dict):
                result = search_key(i_name, key, depth)
                if result:
                    break
        else:
            result = None
        return result
    if abs(depth) > 0:
        if key in dict_x:
            return dict_x[key]
        for i_key, i_name in dict_x.items():
            if isinstance(i_name, dict):
                result = search_key(i_name, key, abs(depth) - 1)
                if result:
                    break
        else: result = None
        return result
    if depth == 0:
        return None
word = input('Введите значение для поиска: ')
result = search_key(site, word, -2)
if result:
    print('Значение: ', result)
else:
    print('Значение не найдено!')
