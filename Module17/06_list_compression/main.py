def change(elm, elm_list):
    if elm_list[elm] == 0:
        del elm_list[elm]
        elm_list.append(0)
    return elm_list[elm]


num_list = [2, 0, 3, 1, 0, 5, 0, 3, 1]

# TODO: Обратите внимание что к концу выполнения программы исходный список изменился.
#  Есть ли смысл тогда заводить new_list?:)
new_list = [change(i_elm, num_list) for i_elm in range(len(num_list))]
print('Список с нулями:', new_list)

non_zero_list = [digit for digit in new_list if digit != 0]
print('Список без нулей:', non_zero_list)
