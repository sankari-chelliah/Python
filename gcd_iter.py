def gcdIter(a, b):
    ''' Calculates GCD of 2 numbers
        Input: a (positive int), b(positive int)
        Output: gcd of a and b (int)'''

    c = min(a,b)
    while c >= 1:
        if c == 1:
            return c
            break
        else:
            if a%c==0 and b%c==0:
                return c
                break
            else:
                c -= 1
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"The greatest common factor of {x} and {y} is {gcdIter(x,y)}")
