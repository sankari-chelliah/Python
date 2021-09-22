#Program to convert floating point number to Binary number

num= float(input("Enter Float Number: "))

p=0

#Convert the decimal number into a smallest whole number possible by multiplying 2**P,
#find the binary, then devide the result by 2**p
while ((2**p)*num)%1 != 0:
    print((2**p)*num - int((2**p)*num))
    p=p+1

num = int((2**p)*num)
result=''


# Does actual binary conversion
while num>0:
    result=str(num%2)+result
    num=num//2

#Shifts digits to right if needed
for i in range(p - len(result)):
    result='0'+result

#Add decimal point in the appropriate place
result = result[0:-p]+'.'+result[-p:]
print(f"result: {result}")
