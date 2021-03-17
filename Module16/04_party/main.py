def is_guest_exist(person, guests_list):
    for name_person in guests_list:
        if name_person == person:
            return True
    return False


def actions(instructions, friends_list):
    if instructions == 'пришел' and len(friends_list) < 6:
        name = input('Имя гостя: ')
        friends_list.append(name)
        print('Привет,', name + '!')
    elif instructions == 'пришел' and len(friends_list) >= 6:
        name = input('Имя гостя: ')
        print('Прости,', name, ', но мест нет.')
    elif instructions == 'ушел':
        name = input('Имя гостя: ')
        if is_guest_exist(name, friends_list):
            print('Пока,', name)
            friends_list.remove(name)
        else:
            print('Гостя с таким именем не было')
    else:
        print('Такой команды нету')
    return friends_list


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек', guests)
    command = input('Гость пришел или ушел? ')
    if command == 'пора спать':
        break
    else:
        actions(command, guests)


print('Вечеринка закончилась, все легли спать')
