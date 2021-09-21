# Finding number of occurences of bob
s= str(input("Enter string: "))
s=s.lower()
a=s.split("bob")  #Split input string into an array with separator bob
print(f"Number of times bob occurs is: {(len(a)-1)}")
