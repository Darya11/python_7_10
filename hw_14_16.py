import math
#task_14
#-------------------------------------------
print('Is the numeral even?')

def is_the_numeral_even(numeral):
    if numeral % 2 == 0:
        return True
    else:
        return False


result = is_the_numeral_even(10)
print(result)


#task_15
#-------------------------------------------
print('Do two given circles intersect in the plane?')

def is_circles_intersect (x1, x2, r1, y1, y2, r2):
    distance_between_centres = math.sqrt((y1 - x1)**2 + (y2 - x2)**2)
    sum_of_radiuses = r1 + r2
    if distance_between_centres > sum_of_radiuses or distance_between_centres < abs(r1 - r2):
        return False
    else:
        return True


result1 = is_circles_intersect(0, 0, 5, 0, 0, 4)
print(result1)



#task_16
#---------------------------------------------
print("Two trains move at a given speed. Between them is 10 km. The first train can turn off the road after 4 km ."
      "Will the trains collide?")


def is_the_trains_crash (velocity1, velocity2):
    distance = 10
    time_train_1 = (distance - 6)/velocity1
    time_train_2 = (distance - 4)/velocity2
    if time_train_1 < time_train_2:
        return False
    else:
        return True

result2 = is_the_trains_crash(30, 60)
print(result2)
