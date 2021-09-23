def fibb(a):
    ''' Calculates fibbinocci series for the given number
        Input: a (positive int
        Output: sum of the series produced by fibbinocci series'''

    if a==0 or a==1:
        return 1

    else:
        return fibb(a-1)+fibb(a-2)


x = int(input("Enter a number: "))
print(f"Sum of fibbinocci series for {x} numbers is: {fibb(x)}")
