containers = int(input('Введите кол-во контейнеров: '))
last_container_weight = 200
container_weight_list = []
count = 0
check = False
last_weight = 0

# Записываем последовательность контейнеров в лист с проверкой
for _ in range(1, containers + 1):
    while True:
        container_weight = int(input('Введите вес контейнера: '))
        if container_weight > 200 or container_weight > last_container_weight:
            print('Неверный вес контейнера. Попробуйте еще раз.')
        else:
            break
    container_weight_list.append(container_weight)
    last_container_weight = container_weight

while True:
    new_container_weight = int(input('Введите вес нового контейнера: '))
    if new_container_weight > 200:
        print('Вес введен неверно. Попробуйте снова.')
    else:
        break

for weight in container_weight_list:
    count += 1
    # Если все контейнеры одинакового веса, новый встает в конце
    if count == containers and check:
        count += 1
        num_container = count
        break
    # Если несколько контейнеров с одинаковым весом, новый встает после них
    elif last_weight != weight and check:
        num_container = count
        break
    elif new_container_weight == weight:
        last_weight = weight
        check = True
    # Если новый контейнер легче предыдущего, то встает за ним
    elif new_container_weight > weight:
        num_container = count
        break

print('Номер, куда встанет новый контейнер:', num_container)

# зачёт!
