# Пользователь вводит строку, которая, возможно, содержит пробелы. Напишите программу,
# которая извлекает из этой строки все символы, являющиеся цифрами и составляет из них новую строку.
#
# Пример:
# Введите строку: пр6и89вет
#
# Цифры: 689
#
text = input('Введите строку: ')
new_text = [i for i in text if i.isdigit()]
print('Цифры: ', ''.join(new_text))