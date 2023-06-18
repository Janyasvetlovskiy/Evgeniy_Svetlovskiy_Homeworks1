spisok = [1, 5, 1, 7, 7, 1, 6, 7, 9, 9]
spisok2 = []
for i in spisok:
    if spisok.count(i) > 2:
        spisok2.append(i)
print(spisok2)