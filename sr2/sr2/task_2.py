# Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.

list1 = [4, 16, 5, 11, 9, 17, 16, 3, 7]
list2 =[]
for i in list1:
    if i < sum(list1) / len(list1):
        list2.append(i)
print(list2)