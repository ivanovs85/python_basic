list_participants = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list = []

for index in range(len(list_participants)):
    if index % 2 != 0:
        new_list.append(list_participants[index])

print(new_list)
