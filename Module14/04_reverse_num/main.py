first_num = input('Введите первое число: ')
second_num = input('Введите второе число: ')

# TODO: Ф-ия должна быть обособлена от остального кода на 2 пустые строки:)
def revers(num):
    revers_num = ''
    revers_int = ''
    for i in num:
        if i == '.':
            revers_int = revers_num + '.'
            revers_num = ''
            continue
        revers_num = i + revers_num
    revers_num = revers_int + revers_num
    return revers_num

first_revers = revers(first_num)
second_revers = revers(second_num)
# TODO: Аналогично 3 и 2:)
summ = float(first_revers) + float(second_revers)

print('Первое число наоборот:', first_revers, '\nВторое число наоборот:', second_revers, '\nСумма:', summ)