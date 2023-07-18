# 2)	Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

with open('task_2_fail.txt', 'w') as file:
    while True:
        string = input('Введите данные: ')
        if string == 'end':
            file.write('')
            break
        file.write(string + '\n')


