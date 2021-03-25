def vowels_check(letter):
    for vowels in vowels_list:
        if letter == vowels:
            return True
    return False


text = input('Введите текст: ')
vowels_list = ['а', 'у', 'о', 'и', 'э', 'ы', 'е', 'я', 'ю']

vowels_sym = [sym for sym in text if vowels_check(sym)]
print('Список гласных букв:', vowels_sym, '\nДлина списка:', len(vowels_sym))
