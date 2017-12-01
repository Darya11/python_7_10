import random
#task_21
#-----------------------------------

def get_number_of_twelwe_digits(num_limited, lower_bound, upper_bound):
    number = 0

    for i in range(num_limited):
        random_number = random.randint(lower_bound, upper_bound)
        number = random_number
    return number


number = get_number_of_twelwe_digits(1, 100000000000, 1000000000000)
print(number)


def get_max_digit(number):
    number_of_twelwe_digits = number
    max_digit = number_of_twelwe_digits % 10
    number_of_twelwe_digits = number_of_twelwe_digits // 10
    while number_of_twelwe_digits > 0:
        if number_of_twelwe_digits % 10 > max_digit:
            max_digit = number_of_twelwe_digits % 10
        number_of_twelwe_digits = number_of_twelwe_digits // 10
    return max_digit


result2 = get_max_digit(number)
print(result2)
print('The max digit in radom twelwe-digits number %d' % number, 'is: %d' % result2)