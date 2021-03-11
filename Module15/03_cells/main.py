cell = int(input('Введите количество клеток: '))
unsuitable_list = []

for rank in range(cell):
    print('Эффективность', rank + 1, 'клетки: ', end='')
    efficiency = int(input())
    if efficiency < rank + 1:
        unsuitable_list.append(efficiency)

print('Неподходящие значения: ', end='')

for i in unsuitable_list:
    print(i, end=' ')
