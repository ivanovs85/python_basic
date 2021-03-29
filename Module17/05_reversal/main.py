text = input('Введите текст: ')

h_init = text.index('h')
h_end = len(text) - text[::-1].index('h') - 1

print(text[:h_init] + text[h_end:h_init:-1] + text[h_end:])

