quantity = int(input('Введите количество видеокарт: '))
card_list = []
new_card_list = []
max_card = 0

# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
#  В таком случае, вычисление произойдёт только 1 раз в range, вместо вычислений каждую итерацию цикла.

for index in range(quantity):
    print(index + 1, 'видеокарта: ', end='')
    card = int(input())
    card_list.append(card)
    if card > max_card:
        max_card = card


# TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i" не отражает =)

for i in card_list:
    if i != max_card:
        new_card_list.append(i)

print('Старый список видеокарт:', card_list, '\nНовый список видеокарт:', new_card_list)
