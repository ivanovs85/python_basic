films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
check = True
films_favorite = []
add = int(input('Сколько фильмов хотите добавить: '))

for _ in range(add):
    add_film = input('Введите название фильма: ')
    for film in films:
        if film == add_film:
            films_favorite.append(film)
            check = False
            break
    if check:
        print('Такого фильма нет в списке')
    check = True

print('\nСписок любимых фильмов:', end=' ')

for i in films_favorite:
    print(i, end=' ')
