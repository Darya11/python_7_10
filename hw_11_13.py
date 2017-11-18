import math

#task_11
#---------------------------------

def degrees_to_radians (value1, value2, value3):
   return math.cos(math.radians(value1)), math.cos(math.radians(value2)), math.cos(math.radians(value3))

result1, result2, result3 = degrees_to_radians (60, 45, 40)
print('Значение косинусов улов в 60, 45, 40 градусов в радианах равно: %.1f' % result1,
      '%.1f' % result2, '%.1f' % result3)

#task_12
#---------------------------------

def sum_of_all_numerals (numeral):
    sum = (numeral // 100) + (numeral % 100 // 10) + (numeral % 10)
    return sum

result = sum_of_all_numerals(257)
print('Сумма цифр трехзначного числа равна:', result)


#task_13
#----------------------------------
def right_triangle(cathetus_1, cathetus_2):
    hypotenuse = math.sqrt(pow(cathetus_1, 2) + pow(cathetus_2, 2))
    triangle_perimeter = hypotenuse + cathetus_1 + cathetus_2
    triangle_square = 1/2 * cathetus_1*cathetus_2
    return triangle_perimeter, triangle_square

result_1, result_2 = right_triangle(5,6)
print('Периметр и площадь прямоугольного треугольника равно: ' '%.1f'% result_1, 'см. и', int(result_2), 'см.')












