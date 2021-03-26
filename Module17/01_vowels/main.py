text = input('Введите текст: ')
vowels_list = ['а', 'у', 'о', 'и', 'э', 'ы', 'е', 'я', 'ю']

vowels_sym = [sym for sym in text if sym in vowels_list]
print('Список гласных букв:', vowels_sym, '\nДлина списка:', len(vowels_sym))
