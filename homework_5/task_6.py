b = int(input("Введите число, в степень которого будет возведена последняя двойка "))
a = [2 ** i for i in range(1,b)]
print(a)