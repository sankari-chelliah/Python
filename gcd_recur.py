def gcdRecur(a, b):
    ''' Calculates GCD of 2 numbers
        Input: a (positive int), b(positive int)
        Output: gcd of a and b (int)'''

    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"The greatest common factor of {x} and {y} is {gcdRecur(x,y)}")
