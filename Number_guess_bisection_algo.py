#Guess number between 0 and 100 - inclusive (Bisection_algorithm)
print ("Please think of a number between 0 and 100!")
low = 0
high =100
check = 'a'
while check!='c':
    a = (low+high)//2
    print (f"Is your number: {a}")
    check = input("Press\n'l' for low\n'h' for high\n'c' for correct: ")

    if check  == 'l':
        low = a
    elif check == 'h':
        high = a
    elif check == 'c':
         print(f"The number you thought is:{a}")
         break
    else:
         print("Type the correct option")
