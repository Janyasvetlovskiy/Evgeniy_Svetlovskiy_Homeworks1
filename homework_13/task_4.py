# Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт. (целое число).
# Напишите программу, подсчитывающую общую стоимость заказа.

with open('prices.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    lines2 = [i.rstrip() for i in lines]
    print(lines2)
    all_price = 0
    for i in lines2:
        line = i.split('    ')
        all_price += int(line[1]) * int(line[2])
    print(f'Общая стоимость заказа - {all_price} рублей')