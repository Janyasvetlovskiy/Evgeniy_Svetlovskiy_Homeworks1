# 17*.
# Дезоксирибонуклеиновая кислота (ДНК) представляет собой
# химическое вещество, находящееся в ядре клеток и несущее
# «инструкции» по развитию и функционированию живых организмов.
# В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и
# «G».Вам нужно вернуть другую дополнительную сторону. Нить
# ДНК никогда не бывает пустой или ДНК вообще не существует.
# Пример: (ввод --> вывод)
#
# “АТТGС" --> "ТААСG"
# “GТАТ" --> "САТА"
string = input("Введите ДНК ")
spis = [i for i in string]
spis2 = []
for i in spis:
    if i == 'A':
        spis2.append('T')
    elif i == 'T':
        spis2.append('A')
    elif i == 'G':
        spis2.append('C')
    else:
        spis2.append('G')
string2 = ''.join(spis2)
print(string2)