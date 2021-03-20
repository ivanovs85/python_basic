def is_guest_exist(person, guests_list):
    for name_person in guests_list:
        if name_person == person:
            return True
    return False


def come(friends):
    name = input('Имя гостя: ')
    if len(guests) < 6:
        friends.append(name)
        print('Привет,', name + '!')
    else:
        print('Прости,', name, ', но мест нет.')


def gone(friends):
    name = input('Имя гостя: ')
    if is_guest_exist(name, friends):
        print('Пока,', name)
        friends.remove(name)
    else:
        print('Гостя с таким именем не было')


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек', guests)
    instructions = input('Гость пришел или ушел? ')
    if instructions == 'пришел':
        come(guests)
    elif instructions == 'ушел':
        gone(guests)
    elif instructions == 'пора спать':
        break
    else:
        print('Такой команды нету')

print('Вечеринка закончилась, все легли спать')
