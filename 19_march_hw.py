#A
#B B
#C C C
#D D D D

for i in range(65,70):
    for j in range(65, i+1):
        print(chr(i), end = " ")
    print()




# * * * *
# * * *
# * *
# *

for i in range(5, 1, -1):
    for j in range(i-1):
        print("*", end = " ")
    print()




# A
# B C
# D E F
# G H I J

p=65
for i in range(4):
    for j in range(i+1):
        print(chr(p), end = " ")
        p= p+1
    print()


# A B C D
# E F G
# H I
# J

p = 65
for i in range(4, 0, -1):
    for j in range(i):
        print(chr(p), end = " ")
        p +=1
    print()



