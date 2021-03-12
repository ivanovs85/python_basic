num = int(input('Введите целое число: '))
odd_num = []

for i in range(1, num + 1):
    if i % 2 != 0:
        odd_num.append(i)

print(odd_num)
