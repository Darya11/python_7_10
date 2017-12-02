import math
import random
#task_17
#---------------------------------------



def solve_quadratic_equation(a, b, c):
    find_discriminant = b**2 - (4 * a * c)

    if a == 0:
        return None, None

    elif find_discriminant > 0:
     root1 = (- b + math.sqrt(find_discriminant)) / (2 * a)
     root2 = (- b - math.sqrt(find_discriminant)) / (2 * a)
     return root1, root2

    elif find_discriminant == 0:
        root1 = (- b + math.sqrt(find_discriminant)) / (2 * a)
        return root1, None
    else:
        return None, None


result = solve_quadratic_equation(10, 2, 0)
print('The roots of the quadratic equation are: ', result)


#task_18
#-----------------------------------------

def sum_symbol_codes(first_unicode, last_unicode):
    total_sum = 0
    for i in range(ord(first_unicode), ord(last_unicode) + 1):
        total_sum += i

    return total_sum


result1 = sum_symbol_codes('\a','\r')
print('The sum of symbol codes is:', result1)


#task_19
#------------------------------------------

def diff_min_max(num_limit, lower_bound, upper_bound):
    min_number = upper_bound
    max_number = lower_bound

    for i in range(num_limit):
        random_of_numbers = random.randint(lower_bound, upper_bound)
        print(random_of_numbers)
        if random_of_numbers < min_number:
            min_number = random_of_numbers

        elif random_of_numbers > max_number:
            max_number = random_of_numbers

    return max_number, min_number, (max_number - min_number)


result2 = diff_min_max(5, 10, 20)
print(result2)
print('The total difference between random numerals %d' % result2[0],'and %d' % result2[1],  'is: %d' % result2[2])

#task_20
#------------------------------------------

def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_of_even = 0
    sum_of_odd = 0

    for i in range(num_limit):
        random_number = random.randint(lower_bound, upper_bound)
        print(random_number)
        if random_number % 2 == 0:
            sum_of_even += random_number

        else:
            sum_of_odd += random_number

    return sum_of_even - sum_of_odd


result3 = diff_even_odd(100, 200, 850)
print('The result of the difference between random generated even and odd numbers is', result3)




