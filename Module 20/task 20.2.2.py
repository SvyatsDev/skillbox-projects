import math
def square(r,h):
    side = 2 * math.pi * r * h
    s_round = 2 * math.pi * (r**2)
    full = side + 2 * s_round
    return side, full
r = int(input('Радиус: '))

h = int(input('Высота: '))
side, full = square(r, h)
print('Площадь стороны: ', side)
print('Площадь цилиндра: ', full)

