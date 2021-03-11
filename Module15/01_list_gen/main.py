num = int(input('Введите целое число: '))
b = []

for i in range(1, num + 1):
    if i % 2 != 0:
        b.append(i)

print(b)
