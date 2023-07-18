# 1)	Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длины.

with open('task_1_fail.txt', 'r') as file:
    list1 = file.readlines()
    print(list1)
    list2 = [i.rstrip() for i in list1]
    print(list2)
    numbers = []
    litters = []
    for i in list2:
        if i.isdigit():
            numbers.append(int(i))
        else:
            litters.append(i)
    numbers.sort()
    litters.sort()
    print(numbers + litters)

