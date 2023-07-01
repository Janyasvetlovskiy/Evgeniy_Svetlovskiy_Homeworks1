# Даны два целых числа m и n. Напишите программу,
# которая выводит все числа от m до n включительно в порядке возрастания,
# если m<n, или в порядке убывания в противном случае.
num_1 = int(input("Введите первое число "))
num_2 = int(input("Введите второе число "))
spis = []
if num_2 > num_1:
    for i in range(num_1, num_2):
        spis.append(i)
    spis.sort
    print(spis)
else:
    for i in range(num_2, num_1):
        spis.append(i)
    spis.sort(reverse=True)
    print(spis)
