age = int(input('enter the user age: '))
if age < 15:
    print('you are a child')
elif age > 15 and age < 40:
    print('you are a adult')
elif age > 40:
    print('you are old')
elif age < 0:
    print('not valid')





salary = 20000.0
expenses = (10/100)*salary
net_salary = salary - expenses
print('the net salary is',net_salary)