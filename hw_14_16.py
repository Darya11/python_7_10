import math
#task_14
#-------------------------------------------
def parity_of_numeral (numeral):
    if numeral / 2 == int(numeral / 2):
        print(numeral)
    else:
        print('Число нечетное')


result = parity_of_numeral(9)


#task_15
#-------------------------------------------
print('Пересекаются ли две заданные окружности на плоскости?')

def circus_intersections (x1, x2, r1, y1, y2, r2):
    distance_between_centres = math.sqrt((y1 - x1)**2 + (y2 - x2)**2)
    sum_of_radiuses = r1 + r2
    if distance_between_centres > sum_of_radiuses:
        print("Нет")
    elif distance_between_centres < sum_of_radiuses:
        print("Нет")
    else:
        print('Да')


result1 = circus_intersections(7, 8, 3, 8, 9, 5)


#task_16
#---------------------------------------------
print("Два поезда движутся с заданной скоростью. Между ними 10 км. Первый поезд через 4 км может свернуть с пути."
      "Столкнутся ли поезда?")


def trains_crash (velocity1, velocity2):
    square = 10
    time_train_1 = (10 - 6)/velocity1
    time_train_2 = (10 - 4)/velocity2
    if time_train_1 < time_train_2:
        print('Поезда не столкнутся')
    else:
        print("Поезда столкнутся")

result2 = trains_crash(30, 60)
