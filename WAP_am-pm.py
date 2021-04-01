#write a program to find A.M or P.M from the time given by the user.


time = int(input("enter a time: "))
if time<12 and time>0:
    print('it is am')
elif time>12 and time<24:
    print('it is P.M')
