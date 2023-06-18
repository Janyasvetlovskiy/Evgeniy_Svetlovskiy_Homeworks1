spisok = [5,8,3,8,9,9,4,11,12,11]
spisok2 = []
for i in spisok:
    if spisok.count(i) < 2:
        spisok2.append(i)
print(spisok2)