quantity = int(input('Введите количество видеокарт: '))
card_list = []
new_card_list = []
max_card = 0

for index in range(1, quantity + 1):
    print(index, 'видеокарта: ', end='')
    card = int(input())
    card_list.append(card)
    if card > max_card:
        max_card = card

for card in card_list:
    if card != max_card:
        new_card_list.append(card)

print('Старый список видеокарт:', card_list, '\nНовый список видеокарт:', new_card_list)
