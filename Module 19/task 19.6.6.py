# Одна библиотека поручила вам написать программу для оцифровки словарей слов-синонимов.
# На вход в программу подаётся N пар слов. Каждое слово является синонимом к парному ему слову.
# Реализуйте код, который составляет словарь слов-синонимов (все слова в словаре различны),
# затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода:
# если такого слова нет, то выведите ошибку и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов.
#
# Пример:
# Введите количество пар слов: 3
# 1 пара: Привет - Здравствуйте
# 2 пара: Печально - Грустно
# 3 пара: Весело - Радостно
#
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет
def check_synonyms(word, dict_synonyms):
    temp_list = ''
    flag = True
    for i in dict_synonyms:
        temp_list = [x for x in dict_synonyms[i]]
        if word in temp_list:
            return_synonyms = [x for x in temp_list if x != word]
            flag = False
            return print('Синоним:', ' '.join(return_synonyms).title())
    if flag:
        return 'Такого слова нет в словаре!'

count = int(input('Введите количество пар слов: '))
dict_synonyms = dict()
for _ in range(count):
    print(_ + 1, 'пара: ', end= '')
    double = input('').lower().split(' ')
    dict_synonyms[_] = double
while True:
    check_word = input('Введите слово: ')
    result = check_synonyms(check_word, dict_synonyms)


