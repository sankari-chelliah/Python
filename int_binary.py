#Program to convert integer to Binary number

num= int(input("Enter Number: "))

result=''
#Check the sign of the number
if num<0:
    isneg=True
    num = abs(num)
elif num==0:
    result='0'
else:
    isneg= False

# Does actual binary conversion
while num>0:
    result=str(num%2)+result
    num=num//2

#Display result with the sign of the input
if isneg==True:
    print(f"-{result}")
else:
    print(result)
