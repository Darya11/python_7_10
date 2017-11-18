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
