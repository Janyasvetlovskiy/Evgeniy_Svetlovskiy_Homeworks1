# 3)	Есть список натуральных чисел. Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу:
# например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
# само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
# строка «444» (третье повторение, т.е. строка множится на 3).

list1 = [7, 14, 25, 7, 99, 25, 25, 43]
set1 = set()
for i in list1:
    number = list1.count(i)
    set1.add(str(i)*number)
print(set1)