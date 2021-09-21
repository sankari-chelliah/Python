# Finding number of occurences of bob
s= str(input("Enter string: "))
s=s.lower()

#method1
bob_count = s.count("bob")
print(f"Number of times bob occurs is: {bob_count}")

#method2
#a=s.split("bob")  #Split input string into an array with separator bob
#print(f"Number of times bob occurs is: {(len(a)-1)}")
