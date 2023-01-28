# Илья зашёл на один любительский киносайт, где пользователи пишут рецензии на фильмы.
# Вот, кстати, список этих фильмов:
#
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

new_films = []
len_films = len(films)
while True:

    choice_film = input('\nВведите название фильма: ')
    for i in range(len_films):

        if films[i] == choice_film:
            new_films.append(choice_film)
            break
        else:
            print('Ошибка! Такого фильма не существует.')
            break
    print('Новый список фильмов: ', new_films)

