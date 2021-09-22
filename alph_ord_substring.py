s='aabbccdamzxybghmnozk'     #s='aabcdamzxybghmnozk'
arr=[]
print(len(s))
for i in range(len(s)-1):
    if s[i]<=s[i+1]:
        arr.append(i)
        arr.append(i+1)
        print(s[i]+s[i+1])

    else:
        arr.append("#")
print(arr)
#[0, 1, 1, 2, 2, 3, 3, 4, '#', 5, 6, 6, 7, '#', 8, 9, '#', 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, '#']

arr2=[]
for j in arr:
    if j!="#":
        if j not in arr2:
            arr2.append(j)
    else:
        arr2.append("$")

print(arr2)
#[0, 1, 2, 3, 4, '$', 5, 6, 7, '$', 8, 9, '$', 10, 11, 12, 13, 14, 15, 16, '$']

a=''
for j in arr2:
    if j!='$':
        a = a + str(s[j])
    else:
        a=a+ ' '
a= a.strip()
print(a)

#aabcd amz xy bghmnoz

arr3 = a.split(" ")
print(arr3)

#['aabcd', 'amz', 'xy', 'bghmnoz']

arr4=[]
for k in arr3:
    arr4.append(len(k))
print(arr4)
max1 = max(arr4)
print(max1)  #7

#[5, 3, 2, 7]
dict1={}
for n in range(len(arr3)):
    if arr3[n] not in dict1:
        dict1.update({arr3[n]:arr4[n]})
print(dict1)

#{'aabcd': 5, 'amz': 3, 'xy': 2, 'bghmnoz': 7}


for c,d in dict1.items():
    if d == max1:
        print(f"The substring is {c}")
        break
