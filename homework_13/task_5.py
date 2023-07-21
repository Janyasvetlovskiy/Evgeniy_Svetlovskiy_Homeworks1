# Вам предоставляется CSV-файл, содержащий данные о продажах различных товаров.
# Каждая строка файла содержит информацию о конкретной продаже: название товара,
# количество проданных единиц и цена за единицу. Ваша задача - написать программу,
# которая считывает данные из файла и вычисляет общую сумму продаж.

import csv

# data = [
#     ['car', '12', '7000'],
#     ['bus', '4', '12000'],
#     ['train', '14', '50000']
# ]
#
# with open('info.csv', 'a', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(data)

with open('info.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    all_price = 0
    for el in reader:
        all_price += int(el[1]) * int(el[2])
    print(f'Общая сумма продаж - {all_price}')



