first_num = input('Введите первое число: ')
second_num = input('Введите второе число: ')


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
sum_num = float(first_revers) + float(second_revers)

print('Первое число наоборот:', first_revers, '\nВторое число наоборот:', second_revers, '\nСумма:', sum_num)
