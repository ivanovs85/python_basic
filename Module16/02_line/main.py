# TODO: Можно сделать проще. Просто оберните ваш range(...) в ф-ию list():)
def range_class(start, end, step):
    class_list = []
    for pupil in range(start, end, step):
        class_list.append(pupil)
    return class_list


def sorting(sort_list):
    for i_mn in range(len(sort_list)):
        for curr in range(i_mn, len(sort_list)):
            if sort_list[curr] < sort_list[i_mn]:
                sort_list[curr], sort_list[i_mn] = sort_list[i_mn], sort_list[curr]
    return sort_list

CLASS_A_START = 160
CLASS_A_END = 176
STEP_A = 2
CLASS_B_START = 162
CLASS_B_END = 180
STEP_B = 3

list_class = range_class(CLASS_A_START, CLASS_A_END, STEP_A)
list_class.extend(range_class(CLASS_B_START, CLASS_B_END, STEP_B))
list_sort = sorting(list_class)

print(list_sort)
