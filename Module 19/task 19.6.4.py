# В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает
# за коды товаров, второй — за списки количества разнообразных товаров на складе:
#
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за 1 шт.).
#
# Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.
#
# Результат работы программы.
# Лампа - 27 шт, стоимость 1134 руб
# Стол - 54 шт, стоимость 27860 руб
# Диван - 3 шт, стоимость 3550 руб
# Стул - 105 шт, стоимость 10311 руб
count = 0
summ = 0
temp_count = 0
keys_goods = [x for x in goods]
i_keys = 0
for i_store in store:
    for _ in range(len(store[i_store])):
        count += store[i_store][_].get('quantity', 0)
        temp_count = store[i_store][_].get('quantity', 0)
        summ += store[i_store][_].get('price', 0) * temp_count
        temp_count = 0
    print(keys_goods[i_keys], '-', count, 'шт,', 'стоимость', summ, 'руб')
    count = 0
    summ = 0
    i_keys += 1