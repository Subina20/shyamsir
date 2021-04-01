'''
nested loop
-------------
-------------
'''


for i in range(4):
    for i in range(4):
         print('*',end='')
    print()

for i in range(2):
    for i in range(3):
        print('2',end=' ')
    print()


'''

'''
a=0
for i in range(4):
    for i in range(i + 1):
        print(a,end=' ')
        a = a+1
    print()  




a=0
for i in range(4):
    for i in range(i + 1):
        print(a,end=' ')
    a = a+1
    print()



