import random
number = random.randint(1,11)
color = random.randint(1,3)
color3 = []
if color == 1:
    color3.append("красный")
if color == 2:
    color3.append("чёрный")
tries = 5
color4 = "".join(color3)
while True:
    if tries == 0:
        print(f"Попытки кончились. Правильный ответ {number} {color4}.")
        break
    number2 = int(input("Введите число от 1 до 10. "))
    color2 = input("Выберите цвет. Красный или чёрный. ")
    if number2 == number and color2 == color4:
        print("Вы выиграли!!!")
        break
    else:
        print("Попробуйте ещё.")
    tries -= 1