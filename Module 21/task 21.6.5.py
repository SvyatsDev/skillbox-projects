# У нас есть функция, которая делает определённые действия с входными данными:
# Берёт факториал от числа.
# Результат делит на куб входного числа.
# И получившиеся число возводит в 10-ю степень.
#
# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result
#
# Однако каждый раз нам приходится делать сложные вычисления, хотя входные и выходные данные одни и те же.
# И тут наши знания тонкостей Python должны нам помочь.
#
# Оптимизируйте функцию так, чтобы высчитывать факториал для одного и того же числа только один раз.
#
# Подсказка: вспомните, что происходит с изменяемыми данными, если их выставить по умолчанию в параметрах функции.
def calculating_math_func(data, factorial= {} ):
    if data in factorial:
        result = factorial[data]
        print(factorial)
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        factorial[data] = result
    result /= data ** 3
    result = result ** 10
    return result
while True:
    data = int(input('Введите число: '))
    print('Ответ: ', calculating_math_func(data))