ten_things = "apple Orange Grape PineApple Banana Kiwi Mango"

things_list = ten_things.split()

family =["Baby", "Boy", "Girl", "Dad", "Mom"]

while len(things_list) !=10:
    print (f"There are {len(things_list)} items in the list, lets add one more")
    next_item = family.pop()
    print (f"Adding {next_item} to list")
    things_list.append(next_item)

print (f"Here is the final list: {things_list}")
print (f"Items remaining in family: {family}")

print ('\n')
print (things_list[0])
print (things_list[1])
print (things_list[-1])
#print (things_list.pop())
print (' '.join(things_list))
print ('#'.join(things_list))
