word = input('Введите слово: ')
word_list = list(word)
count = 0


# TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i" и "j" не отражают =)

for i in range(len(word_list)):
    for j in range(i + 1, len(word_list)):
        if word_list[i] == word_list[j]:
            word_list[i] = 0

for sym in word_list:
    if sym != 0:
        count += 1

print('Количество уникальных букв:', count)


# TODO Введите слово: карамба
#  Количество уникальных букв: 5
#  По идее, буквы 4 =) к р м б