#Reverse the digits of a number
from math import copysign
sign = lambda m : copysign(1, m)

x = int(input("Enter a positive or negative integer"))
s=sign(x)
y = abs(x)
z=str(y)
a=z[::-1]
print ("The reversed value is:",end='')
if s<0:
    print(f"-{a}")
else:
    print(a)
