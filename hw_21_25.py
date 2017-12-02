import random
#task_21
#-----------------------------------

number = random.randint(100000000000, 999999999999.)


def get_max_digit(number):
    max_digit = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > max_digit:
            max_digit = number % 10
        number = number // 10
    return max_digit


result2 = get_max_digit(number)
print(result2)
print('The max digit in random twelve-digits number %d' % number, 'is: %d' % result2)