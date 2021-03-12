print('Введите список цифр:')
list_num = []

for _ in range(5):
    num = int(input('->'))
    list_num.append(num)

# Проходимся по списку и меняем местами соседние числа по возрастанию. И это повторяем 5 раз пока точно все не
# упорядочится
for _ in range(5):
    for i in range(4):
        if list_num[i] > list_num[i + 1]:
            temp = list_num[i]
            list_num[i] = list_num[i + 1]
            list_num[i + 1] = temp

print(list_num)

# зачёт!
