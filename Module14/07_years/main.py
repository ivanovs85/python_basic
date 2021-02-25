first_year = int(input('Введите первый год: '))
second_year = int(input('Введите первый год: '))
count = 0

for year in range(first_year, second_year + 1):
    for num in str(year):
        for check_num in str(year):
            if num == check_num:
                count += 1
        if count == 3:
            print(year)
            count =0
            break
        else:
            count = 0

