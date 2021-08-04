the_count= [1,2,3,4,5]
fruits = ['apple', 'orange','banana','papaya','mango']
change = [1, 'pennies',2,'dimes',3,'quaters']
elements = []

for i in the_count:
    print("The count is {}".format(i))

for j in fruits:
    print(f"The fruit is {j}")

for k in change:
    print(f"I got {k}")

for x in range(0,10):
    print(f"Adding {x} to list")
    elements.append(x)

for y in elements:
    print(f"Values in new list is {y}")
