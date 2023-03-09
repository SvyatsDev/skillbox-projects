# Мы поддерживаем свой киносайт и хотим сделать так, чтобы пользователи после регистрации могли создать собственный
# рейтинг фильмов из тех, которые есть на сайте. Вот сам список фильмов (конечно же, можете брать свои):
# Напишите программу, которая позволяет добавлять в свой рейтинг фильмы, удалять их оттуда, а также вставлять
# на нужное пользователю место. Обеспечьте контроль ввода и сделайте так, чтобы в список нельзя было добавить
# один и тот же фильм несколько раз.

# Пример:
# Ваш текущий топ фильмов: []
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: добавить
def is_film_exist(x, y):
    for _ in y:
        if _ == x:
            return True
    return False


def is_same_film(check_film, list_film):
    for _ in list_film:
        if _ == check_film:
            return True
    return False


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
top_films = []
while True:
    print('Ваш текущий список фильмов: ', top_films)
    new_film = input('Название фильма: ')
    if is_film_exist(new_film, films):
        print('Команды: добавить, вставить, удалить.')
        command = input('Введите команду: ')
        if command == 'добавить':
            if is_same_film(new_film, top_films):
                print('Такой фильм уже есть в списке')
            else:
                top_films.append(new_film)
        if command == 'вставить':
            if is_same_film(new_film, top_films):
                print('Такой фильм уже есть в списке')
            else:
                place = input('После какого фильма вставить: ')
                top_films.insert(top_films.index(place) + 1 , new_film)
        if command == 'удалить':
            top_films.remove(new_film)
    else:
        print('Такого фильма нет на сайте')