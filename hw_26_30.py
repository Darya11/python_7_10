import random
list_of_random_digits = [random.randint(-1, 1) for x in range(11)]

print('Random list is: %s' % list_of_random_digits)

def calc_frequency(list_of_random_digits):
    frequency_of_minus_1 = sum([1 for elem in list_of_random_digits if elem == -1])
    frequency_of_0 = sum([1 for elem in list_of_random_digits if elem == 0])
    frequency_of_1 = sum([1 for elem in list_of_random_digits if elem == 1])
    list_of_frequences = [frequency_of_minus_1, frequency_of_0, frequency_of_1]
    print('Frequency calculation of numbers in random list %s' % list_of_random_digits,'is: %s' % list_of_frequences)
    print('Max number of frequency is:')

    for i in list_of_frequences:
        if list_of_frequences[0] != list_of_frequences[1] and list_of_frequences[0] != list_of_frequences[2]\
                and list_of_frequences[1] != list_of_frequences[2]:
            return max(list_of_frequences)
        else:
            return None


result_1 = calc_frequency(list_of_random_digits)
print(result_1)


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
