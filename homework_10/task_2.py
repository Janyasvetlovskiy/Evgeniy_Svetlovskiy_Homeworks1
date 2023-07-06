# 2)	Создайте словарь d = {'1': 0, ‘2’: 0, '3': 0} тремя способами. Выведите полученный словарь на экран.

# 1
keys = ['1', '2', '3']
values = [0, 0, 0]
dct1 = dict(zip(keys, values))
print(dct1)

# 2
keys = ['1', '2', '3']
dct2 = dict.fromkeys(keys, 0)
print(dct2)

# 3
dct3 = dict([('1',0), ('2',0), ('3',0)])
print(dct3)