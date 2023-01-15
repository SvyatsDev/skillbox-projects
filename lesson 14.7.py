def num_summ(x):
    if x > 0:
        total_summ = 0
        while x != 0:
            total_summ += x % 10
            x //= 10
        return total_summ
    else:
        print('Ошибка введите значение больше нуля!')

def num_count(x):
    total_count = 0
    if x > 0:
        while x != 0:
            total_count += 1
            x //= 10
        return total_count
    else:
        print('Ошибка, введите значение больше нуля!')

x = int(input('Введите число: '))
summ = num_summ(x)
count = num_count(x)

print('\nСумма чисел: ', summ)
print('\nКоличество цифр: ', count)
print('\nРазница суммы чисел и количества: ', summ - count)

