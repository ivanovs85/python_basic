first_list = []
second_list = []

for _ in range(3):
    num_first = int(input('Введите число первого списка: '))
    first_list.append(num_first)

for _ in range(7):
    num_second = int(input('Введите число второго списка: '))
    second_list.append(num_second)

print('Первый список:', first_list,
      '\nВторой список:', second_list)

first_list.extend(second_list)

for elm in first_list:
    count_elm = first_list.count(elm)
    for _ in range(count_elm - 1):
        first_list.remove(elm)

print('Новый первый список с уникальными элементами:', first_list)
