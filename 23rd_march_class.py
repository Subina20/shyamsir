#The python code below calaculates the multiplication of 3 up to 1. Rewrite the code using recursion.
#code to calculate the multiplication of 3.


a =int(input('enter the number:'))
for i in range(1,11):
    mul = a * i
    print(f"{a} * {i} = {mul}")







#what will be the output of following program?. Rewrite the code using while loop to display the same output.

i = 0
while i<=4:
    if i == 3:
        break
    print(i)
    i = i + 1



#What will be the output of the following program?. Rewrite the code using for loop to display same output .


for i in range(1,7):
    if i== 3:
        continue
    print(i)


#The python code below generates 50 random even integers. Rewrite the code so it uses a while loop instead of for loop.


import random
i = 0
mylist =[]
+cv