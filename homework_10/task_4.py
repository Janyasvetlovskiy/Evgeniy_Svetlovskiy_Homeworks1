# 4)	На вход программы подается словарь a = {1:10, 2:20, 3:30},
# необходимо получить список произведения ключа на значение.
a = {1:10, 2:20, 3:30}
proizv = []
for key,value in a.items():
    pr = key * value
    proizv.append(pr)
print(proizv)