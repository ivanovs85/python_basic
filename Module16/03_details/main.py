shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
count_detail = 0
total_price = 0

for price in shop:
    if price[0] == detail:
        count_detail += 1
        total_price += price[1]

print('Кол-во деталей -', count_detail, '\nОбщая стоимость -', total_price)
