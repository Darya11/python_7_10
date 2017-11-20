import math

#task_11
#---------------------------------

def degrees_to_radians (value):
   return math.cos(math.radians(value))

result1 = degrees_to_radians (60)
result2 = degrees_to_radians(45)
result3 = degrees_to_radians(40)
print('Значение косинусов улов в градусах будет равно в радианах: %.1f' % result1,
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
def right_triangle_perimeter_and_square(cathetus_1, cathetus_2):
    hypotenuse = math.sqrt(pow(cathetus_1, 2) + pow(cathetus_2, 2))
    triangle_perimeter = hypotenuse + cathetus_1 + cathetus_2
    triangle_square = 1/2 * cathetus_1*cathetus_2
    return triangle_perimeter, triangle_square

result_1, result_2 = right_triangle_perimeter_and_square(5,6)
print('Периметр и площадь прямоугольного треугольника равно: ' '%.1f'% result_1, 'см. и', int(result_2), 'см.')












