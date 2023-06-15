ug1 = int(input("Введите градусную меру угла 1 "))
ug2 = int(input("Введите градусную меру угла 2 "))
ug3 = int(input("Введите градусную меру угла 3 "))
st1 = int(input("Введите длину стороны 1 "))
st2 = int(input("Введите длину стороны 2 "))
st3 = int(input("Введите длину стороны 3 "))

a = ug1 + ug2 + ug3 == 180
b = st1 < st2 + st3
c = st2 < st1 + st3
d = st3 < st1 + st2
e = ug1 == ug2 != ug3
f = ug2 == ug3 != ug1
g = ug3 == ug1 != ug2
h = st1 == st2 != st3
i = st2 == st3 != st1
j = st3 == st1 != st2
x = h + i + j
if a and b and c and d and (e or f or g) and (h or i or j) and ug1 != 90 and ug2 != 90 and ug3 != 90:
    print("Такой тругольник существует и он равнобедренный.")
elif a and b and c and d and (ug1 == 90 or ug2 == 90 or ug3 == 90) and not x:
    print("Такой треугольник существует и он прямоугольный.")
elif a and b and c and d and (ug1 == 90 or ug2 == 90 or ug3 == 90) and (h or i or j) and (e or f or g):
    print("Такой треугольник существует и он прямоугольный и равнобедренный.")
elif a and (ug1 != ug2 != ug3) and (st1 != st2 != st3):
    print("Такой треугольник существует и он произвольный.")
elif a and (ug1 == ug2 == ug3) and (st1 == st2 == st3):
    print("Такой треугольник существует и он равносторонний.")
else:
    print("Такой треугольник не существует.")