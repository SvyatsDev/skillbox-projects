# На вход в программу подаётся строка, в которой буква h встречается как минимум два раза. Реализуйте код, который
# разворачивает последовательность символов, заключённую между первым и последним появлением буквы h, в противоположном порядке.

word = '222h44445555h11'
first_h = word.index('h')
sub_word = word[first_h+1::]
second_h = sub_word.index('h') + first_h + 1
new_word = word[0:first_h] + word[second_h:first_h:-1]+ word[second_h::]
print(new_word)

