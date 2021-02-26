num = int(input('Введите число: '))
# TODO: Аналогично 2 и 3:)
# Не понял что вы имеете ввиду
for devider in range(2, num + 1):
    if num % devider == 0:
        break
print('Наименьший делитель, отличный от еденицы:', devider)