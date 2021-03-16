def range_class(start, end, step):
    num = int((end - start) / step)
    class_list = []
    for pupil in range(num + 1):
        growth = start + step * pupil
        class_list.append(growth)
    return class_list


# TODO: Правильнее было бы оформить эти значения в виде коонстант:
#  то же самое только всее символы в нейминге верхнего регистра:)
class_a_start = 160
class_a_end = 176
step_a = 2
class_b_start = 162
class_b_end = 180
step_b = 3

# TODO: Предлагаю сделать на много проще: используйте range(), в котором вы также можете указать старт, стоп и шаг:)
list_class = range_class(class_a_start, class_a_end, step_a)
list_class.extend(range_class(class_b_start, class_b_end, step_b))

# TODO: Предлагаю оформить в вид ф-ии, принимающей на вход не отсортированный список и возвращающей отсортированный:)
for i_mn in range(len(list_class)):
    for curr in range(i_mn, len(list_class)):
        if list_class[curr] < list_class[i_mn]:
            list_class[curr], list_class[i_mn] = list_class[i_mn], list_class[curr]

print(list_class)
