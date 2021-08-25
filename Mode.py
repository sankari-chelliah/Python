input_list= [10,10,10,50,50,50,20,90,70]   #Input List
unq_list= list(set(input_list))            #Make it a set to get Unique values
unq_list.sort()                            #Sort in Asc order

# Declaration for intermediate steps
dict_val_count={}
listx=[]

#Add list elements and its count in key:Pair value in a dictionary
for x in unq_list:
    y= input_list.count(x)
    dict_val_count[x]=y


a = max(dict_val_count.values())  #Find max count from dict values


#Make a new list with only keys that occurs max times in input list
for n,m in dict_val_count.items():
    if m>=a:

        listx.append(n)

#Display min number in list that occurs most frequently
print(f"Mode of list{input_list} is : {min(listx)}")
