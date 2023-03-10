# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по
# алфавиту через K позиций по кругу. Если взять русский алфавит и k = 3, то в слове, которое мы хотим зашифровать,
# буква А станет буквой Г, Б станет Д и так далее.
#
# Пользователь вводит сообщение, а также значение сдвига. Напишите программу, которая зашифрует это сообщение при помощи шифра Цезаря.
#
# Пример:
# Введите сообщение: это питон
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
text = list(input('Введите сообщение которое надо зашифровать: '))
step = int(input('Введите сдвиг: '))
hiden_text = ''
# new_text = []
# idx = 0
# for i in text:
#     if i == ' ':
#         new_text.append(' ')
#     else:
#         idx = (alphabet.index(i) + step - 1) % len(alphabet)
#         new_text.append(alphabet[idx])
new_text = [' ' if i == ' ' else alphabet[(alphabet.index(i) + step) % len(alphabet)] for i in text]
for _ in new_text:
    hiden_text += _
print('Зашифрованное сообщение: ', hiden_text)




