word = input('Введите слово: ')
letter_list = []
count = 0
count_double = 0

for letter in word:
    letter_list.append(letter)

for letter in letter_list:
    count += 1
    if count > len(letter_list) / 2 + 0.5:
        break
    elif letter == letter_list[-count]:
        count_double += 1

if count_double + 1 >= len(letter_list) / 2 + 0.5:
    print('Слово является полиндромом')
else:
    print('Слово не является полиндромом')
