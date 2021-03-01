num = int(input('Введите число: '))

for divider in range(2, num + 1):
    if num % divider == 0:
        break
print('Наименьший делитель, отличный от еденицы:', divider)
