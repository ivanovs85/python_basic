word = input('Введите слово: ')
word_list = list(word)
count = 0

for i in range(len(word_list)):
    for j in range(i + 1, len(word_list)):
        if word_list[i] == word_list[j]:
            word_list[i] = 0

for sym in word_list:
    if sym != 0:
        count += 1

print('Количество уникальных букв:', count)