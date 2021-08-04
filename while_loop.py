i=0
numbers = []

while i<6:
    print(f"Adding {i} to list")
    numbers.append(i)
    i += 1
    print("Numbers now:", numbers)
    print(f" The next value of i is: {i}")
    print("\n")

print("The numbers: ")
for a in numbers:
    print(a)
