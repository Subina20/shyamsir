num = int(input('enter the number: '))
while num>0:
    rem = num % 10
    print(rem)
    num=num//10


#write a program  to check a number given by the user is armstrong or not.


num = int(input('enter any number: '))
sum = 0
while num>0:
    rem = num % 10
    sum= sum + rem**3
    num = num // 10
print(sum)
if sum == 0:
    print('it is armstrong')
else:
    print('it is not armstrong: ')


