skates = int(input('Кол-во коньков: '))
skates_size_list = []
foot_size_list = []
count_people = 0

for count in range(1, skates + 1):
    print('Размер', count, 'пары:', end=' ')
    skates_size = int(input())
    skates_size_list.append(skates_size)

peoples = int(input('\nКол-во людей: '))

for count in range(1, peoples + 1):
    print('Размер ноги', count, 'человека:', end=' ')
    foot_size = int(input())
    foot_size_list.append(foot_size)

# Сначало ищем подходящую обувь, и если не найдем, то большего размера. Как нашли удаляем его из списка, чтоб не мешал
for i_foot in range(len(foot_size_list)):
    for i_size in range(len(skates_size_list)):
        if foot_size_list[i_foot] == skates_size_list[i_size]:
            skates_size_list.remove(skates_size_list[i_size])
            count_people += 1
            break
        elif foot_size_list[i_foot] < skates_size_list[i_size]:
            skates_size_list.remove(skates_size_list[i_size])
            count_people += 1
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_people)
