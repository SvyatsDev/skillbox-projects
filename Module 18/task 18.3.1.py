# Усовершенствуйте старую программу:
# У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения,
# который вводится уже в одну строку. Напишите программу, которая посчитает, сколько раз слова пользователя встречаются в тексте.
#

words = input('Введите 3 слова для проверки: ').split()
text = input('Введите текст произведения: ').split()
count = [0 for _ in words]
for i_words in words:
    for i_text in text:
        if i_words == i_text:
            count[words.index(i_words)] += 1
result = ['---'. join([words[i_count], str(count[i_count])]) for i_count in range(len(count))]

print(result)
