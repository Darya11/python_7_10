#task_7
#-----------------------------------------------
a = '05.17.2016'
print(a)
a = ['05.', '17.', '2016']
a[0], a[1] = a[1], a[0]
b = "".join(a)
print(b)


#task_8
#------------------------------------------------
k = 'Mark Zuckerberg'
print(k)
lst = k.split(' ')
print(lst[1] + ' ' + lst[0])


#task_9
#------------------------------------------------
s = 'employee_first_name'
print(s)
s ='{0}mployee{1}irst{2}ame'.format('E', 'F', 'N')
print(s)


#task_10
#-------------------------------------------------
m ='Leo Tolstoy*1828-08-28*1910-11-20'.split('*')
born = m[1].split("-")
dead = m[2].split("-")
lives = int(dead[0]) - int(born[0])
print(m[0] + ' ' + str(lives))




