while True:
    print("Введите первую точку")
    x1 = float(input('X: '))
    y1 = float(input('Y: '))
    print("\nВведите вторую точку")
    x2 = float(input('X: '))
    y2 = float(input('Y: '))
    if x1 == x2:
        # TODO: Увы, заключение не веерное:(
        # Но ведь, на 0 делить нельзя, если х1 и х2 будут равными, то x_diff будет равен 0
        # TODO: Это значит что у них будет другой вид уравнения.
        #  Если и игрики будут равны, то получим точку. В противном случае уравнение х = ...
        print('Х первой точки не должен быть равен Х второй точки. Введите координаты еще раз.')
    else:
        break

x_diff = x1 - x2
y_diff = y1 - y2
k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)
