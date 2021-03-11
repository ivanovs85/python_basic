print('Введите список элементов:')
num_list = []
new_num_list = [0, 0, 0, 0, 0]
count = -1

for _ in range(5):
    num = int(input('-> '))
    num_list.append(num)

shift = int(input('Введите сдвиг: '))
print('Изначальный список:', num_list)

for i in num_list:
    count += 1
    if shift + count > 4:
        new_num_list[shift + count - 5] = i
    else:
        new_num_list[shift + count] = i

print('Сдвинутый список:  ', new_num_list)
