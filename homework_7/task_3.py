# 3)	Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 3].
# Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).
spis1 = [-8, 1, 2, -2, 0]
spis2 = [1, -1, 0, -9, 4, -5]
spis3 = [1, 4, 0, 23, 6, 3]
spis1.sort()
spis2.sort()
spis3.sort()
print(f"Второе наименьшее значение этого списка - {spis1[1]} ")
print(f"Второе наименьшее значение этого списка - {spis2[1]} ")
print(f"Второе наименьшее значение этого списка - {spis3[1]} ")