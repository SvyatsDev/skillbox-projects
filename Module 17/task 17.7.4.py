# Дана строка, в которой хранятся первые семь букв английского алфавита.
# alphabet = 'abcdefg'
# Напишите программу, которая выводит на экран 10 вот таких результатов:
# 1.	Копия строки.
# 2.	Элементы строки в обратном порядке.
# 3.	Каждый второй элемент строки (включая самый первый).
# 4.	Каждый второй элемент строки после первого.
# 5.	Все элементы до второго.
# 6.	Все элементы, начиная с конца до предпоследнего.
# 7.	Все элементы в диапазоне индексов от 3 до 4 (не включая 4).
# 8.	Последние три элемента строки.
# 9.	Все элементы в диапазоне индексов от 3 до 4 (не включая 5).
# 10.	То же, что и в предыдущем пункте, но в обратном порядке.
# Для получения и вывода результатов используйте только команду print и срезы.
#
# Результаты работы программы:
#
# 1: abcdefg
# 2: gfedcba
# 3: aceg
# 4: bdf
# 5: a
# 6: g
# 7: d
# 8: efg
# 9: ed
# 10: de

alphabet = 'abcdefg'
new_alphabet = alphabet[::]
print(new_alphabet)
print(alphabet[::-1])
print(alphabet[0::2])
print(alphabet[1::2])
print(alphabet[:1])
print(alphabet[-1])
print(alphabet[3:4])
print(alphabet[-3::])
print(alphabet[3:5])
print(alphabet[4:2:-1])