import random
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
    return sum(lst)


result = sum_fibonacci(1, 1)
print('The sum of first ten fibonacci numbers is: %s' % result)


#task_8
#-------------------------------------
def sorted_list(list):
    min_elem = min(list)
    max_elem = max(list)
    idx_min_elem = list.index(min_elem)
    idx_max_elem = list.index(max_elem)
    list[idx_min_elem], list[idx_max_elem] = list[idx_max_elem], list[idx_min_elem]
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
    for i in list:
        if max_number != 0:
            ration_number = i / max_number
            ration_list.append(ration_number)
    return list, ration_list


result = rationing([4, 3, -5])
print(result)

#task_10
#----------------------------------------
def saddle_points(matrix):
    rowmins = []
    rowmaxs = []
    colmins = []
    colmaxs = []

    for i,row in enumerate(matrix):
        min_row = min(row)
        max_row = max(row)
        for j,x in enumerate(row):
            if x == min_row: rowmins.append((i,j))
            if x == max_row: rowmaxs.append((i,j))

    column_list = [list(column) for column in zip(*matrix)]

    for j,column in enumerate(column_list):
        min_column = min(column)
        max_column = max(column)
        for i,x in enumerate(column):
            if x == min_column: colmins.append((i,j))
            if x == max_column: colmaxs.append((i,j))


    return (set(rowmins) & set(colmaxs)) | (set(rowmaxs) & set(colmins))


matrix = [[3, 8, 7], [5, 9, 6], [2, 6, 7]]
print(saddle_points(matrix))


#task_12
#---------------------------------
def multiplication_equation():
    multiplication_list = []
    while len(multiplication_list) < 15:
        i = random.randint(2, 9)
        b = random.randint(2, 9)


        multiplication_numbers = i * b
        if i!=b and b !=i and multiplication_numbers not in multiplication_list:
            multiplication_list.append(multiplication_numbers)
            print(i, '*', b)

    return multiplication_list


result = multiplication_equation()
print(result)

