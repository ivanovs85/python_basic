def change(elm, elm_list):
    if elm_list[elm] == 0:
        del elm_list[elm]
        elm_list.append(0)
    return elm_list[elm]


num_list = [2, 0, 3, 1, 0, 5, 0, 3, 1]

num_list = [change(i_elm, num_list) for i_elm in range(len(num_list))]
print('Список с нулями:', num_list)

num_list = [digit for digit in num_list if digit != 0]
print('Список без нулей:', num_list)
