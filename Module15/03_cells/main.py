cell = int(input('Введите количество клеток: '))
unsuitable_list = []


# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
#  В таком случае, вычисление произойдёт только 1 раз в range, вместо вычислений каждую итерацию цикла.

for rank in range(cell):
    print('Эффективность', rank + 1, 'клетки: ', end='')
    efficiency = int(input())
    if efficiency < rank + 1:
        unsuitable_list.append(efficiency)

print('Неподходящие значения: ', end='')

for i in unsuitable_list:
    print(i, end=' ')
