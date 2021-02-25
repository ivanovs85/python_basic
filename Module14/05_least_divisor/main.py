num = int(input('Введите число: '))
for devider in range(2, num + 1):
    if num % devider == 0:
        break
print('Наименьший делитель, отличный от еденицы:', devider)