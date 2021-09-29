def fibb(n, d):
    ''' Calculates fibbinocci series for the given number
        Input: n positive int
               d dictionary
        Output: sum of the series produced by fibbinocci series'''

    if n in d:
        return d[n]

    else:
        ans = fibb(n-1, d)+fibb(n-2, d)
        d[n] = ans
        return ans

d={1:1, 2:2}
x = int(input("Enter a number: "))
print(f"The {x} numbers in Fibbinocci series is: {fibb(x,d)}\n")
print(f"The Fibbinocci series is: {d.values()}")
