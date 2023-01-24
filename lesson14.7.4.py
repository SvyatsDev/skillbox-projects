# Пользователь вводит два вещественных числа — N и K.
# Напишите программу, которая отдельно заменяет сначала
# целую часть на число, которое получается из исходного
# записью его цифр в обратном порядке, затем то же самое
# делает с дробной частью. После этого числа складываются
# и сумма выводится на экран.
# 102.53


def revers(x):
    x = str(x)
    revers_num = ''
    int_num = ''
    float_num = ''
    temp_num = ''
    flag = True
    for symbol in x:
        if symbol == '.':
            flag = False
        elif flag:
            int_num += symbol
        else:
            float_num += symbol
    while int_num != 0:
        temp_num += str(int(int_num)%10)
        int_num = int(int_num)//10
    int_num = temp_num
    temp_num = ''
    while float_num != 0:
        temp_num += str(int(float_num) % 10)
        float_num = int(float_num) // 10
    float_num = temp_num
    temp_num = ''
    new_num = float_num + '.' + int_num # здесь целая часть и плавающая меняются местами
    return new_num

x = float(input('Введите число с плавающей точкой: '))
new_num = revers(x)
print('Новое число наоборот равно: ', new_num)







