cell = int(input('Введите количество клеток: '))
unsuitable_list = []

for rank in range(1, cell + 1):
    print('Эффективность', rank, 'клетки: ', end='')
    efficiency = int(input())
    if efficiency < rank:
        unsuitable_list.append(efficiency)

print('Неподходящие значения: ', end='')

for i in unsuitable_list:
    print(i, end=' ')
