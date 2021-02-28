first_year = int(input('Введите первый год: '))
second_year = int(input('Введите первый год: '))
count = 0
count_first = 0
count_second = 0
num_first = 0
num_second = 0

for year in range(first_year, second_year + 1):
    for num in str(year):
        count += 1
        if count == 1:
            num_first = num
        elif count == 2:
            num_second = num
        if num_first == num:
            count_first += 1
        elif num_second == num:
            count_second += 1

    if count_first == 3 or count_second == 3:
        print(year)

    count = 0
    count_first = 0
    count_second = 0
    num_first = 0
    num_second = 0
