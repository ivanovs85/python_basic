main_list = [1, 5, 3]
list_a = [1, 5, 1, 5]
list_b = [1, 3, 1, 5, 3, 3]
main_list.extend(list_a)
count_a = 0
count_b = 0

for elm in main_list:
    if elm == 5:
        count_a += 1
        main_list.remove(elm)

main_list.extend(list_b)

for elm in main_list:
    if elm == 3:
        count_b += 1

print('Кол-во цифр 5 при первом объединении:', count_a,
      '\nКол-во цифр 3 при втором объединении:', count_b,
      '\nИтоговый список:', main_list)
