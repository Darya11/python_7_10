import random
import string

list_of_random_digits = [random.randint(-1, 1) for x in range(11)]

print('Random list is: %s' % list_of_random_digits)

def calc_frequency(list_of_random_digits):
    frequency_of_minus_1 = sum([1 for elem in list_of_random_digits if elem == -1])
    frequency_of_0 = sum([1 for elem in list_of_random_digits if elem == 0])
    frequency_of_1 = sum([1 for elem in list_of_random_digits if elem == 1])
    list_of_frequences = [frequency_of_minus_1, frequency_of_0, frequency_of_1]
    print('Frequency calculation of numbers in random list %s' % list_of_random_digits,'is: %s' % list_of_frequences)
    print('Max number of frequency is:')

    if frequency_of_minus_1 > frequency_of_0 and frequency_of_minus_1 > frequency_of_1:
        return frequency_of_minus_1
    elif frequency_of_0 > frequency_of_minus_1 and frequency_of_0 > frequency_of_1:
        return frequency_of_0
    elif frequency_of_1 > frequency_of_minus_1 and frequency_of_1 > frequency_of_0:
        return frequency_of_1




result_1 = calc_frequency(list_of_random_digits)
print(result_1)

#task_28
#-----------------------------------
cipher_list = string.ascii_lowercase + string.digits

str_to_encode = input().lower()

def encode(str_to_encode):
    cipter_str = ''

    for i in str_to_encode:
        if i not in cipher_list:
            cipter_str += i
            continue

        j = (cipher_list.index(i) + 5) % len(cipher_list)
        cipter_str += cipher_list[j]

    return cipter_str

print(encode(str_to_encode))
#task_29
#-----------------------------------

def gen_password():
    password = []
    b = string.ascii_lowercase
    c = string.ascii_uppercase + string.digits + '_'
    d = string.digits + '_'


    a_1 = ([password.append(random.choice(b)) for x in range(4) ])
    a_2 = ([password.append(random.choice(c)) for x in range(4)])
    a_3 = ([password.append(random.choice(d)) for x in range(2)])
    return ''.join(password)


print(gen_password())


#task_30
#------------------------------------
def gen_primes():
    list_of_numbers = []
    for i in range(2, 101):
            for j in list_of_numbers:
                if i % j == 0:
                    break
            else:
                list_of_numbers.append(i)
    return list_of_numbers


result_2 = gen_primes()
print(result_2)
