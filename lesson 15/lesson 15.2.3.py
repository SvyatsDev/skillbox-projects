# Задача 3. Собачьи бега
# В собачьих бегах участвует N собак, у каждой из них есть определённое количество очков за сезон.
# На огромном табло выводятся очки каждой собаки. Однако при выводе был обнаружен баг:
# собаки с наибольшим и наименьшим количеством очков поменялись местами! Нужно это исправить.
# Дан список очков из N собак. Напишите программу, которая меняет местами наибольший и наименьший элементы в списке.

n = int(input('Введите количество собак: '))
dog_list = []

for _ in range(n):
    score = int(input('Введите очки собаки: '))
    dog_list.append(score)

min_score = dog_list[0]
max_score = dog_list[0]
i_min = 0
i_max = 0

for i_score in range(n):
    if min_score > dog_list[i_score]:
        min_score = dog_list[i_score]
        i_min = i_score
    if max_score < dog_list[i_score]:
        max_score = dog_list[i_score]
        i_max = i_score
print('\nТаблица очков', dog_list)
print('==========')
dog_list[i_max] = min_score
dog_list[i_min] = max_score
print('Новый список: ', dog_list)


