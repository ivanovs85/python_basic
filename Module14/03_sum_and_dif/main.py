num = (input('Введите число: '))
var = 0
num_summ = 0
for i in num:
    num_summ += int(i)
    var += 1
diff = num_summ - var
print('Сумма цифр:', num_summ, '\nКол-во цифр в числе:', var, '\nРазность суммы и кол-ва цифр:', diff)
