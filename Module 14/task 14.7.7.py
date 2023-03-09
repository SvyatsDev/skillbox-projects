#Задача 7. Годы
#Недавно Костя прочитал какую-то научно-фантастическую книжку, где самые страшные события случались
# только в определённые годы, а именно когда в году были ровно три одинаковые цифры. Косте стало интересно,
# какие годы были или будут «особенными» в определённом промежутке.
#Напишите программу, в которой у пользователя запрашивается два четырёхзначных числа A и B.
# Затем выведите в порядке возрастания все четырёхзначные числа в интервале от A до B,
# запись которых содержит ровно три одинаковые цифры.

def programm(a,b,n):
    temp_num = 0
    temp_i = 0
    count_num0 = 0
    count_num1 = 0
    count_num2 = 0
    count_num3 = 0
    count_num4 = 0
    count_num5 = 0
    count_num6 = 0
    count_num7 = 0
    count_num8 = 0
    count_num9 = 0

    for i in range(a,b+1):
        temp_i = i
        while temp_i != 0:
            temp_num = temp_i % 10
            if temp_num == 0:
                count_num0 += 1
            if temp_num == 1:
                count_num1 += 1
            if temp_num == 2:
                count_num2 += 1
            if temp_num == 3:
                count_num3 += 1
            if temp_num == 4:
                count_num4 += 1
            if temp_num == 5:
                count_num5 += 1
            if temp_num == 6:
                count_num6 += 1
            if temp_num == 7:
                count_num7 += 1
            if temp_num == 8:
                count_num8 += 1
            if temp_num == 9:
                count_num9 += 1
            temp_i = temp_i // 10
        if count_num0 == n or count_num1 == n or count_num2 == n or count_num3 == n or count_num4 == n or count_num5 == n or count_num6 == n or count_num7 == n or count_num8 == n or count_num9 == n:
            print(i)

        count_num0 = 0
        count_num1 = 0
        count_num2 = 0
        count_num3 = 0
        count_num4 = 0
        count_num5 = 0
        count_num6 = 0
        count_num7 = 0
        count_num8 = 0
        count_num9 = 0



a = int(input('Введите нижнюю границу числа: '))
b = int(input('Введите верхнюю границу числа: '))
n = int(input('Введите количество одинаковых цифр в числе: '))
print('=============')

programm(a,b,n)