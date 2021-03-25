def shift_let(sym, trans):
    if sym == ' ':
        return sym
    i_letter = alphabet.index(sym)
    shift_letter = alphabet[(i_letter + trans) % 33]
    return shift_letter


message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

encrypted = [shift_let(letter, shift) for letter in message]
print('Зашифрованное сообщение:', ''.join(encrypted))
