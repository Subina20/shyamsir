'''
if statement
-------------

if <condition>:
    <statement>

-----------------------------
if-else statement
----------------------
if<condition>:
    <statement>
else:
    <statement>

-------------------------------
elif statement:
--------------
if <condition>:
    <statement>
elif <condition>:
    <statement>
elif <condition>
    <statement>
.
.
.
else:
    <statement>

'''

num = int(input('enter the number: '))
if num==0:
    print('number is zero')
elif num<0:
    print('the number is negative')
elif num>0:
        print('number is positive')
print('program i over')



num = int(input('enter the week number: '))
if num ==1:
    print('it is sunday: ')
elif num ==2:
    print('it is monday')
elif num ==3:
    print('it is tuesday')
elif num ==4:
    print('it is wenesday')
elif num ==5:
    print('it is thrusday')
elif num ==6:
    print('it is friday')
elif num ==7:
    print('it is saturday')
else:
    print('not a valid week number') 