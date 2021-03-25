import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(first_team[unit], second_team[unit]) for unit in range(20)]

print('Первая команда:', first_team, '\nВторая команда', second_team, '\nПобедители', winners)
