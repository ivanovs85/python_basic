quantity = int(input('Введите количество видеокарт: '))
card_list = []
new_card_list = []
max_card = 0

for index in range(quantity):
    print(index + 1, 'видеокарта: ', end='')
    card = int(input())
    card_list.append(card)
    if card > max_card:
        max_card = card

for i in card_list:
    if i != max_card:
        new_card_list.append(i)

print('Старый список видеокарт:', card_list, '\nНовый список видеокарт:', new_card_list)
