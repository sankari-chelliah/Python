s='abcdefghijklmno'
count = 0
for x in s:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count +=1
print(f"Number of vowels: {count}")
