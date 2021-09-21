#Guess number between 0 and 100 - inclusive (Bisection_algorithm)
print ("Please think of a number between 0 and 100!")
low = 0
high =100
check = 'a'
while check!='c':
    a = (low+high)//2
    print (f"Is your secret number {a}")
    check = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if check  == 'l':
        low = a
    elif check == 'h':
        high = a
    elif check == 'c':
         print(f"Game over. Your secret number was: {a}")
         break
    else:
         print("Type the correct option")
