formatter ="{} {} {} {}"

print(formatter.format(1,2,3,4,5)) #the extra 5 do no harm, but if arg is less than 4 then it shows error
print(formatter.format("One","Two","Three","Four"))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
"I like Popcorn, ",
"I like Tea, ",
"I want you to ..... ",
"Jump with me!"))
