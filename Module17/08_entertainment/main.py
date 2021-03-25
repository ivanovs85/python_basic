pin = int(input('Введите количество палок: '))
throws = int(input('Введите количество бросков: '))

pin_list = ['I' for _ in range(pin)]

for throw in range(1, throws + 1):
    print('Бросок', str(throw) + '. Сбиты палки с номера', end=' ')
    first_num = int(input())
    end_num = int(input('по номер '))
    pin_list = [('.' if first_num - 1 <= i_elm <= end_num - 1 else pin_list[i_elm]) for i_elm in range(len(pin_list))]

print('\nРезультат:', ''.join(pin_list))
