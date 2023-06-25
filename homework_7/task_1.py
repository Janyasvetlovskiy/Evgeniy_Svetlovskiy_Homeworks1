# 1)	Дан список list=[15,48,'hello',6,19,'world’].'
# ' Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. '
# 'Если нечётное, то заменить  его на 1 в списке. Все слова: посчитать количество гласных и согласных.'
# ' Вывести всё на экран.

list = [15, 48, 'hello', 6, 19, 'world']
numbers = []
letters = []
for i in list:
    if type(i) == int:
        numbers.append(i)
    else:
        letters.append(i)
sum_of_numbers = []
for i in numbers:
    if i > 10 and i % 2 == 0:
        a = i // 10
        b = i % 10
        c = a + b
        sum_of_numbers.append(c)
    elif i < 10 and i % 2 == 0:
        sum_of_numbers.append(i)
    else:
        ind = list.index(i)
        list[ind] = 1
new_letters =''.join(letters)
glasnye_letters = []
soglasnye_letters = []
glasnye = 'AEIOUYaeiouy'
for i in new_letters:
    if i in glasnye:
        glasnye_letters.append(i)
    else:
        soglasnye_letters.append(i)
print(list)
print(f'Сумма цифр чётных чисел - {sum_of_numbers}')
print(f'Количество гласных букв в словах {len(glasnye_letters)}')
print(f'Количество согласных букв в словах {len(soglasnye_letters)}')




