length = int(input('Введите длину списка: '))
list_num = [(1 if num % 2 == 0 else num % 5) for num in range(length)]
print('Результат', list_num)

