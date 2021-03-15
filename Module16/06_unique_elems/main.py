list_num_a = []
list_num_b = []

for num_a in range(3):
    elm = int(input('Введите число первого списка: '))
    list_num_a.append(elm)

for num_b in range(7):
    elm = int(input('Введите число второго списка: '))
    list_num_b.append(elm)

print('Первый список:', list_num_a,
      '\nВторой список:', list_num_b)

list_num_a.extend(list_num_b)

for elm in list_num_a:
    count_elm = list_num_a.count(elm)
    for _ in range(count_elm - 1):
        list_num_a.remove(elm)

print('Новый первый список с уникальными элементами:', list_num_a)
