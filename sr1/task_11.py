# 11.	Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.
spis = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
spis2 = []
for i in spis:
    if " " in i:
        spis2.append(i)
print(spis2)