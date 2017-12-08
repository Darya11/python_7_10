import random
import string
import math
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


#task_23
#------------------------------------

random_number = random.randint(1, 10)
print(random_number)

while True:
    user_choice = input()

    valid_input = True
    if not user_choice.isnumeric():
        valid_input = False

    elif not (1 <= int(user_choice) <= 10):
        valid_input = False

    if not valid_input:
        print('Press the number from 1 to 10')
        continue

    user_choice = int(user_choice)
    if user_choice > random_number:
        print("The number is smaller, try again")

    elif user_choice < random_number:
        print("The number is bigger, try again")

    elif user_choice == random_number:
        print("You have guessed the number")
        break



#task_24
#------------------------------------------------

def chess_reward():
    quantaty_of_corn_more_million = 1

    while quantaty_of_corn_more_million < 1000000:
        quantaty_of_corn_more_million *= 2

    quantaty_of_corn_more_million = quantaty_of_corn_more_million - 1
    cell_of_chess = math.log2(quantaty_of_corn_more_million)


    return round(cell_of_chess), quantaty_of_corn_more_million


result = chess_reward()
print('The number of cell from what the quantaty of corns is more million: %d' % result[0],
      ' and the total amount of corns is: %d' % result[1])