word = input('Введите слово: ')
word_list = list(word)
count = 0
sym_last = ''

for index in range(len(word_list)):
    for index_repeat in range(index + 1, len(word_list)):
        if word_list[index] == word_list[index_repeat] or sym_last == word_list[index_repeat] and sym_last != 0:
            sym_last = word_list[index]
            word_list[index] = 0
            word_list[index_repeat] = 0


print(word_list)
for sym in word_list:
    if sym != 0:
        count += 1

print('Количество уникальных букв:', count)
