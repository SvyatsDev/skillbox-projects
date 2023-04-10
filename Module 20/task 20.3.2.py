# /Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться).
# Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.
# Подсказка: random
#
# Пример:
# Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']
# Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']
#
# Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}
# Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
import random
alphabet_rus = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'.split(',')
first_list = [random.choice(alphabet_rus) for _ in range(10)]
second_list = [random.choice(alphabet_rus) for _ in range(10)]
first_dict = {i_key: i_name for i_key, i_name in enumerate(first_list)}
second_dict = {i_key: i_name for i_key, i_name in enumerate(second_list)}
print(first_list)
print(second_list)

print()
print(first_dict)
print(second_dict)