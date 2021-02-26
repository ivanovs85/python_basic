first_year = int(input('Введите первый год: '))
second_year = int(input('Введите первый год: '))
count = 0

for year in range(first_year, second_year + 1):
    for num in str(year):
        # TODO: Дважды проходитесь по одному и тому же циклу:(
        # К сожалению это вынуждено, в первом цикле мы берем 1 цифру, а во втором проверяем есть ли в году 3 совпадающие цифры
        for check_num in str(year):
            if num == check_num:
                count += 1
        if count == 3:
            print(year)
            # TODO: Не хватает пробела;)
            count = 0   #Пробел поставил
            break
        else:
            count = 0
# TODO: Аналогично 2:)

