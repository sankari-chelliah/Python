def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''

    if exp==0:
       return 1
    else:
        return base * recurPower(base,exp-1)

from decimal import Decimal
a = Decimal(input("Enter a base: "))
b = int(input("Enter a exp: "))
print(f"{a} to the power {b} is {recurPower(a,b)}")
