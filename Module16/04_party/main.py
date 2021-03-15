def is_guest_exist(person, guests_list):
    for name_person in guests_list:
        if name_person == person:
            return True
    return False


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек', guests)
    command = input('Гость пришел или ушел? ')
    if command == 'пришел' and len(guests) < 6:
        name = input('Имя гостя: ')
        guests.append(name)
        print('Привет,', name + '!')
    elif command == 'пришел' and len(guests) >= 6:
        name = input('Имя гостя: ')
        print('Прости,', name, ', но мест нет.')
    elif command == 'ушел':
        name = input('Имя гостя: ')
        if is_guest_exist(name, guests):
            print('Пока,', name)
            guests.remove(name)
        else:
            print('Гостя с таким именем не было')
    elif command == 'Пора спать':
        break
    else:
        print('Такой команды нету')
print('Вечеринка закончилась, все легли спать')
