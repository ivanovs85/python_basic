# TODO: В задании требуется написать ф-ию:)
print('Введите координаты монетки:')
x = float(input('Х: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))


def find_coin(x, y, radius):
    if x ** 2 + y ** 2 < radius ** 2:
        print('Монетка где-то рядом')
    else:
        print('Монетки рядом нет')


find_coin(x, y, radius)