#Пользователь вводит список из N чисел и число K. Напишите код, выводящий на
# экран сумму индексов элементов списка, которые кратны K.


nums_list = []
n = int(input('Введите количество чисел: '))
for _ in range(n):
    print('Введите', _ + 1, 'число: ', end = ' ')
    num = int(input())
    nums_list.append(num)

k = int(input('Введите делитель :'))

i_summ = 0
for i in range(n):
    if nums_list[i] % k == 0:
       print('Индекс числа', nums_list[i], ':', i)
       i_summ += i

print('Сумма индексов кратных', k, 'равна', i_summ)