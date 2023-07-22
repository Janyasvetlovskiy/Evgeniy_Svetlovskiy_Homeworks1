# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

import random
min = int(input('Введите начальную границу массива '))
max = int(input('Введите начальную границу массива '))
length = int(input('Какова будет длина массива? '))
massiv = [random.randint(min, max) for i in range(length)]
print(massiv)
min2 = int(input('Введите новые минимальные границы массива '))
max2 = int(input('Введите новые максимальные границы массива '))
massiv2 = massiv[massiv.index(min2), massiv.index(max2)]
for i in massiv:
    if massiv.index(i) in massiv2:
        massiv.remove(i)
print(massiv)
# Не справился