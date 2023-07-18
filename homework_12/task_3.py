# 3)	В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество в ней символов.

with open('task_3_fails.txt') as file:
    list1 = file.readlines()
    print(list1)
    print(f'Количество строк: {len(list1)}')
    for i in list1:
        print(f'В этой строке {len(i)} символов')