# Дана длина ребра куба. Найти объём куба и площадь его боковой поверхности
long = int(input("Введите длину ребра куба "))

volume = long**3
side_surface_area = long * long * 6

print("Объём куда " + str(volume))
print("Площадь боковой поверхности куба " + str(side_surface_area))