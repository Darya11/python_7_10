#task_7
#-----------------------------------------------
date_us = '05.17.2016'
print(date_us)
date_eu = date_us.split(".")
print(date_eu[1] + '.' + date_eu[0] + '.' + date_eu[2])


#task_8
#------------------------------------------------
name_surname = 'Mark Zuckerberg'
print(name_surname)
surname_name = name_surname.split(' ')
print(surname_name[1] + ' ' + surname_name[0])


#task_9
#------------------------------------------------
snake_style = 'employee_first_name'
print(snake_style)
camelized_style = snake_style.split('_')
print(camelized_style[0].capitalize() + camelized_style[1].capitalize() + camelized_style[2].capitalize())


#task_10
#-------------------------------------------------
leo_tolstoy ='Leo Tolstoy*1828-08-28*1910-11-20'.split('*')
birth_date = leo_tolstoy[1].split("-")
death_date = leo_tolstoy[2].split("-")
age = int(death_date[0]) - int(birth_date[0])
print(leo_tolstoy[0] + ' ' + str(age))




