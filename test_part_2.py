#task_5
#--------------------------------------
def nearest_number(digit_1, digit_2):
    digit_list = []
    digit_list += digit_1, digit_2
    print(digit_list)
    next_number_to_ten = 10
    digit_list.sort(key=lambda elem: abs(next_number_to_ten - elem))
    return digit_list[0]


result = nearest_number(21, 5)
print('The nearest number to ten is %d' % result)


#task_6
#-------------------------------------
def str_isogram(word):
    list_isogram = []
    for c in word:

        if c not in list_isogram:
            list_isogram.append(c)

        else:
            print('The word is not isogram')
    return word



result = str_isogram('woorld')
print(result)



#task_7
#------------------------------------
def sum_fibonacci(number_1, number_2):
    lst = []
    lst += number_1, number_2
    while len(lst) < 10:
            sum_of_elem = lst[-1] + lst[-2]
            lst.append(sum_of_elem)
    return lst[-1]


result = sum_fibonacci(0, 1)
print('The sum of first ten fibonacci numbers is: %s' % result)


#task_8
#-------------------------------------
def sorted_list(list):
    min_elem = min(list)
    max_elem = max(list)
    idx_min_elem = list.index(min_elem)
    idx_max_elem = list.index(max_elem)
    b = list[idx_min_elem]
    list[idx_min_elem] = list[idx_max_elem]
    list[idx_max_elem] = b
    return list


result = sorted_list([1, 3, 9, 4, 8, 3])
print(result)


#task_9
#--------------------------------------
def rationing(list):

    module_list = []
    ration_list = []
    for i in list:
        module_number = abs(i)
        module_list.append(module_number)
        max_number = max(module_list)
        if max_number != 0:
            ration_number = i / max_number
            ration_list.append(ration_number)
    return list, ration_list


result = rationing([-5, 3, 4])
print(result)

