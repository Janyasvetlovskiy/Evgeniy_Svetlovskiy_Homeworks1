chet = []
nechet = []
spisok = [3,5,8,12,9,45,98,76,17]
for i in spisok:
    if i % 2 == 0:
        chet.append(i)
    if i % 2 == 1:
        nechet.append(i)
print(f"Коилчетсво чётных элементов - {len(chet)}")
print(f"Количество нечётных элементов - {len(nechet)}")