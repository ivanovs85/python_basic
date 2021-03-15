players = int(input('Кол-во человек: '))
num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', num, 'человек')

players_list = []
start_count = 1
i_gone = 0

for player in range(1, players + 1):
    players_list.append(player)

while len(players_list) > 1:
    print('\nТекущий круг людей:', players_list,
          '\nНачало счета с номера', start_count)
    i_gone = i_gone + num % len(players_list) - 1
    if i_gone > len(players_list) - 1:
        i_gone = len(players_list) - i_gone
    print('Выбывает человек под номером', players_list[i_gone])
    players_list.remove(players_list[i_gone])
    if i_gone > len(players_list) - 1:
        start_count = players_list[0]
    else:
        start_count = players_list[i_gone]

print('\nОстался человек под номером', players_list[i_gone])
