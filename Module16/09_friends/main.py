friends = int(input('Кол-во друзей: '))
rect = int(input('Долговых расписок: '))
friends_list = []

for _ in range(friends):
    friends_list.append(0)

for i_rect in range(1, rect + 1):
    print()
    print(i_rect, 'расписка')
    credit_friend = int(input('Кому: '))
    debt_friend = int(input('От кого: '))
    summa = int(input('Сколько: '))
    friends_list[credit_friend - 1] += summa
    friends_list[debt_friend - 1] -= summa

print('\nБаланс друзей:')
for index in range(friends):
    print(index + 1, ':', friends_list[index])
