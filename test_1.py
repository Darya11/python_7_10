#task_1
#--------------------------------------
a = 5
b = 7
c = 9
equation_1 = (a + b * c)**2
result_1 = (equation_1)
print('The result of equation (a + b * c)**2 is: %d' % result_1)

#task_2
#--------------------------------------
a = 10
b = 2
c = 3
equation_2 = a - 4 * b / c
result_2 = (equation_2)
print('The result of equation a - 4 * b / c is: %d' % result_2)

#task_3
#--------------------------------------
a = 15
b = 20
c =35
equation_3 = (a * b + 4) / (c - 1)
result_3 = equation_3
print('The result of equation (a * b + 4) / (c - 1) is: %d' % result_3)


#task_4
#--------------------------------------
while True:
    five_digit_number = input('Press the five-digit number')

    valid_input = True
    if not five_digit_number.isnumeric():
        valid_input = False

    elif not (10000 <= int(five_digit_number) <= 100000):
        valid_input = False

    if not valid_input:
         print('Press the number from 10000 to 100000')
         continue

    five_digit_number = int(five_digit_number)
    lst = []
    digit = five_digit_number
    full_number = five_digit_number
    while full_number > 0:
        digit = full_number % 10
        full_number = full_number // 10
        if digit % 2 != 0:
            lst.append(digit)
    sum_of_odd = sum(lst)
    print('The sum of odd in your five-digit number is: %d' % sum_of_odd)






