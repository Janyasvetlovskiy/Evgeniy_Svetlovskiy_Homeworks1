# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

with open('article.txt', 'r') as file:
    list1 = file.readlines()
    print(list1)
    list2 = [i.rstrip() for i in list1]
    print(list2)
    list2.sort(key=len)
    print(list2)
    length = len(list2[-1])
    list3 = []
    for i in list2:
        if len(i) == length:
            list3.append(i)
    print(list3)
    