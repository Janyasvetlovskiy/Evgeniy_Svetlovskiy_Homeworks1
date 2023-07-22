# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

string = ' An apple a day keeps the doctor away'
keys = []
for i in string:
    if i == ' ':
        continue
    keys.append(i)
print(keys)
values = []
for i in keys:
    values.append(keys.count(i))
print(values)
dict1 = dict(zip(keys, values))
print(dict1)