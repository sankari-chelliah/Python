#finding factorial

a = int(input("Enter a number to find factorial: "))
def fact(n):
    """
    Accepts an int n as input and returns factorial of it
    """
    if n==1:
        return 1
    else:
        return n* fact(n-1)

print(f"The factorial of {a} is {fact(a)}")
