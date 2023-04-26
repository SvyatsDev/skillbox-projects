# При работе со значениями по умолчанию и изменяемыми типами данных нужно знать и остерегаться ещё одной интересной штуки.
#
# Напишите функцию с двумя аргументами: первый — число num, позиционный аргумент; второй — список lst,
# по умолчанию он пустой. В теле функции в список добавляется число num и сам список выводится на экран.
#
# В основной программе вызовите функции три раза только с одним аргументом (числом), например так:
# add_num(5)
# add_num(10)
# add_num(15)
#
# И посмотрите, что произойдёт.
#
# После этого сделайте значение lst по умолчанию None и поправьте функцию, чтобы она работала правильно.

def add_num(num, lst=None):
    if lst == None:
        lst = list()
        lst.append(num)
        print(lst)
    else:
        lst.append(num)
        print(lst)


add_num(5, [1,2,3])
add_num(10)
add_num(15)