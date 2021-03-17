def calculation(size_skate, people):
    skates_size_list.remove(size_skate)
    people += 1
    return people


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

for foot in foot_size_list:
    for size in skates_size_list:
        # TODO: По прежнему предлагаю подумать как избавиться от дублирования ниже:)
        if foot == size:
            count_people = calculation(size, count_people)
            break
        elif foot < size:
            count_people = calculation(size, count_people)
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_people)
