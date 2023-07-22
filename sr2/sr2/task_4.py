# Ввести 10 чисел с клавиатуры, данные числа добавить во множество.

set1 = set()
while True:
    if len(set1) == 10:
        print(set1)
        break
    num = int(input('Введите число '))
    set1.add(num)