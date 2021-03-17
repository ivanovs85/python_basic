quantity = int(input('Кол-во чисел: '))
num_list = []
new_list = []

for _ in range(quantity):
    num = int(input('Число: '))
    num_list.append(num)

print()
print('Последовательность:', ' '.join(str(num_list)))
print()

for elm in range(len(num_list) - 1, -1, -1):
    if num_list[elm] != num_list[elm - 1]:
        num_list.append(num_list[elm - 1])
        new_list.append(num_list[elm - 1])

print('Нужно приписать чисел:', len(new_list), '\nСами числа:', end=' ')
for new_elm in new_list:
    print(new_elm, end=' ')
