def change(elm):
    if num_list[elm] == 0:
        del num_list[elm]
        num_list.append(0)
    return num_list[elm]


num_list = [2, 0, 3, 1, 0, 5, 0, 3, 1]

num_list = [change(i_elm) for i_elm in range(len(num_list))]
print('Список с нулями:', num_list)

num_list = [digit for digit in num_list if digit != 0]
print('Список без нулей:', num_list)

#Я не знал этого, думал, что в функция живет своей жизнью, и переменные вне функции не действуют на нее