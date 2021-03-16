violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs = int(input('Сколько песен выбрать? '))
song_length = 0.0

for count in range(1, songs + 1):
    print('Название', count, 'песни:', end=' ')
    # TODO: Хотите научиться писать ткст любой сложности сразу в input?:)
    #  STD: Не понял что вы имеете ввиду
    name_song = input()
    for song in violator_songs:
        if song[0] == name_song:
            song_length += song[1]
            break

print('Общее врем звучания песен:', round(song_length, 2), 'минут')
