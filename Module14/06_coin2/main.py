print('Введите координаты монетки:')
x_coin = float(input('Х: '))
y_coin = float(input('Y: '))
radius = float(input('Введите радиус: '))


def find_coin(x, y, r):
    if x ** 2 + y ** 2 < r ** 2:
        print('Монетка где-то рядом')
    else:
        print('Монетки рядом нет')


find_coin(x_coin, y_coin, radius)
