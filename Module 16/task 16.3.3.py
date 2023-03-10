# При работе с сервером мы кодируем сообщение и отправляем его в виде пакетов информации.
# Их количество равно N. Допустим, каждый пакет содержит четыре числа, каждое из которых равно нулю или единице.
# Эти числа называются битами. Иногда в кодировке сообщения встречаются ошибки, и в пакете эта ошибка обозначается числом -1.
# Если таких ошибок не больше одной, то этот пакет мы целиком добавляем в список для декодирования, а иначе отбрасываем.
#
# Напишите программу, которая будет обрабатывать полученные пакеты и выведет на экран итоговое сообщение для декодирования,
# а также количество ошибок в нём и количество необработанных пакетов.
#
# Пример:
# Кол-во пакетов: 3
#
# Пакет номер 1
# 1 бит: 1
# 2 бит: 0
# 3 бит: -1
# 4 бит: 1
#
# Пакет номер 2
# 1 бит: -1
# 2 бит: -1
# 3 бит: 1
# 4 бит: 1
# Много ошибок в пакете.
#
# Пакет номер 3
# 1 бит: 0
# 2 бит: 1
# 3 бит: 1
# 4 бит: 1
#
# Полученное сообщение: [1, 0, -1, 1, 0, 1, 1, 1]
# Кол-во ошибок в сообщении: 1
# Кол-во потерянных пакетов: 1
#

list_bit = []
total_list = []
pack_lost = 0
bad_bit = 0
n = int(input('Введите количество пакетов: '))
for _ in range(n):
    print('Пакет номер: ', _+1)
    for i in range(4):
        print(i+1, 'бит: ', end=' ')
        bit = int(input())
        list_bit.append(bit)
    if list_bit.count(-1) <= 1:
        total_list.extend(list_bit)
    if list_bit.count(-1) > 1:
        pack_lost += 1
        print('Много ошибок в пакете!')
    list_bit = []
    print()
bad_bit += total_list.count(-1)
print('Полученное сообщение: ', total_list)
print('Количество ошибок в сообщении:', bad_bit)
print('Количество потерянных пакетов: ', pack_lost)