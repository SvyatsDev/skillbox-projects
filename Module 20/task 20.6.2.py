# Спустя некоторое время заказчик попросил нас немного изменить скрипт для своей криптографии:
# теперь индексы элементов должны быть простыми числами.
# Напишите функцию, которая возвращает список из элементов итерируемого объекта (кортежа, строки, списка, словаря),
# у которых индекс — это простое число. Для проверки на простое число напишите отдельную функцию is_prime.
# Дополнительно: сделайте так, чтобы основная функция состояла только из оператора return и при этом также возвращала список.
def lst_char(sample):
    return [x for x in sample]


def is_prime(x):
    is_prime_num = [i_num for i_num in range(1, x + 1) if x % i_num == 0 ]
    if len(is_prime_num) > 2:
        return False
    if 1 < len(is_prime_num) <= 2:
        return True


text = input('Введите данные: ')
new_text = [i_name for i_idx, i_name in enumerate(text) if is_prime(i_idx)]
print(new_text)
