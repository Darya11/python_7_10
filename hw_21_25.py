import random
import string
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


#task_22
#---------------------------------------
def group_by_surname(list_of_enrollees):
    alphabets = ['ABCDEFGHI', 'JKLMNOP', 'QRST', 'UVWXYZ']
    surname = sum([1 for elem in list_of_enrollees if elem.split(' ')[1][0] in alphabets[0]])
    surname_2 = sum([1 for elem in list_of_enrollees if elem.split(' ')[1][0] in alphabets[1]])
    surname_3 = sum([1 for elem in list_of_enrollees if elem.split(' ')[1][0] in alphabets[2]])
    surname_4 = sum([1 for elem in list_of_enrollees if elem.split(' ')[1][0] in alphabets[3]])
    return (surname, surname_2, surname_3, surname_4)


result = group_by_surname(['Will Smith', 'Robin Clarks', 'Ivan Tray', 'Brian Mello'])

print('The quantity of students in groups are: '
      'A-I: %d' % result[0], 'J-K: %d' % result[1] , 'Q-T: %d' % result[2], 'U-Z: %d' % result[3])
