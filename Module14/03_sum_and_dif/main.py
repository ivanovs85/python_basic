num = input('Введите число: ')
var = 0
num_sum = 0
for i in num:
    num_sum += int(i)
    var += 1
diff = num_sum - var
print('Сумма цифр:', num_sum, '\nКол-во цифр в числе:', var, '\nРазность суммы и кол-ва цифр:', diff)
